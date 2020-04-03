
let xhr = new XMLHttpRequest();

function post(tuple){
	xhr.open("POST", "https://localhost:5000/", true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.send(JSON.stringify({
		value: tuple
	}));
}


post("{shiii}")
