// JavaScript script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $("#btn_translate").click(function () {
    $.post(
      "https://hellosalut.stefanbohacek.dev",
      { lang: $("#language_code").val() },
      function (data) {
        $("#hello").text(data.hello);
      }
    );
  });
});
