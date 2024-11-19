async function sayHello () {
  const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
  const hello = await response.json();
  console.log(hello);
  return hello;
}

sayHello().then(data => {
  document.querySelector('#hello').textContent = data.hello;
});
