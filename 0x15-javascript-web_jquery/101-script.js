$(function () {
  const list = $('UL.my_list');

  $('DIV#add_item').on('click', function (event) {
    list.append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', function (event) {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').on('click', function (event) {
    list.empty();
  });
});
