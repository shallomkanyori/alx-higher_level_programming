$(function () {
  const helloDiv = $('DIV#hello');

  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    helloDiv.text(response.hello);
  });
});
