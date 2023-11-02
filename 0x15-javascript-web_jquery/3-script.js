// JavaScript script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header
const add_class_red = function () {
  $("header").addClass("red");
};
$("div#red_header").click(add_class_red);
