// JavaScript script that fetches and prints how to say “Hello” depending on the language
const $ = window.$;
$(document).ready(function () {
  $("input#btn_translate").click(function () {
    const lang = $("input#language_code").val();
    $.post(
      "https://hellosalut.stefanbohacek.dev",
      { lang: $("#language_code").val() },
      function (data) {
        $("#hello").text(data.hello);
      }
    );
  });
  $("input#language_code").keypress(function (e) {
    if (e.which === 13) {
      const lang = $("input#language_code").val();
      $.post(
        "https://hellosalut.stefanbohacek.dev",
        { lang: $("#language_code").val() },
        function (data) {
          $("#hello").text(data.hello);
        }
      );
    }
  });
});
