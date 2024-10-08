export function changeState(status){
	const $userStatus = document.getElementById("userStatus");
	const $chat = document.getElementById("chat");
	const $chatDisplay = document.getElementById("displayChat");
	$chat.classList.add("d-none");
	$chatDisplay.classList.add("d-none");
	$userStatus.style.color = "blue"
	switch (status) {
        case "Searching game":
            $userStatus.textContent = "Searching game"
            break;
        case "Searching tournament":
            $userStatus.textContent = "Searching tournament"
            break;
        case "In game":
            $userStatus.textContent = "In game"
			$userStatus.style.color = "#ff5252"
            break;
        case "In tournament":
            $userStatus.textContent = "In tournament"
			$userStatus.style.color = "#ff5252"
            break;
		case "Offline":
			$userStatus.textContent = "Offline"
			$userStatus.style.color = "gray"
        default:
            $userStatus.textContent = "Online"
			if ($chatDisplay.classList.contains("d-none"))
				$chatDisplay.classList.remove("d-none")
			$userStatus.style.color = "#56ba6f"
            break;
    }
}

export function putOnline(value)
{
	const $token = sessionStorage.getItem('pongToken');
	if (value){
		const $Url = apiUrl + 'online-status/';

		fetch($Url, {
			method: 'GET',
			headers: {
				"Authorization": $token
			}
		})
		.then(response => {
			if (!response.ok) {
				throw new Error(`Request error: ${response.status}`);
			}
			return response.json()
		})
		.catch(error => {
			console.error('Request error:', error);
		});
	} else {
		const $Url = apiUrl + 'offline-status/';

		fetch($Url, {
			method: 'GET',
			headers: {
				"Authorization": $token
			}
		})
		.then(response => {
			if (!response.ok) {
				throw new Error(`Request error: ${response.status}`);
			}
			return response.json()
		})
		.catch(error => {
			console.error('Request error:', error);
		});
	}
	
}