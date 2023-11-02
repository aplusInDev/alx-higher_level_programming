// JavaScript script that fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (data) {
    for (const movie of data.results) {
      $("ul#list_movies").append(`<li>${movie.title}</li>`);
    }
  }
);
