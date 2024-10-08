import json
import base64
import hashlib
import hmac
from datetime import datetime, timedelta
import os
from django.core import serializers

def generate_jwt(user_obj):
    payload = {
        'user': serializers.serialize("json", [user_obj]),
        'exp': datetime.timestamp(datetime.utcnow() + timedelta(days=1)),
    }

    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8'))

    secret_key = os.environ.get("JWT_SECRET")
    signature = hmac.new(secret_key.encode('utf-8'), encoded_payload, hashlib.sha256).digest()
    encoded_signature = base64.urlsafe_b64encode(signature)

    jwt_token = f"{encoded_payload.decode('utf-8')}.{encoded_signature.decode('utf-8')}"

    return jwt_token

def decode_jwt(jwt_token):
    try:
        encoded_payload, encoded_signature = jwt_token.split('.')
    except:
        return {
            'error': 'Invalid token signature'
        }

    payload = json.loads(base64.urlsafe_b64decode(encoded_payload.encode('utf-8')).decode('utf-8'))

    secret_key = os.environ.get("JWT_SECRET")
    expected_signature = base64.urlsafe_b64encode(hmac.new(secret_key.encode('utf-8'), encoded_payload.encode('utf-8'), hashlib.sha256).digest())

    if encoded_signature == expected_signature.decode('utf-8'):
        return payload
    else:
        return {
            'error': 'Invalid token signature'
        }
