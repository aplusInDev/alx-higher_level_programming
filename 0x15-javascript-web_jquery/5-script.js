// JavaScript script that adds a <li> element to a list
// when the user clicks on the tag DIV#add_item
const add_item = function () {
  $("ul.my_list").append("<li>Item</li>");
};
$("div#add_item").click(add_item);
