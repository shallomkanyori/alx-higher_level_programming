const list = $('UL.my_list');

$('DIV#add_item').on('click', function (event) {
  list.append('<li>Item</li>');
});
