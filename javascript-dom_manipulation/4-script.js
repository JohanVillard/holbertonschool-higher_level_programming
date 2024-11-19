document.querySelector("#add_item").onclick = () => {
	let li = document.createElement("li");
	li.appendChild(document.createTextNode("Item"));
	document.querySelector(".my_list").appendChild(li);
}
