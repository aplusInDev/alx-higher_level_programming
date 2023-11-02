// JavaScript script that updates the text of the <header>
// element to New Header!!! when the user clicks on DIV#update_header
const update_header = function () {
  $("header").text("New Header!!!");
};
// const update_header = () => $("header").text("New Header!!!");
$("div#update_header").click(update_header);
