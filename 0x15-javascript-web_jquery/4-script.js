// JavaScript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header
const toggle_header = function () {
  $("header").toggleClass("red green");
};
$("div#toggle_header").click(toggle_header);
