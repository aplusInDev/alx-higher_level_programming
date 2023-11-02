// JavaScript script that updates the text color of the <header>
// element to red (#FF0000) when the user clicks on the tag DIV#red_header
to_red_header = function () {
  $("header").css("color", "#FF0000");
};
$("div#red_header").click(to_red_header);
