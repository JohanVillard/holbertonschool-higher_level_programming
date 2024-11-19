document.querySelector('#add_item').onclick = () => {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  document.querySelector('.my_list').appendChild(li);
};
