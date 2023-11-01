$(function () {
  function translate () {
    const langCode = $('INPUT#language_code').val();

    $.get('https://hellosalut.stefanbohacek.dev/', { lang: langCode }, function (response) {
      $('DIV#hello').text(response.hello);
    });
  }

  $('INPUT#btn_translate').on('click', function (event) {
    translate();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});
