let ws = new WebSocket("ws://" + location.host + "/ws");

ws.onmessage = function(event) {

	let data = JSON.parse(event.data);

	console.log("GPS update:", data);

	document.getElementById("lat").innerText = data.lat;
	document.getElementById("lon").innerText = data.lon;
	document.getElementById("alt").innerText = data.alt;
};
