"""
ASGI config for ft_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from remote.routing import websocket_urlpatterns as remoteSocketsPaths
from chat.routing import websocket_urlpatterns as chatSocketsPaths

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ft_backend.settings")

django_asgi_app = get_asgi_application()

websocket_urlpatterns = remoteSocketsPaths + chatSocketsPaths

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
		"websocket": AllowedHostsOriginValidator(
					AuthMiddlewareStack(URLRouter(websocket_urlpatterns)) 
				),
    }
)
