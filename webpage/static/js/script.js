
function assignCard(){
	document.getElementById("karnetId").setAttribute("type","text");
	var button = document.getElementById("karnet");
	button.setAttribute("value","Usuń");
	button.setAttribute("onClick","removeCard()");
}

function removeCard(){
	document.getElementById("karnetId").setAttribute("type","hidden");
	var button = document.getElementById("karnet");
	button.setAttribute("value","Przypisz");
	button.setAttribute("onClick","assignCard()");
}
