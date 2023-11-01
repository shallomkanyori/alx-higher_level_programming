$(function () {
  $('INPUT#btn_translate').on('click', function (event) {
    const langCode = $('INPUT#language_code').value();

    $.get('https://hellosalut.stefanbohacek.dev/', { lang: langCode }, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
