async function getMovies () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const movies = await response.json();
  return movies;
}

const listMovies = document.querySelector('#list_movies');

getMovies().then(movies => {
  movies.results.forEach(movie => {
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(movie.title));
    listMovies.appendChild(li);
  });
});
