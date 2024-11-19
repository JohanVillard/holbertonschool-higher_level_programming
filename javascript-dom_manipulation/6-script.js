async function getCharacter() {
	const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
	const character = await response.json();
	return character;
}

getCharacter().then(character => {
	document.querySelector("#character").textContent = character.name;
});
