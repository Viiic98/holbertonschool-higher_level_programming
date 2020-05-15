$(document).ready(function () {
  function translate (language) {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    translate(language);
  });
});
