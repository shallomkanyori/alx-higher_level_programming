## JavaScript - Web jQuery

#### Task 0
[0-script.js](0-script.js) is a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
- Uses `document.querySelector` to select the HTML tag
- Does not use the JQuery API

#### Task 1
[1-script.js](1-script.js) is a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 2
[2-script.js](2-script.js) is a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 3
[3-script.js](3-script.js) is a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 4
[4-script.js](4-script.js) is a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`
- The `<header>` element always has one class: `red` or `green`, never both in the same time and never empty.
- If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class is updated to `green` and vice versa.
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 5
[5-script.js](5-script.js) is a a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`
- The new element: `<li>Item</li>`
- The new element is added to `UL.my_list`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 6
[6-script.js](6-script.js) is a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 7
[7-script.js](7-script.js) is a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`
- The name must be displayed in the HTML tag `DIV#character`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 8
[8-script.js](8-script.js) is a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`
- All movie titles are listed in the HTML tag `UL#list_movies`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API

#### Task 9
[9-script.js](9-script.js) is a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
- The translation of “hello” is displayed in the HTML tag `DIV#hello`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API
- Works when it is imported from the `<head>` tag


#### Task 10
[100-script.js](100-script.js) is a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
- Uses `document.querySelector` to select the HTML tag
- Does not use the JQuery API
- Note: Script is imported from the `<head>` tag, not at the end of the HTML

#### Task 11
[101-script.js](101-script.js) is a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks
- The new element: `<li>Item</li>`
- The new element is added to `UL.my_list`
- When the user clicks on `DIV#add_item`: a new element is added to the list
- When the user clicks on `DIV#remove_item`: the last element is removed from the list
- When the user clicks on `DIV#clear_list`: all elements of the list are removed
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API
- Works when it is imported from the `HEAD` tag

#### Task 12
[102-script.js](102-script.js) is a JavaScript script that fetches and prints how to say “Hello” depending on the language.
- Uses this API service: [https://www.fourtonfish.com/hellosalut/hello/](https://www.fourtonfish.com/hellosalut/hello/)
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation is fetched when the user clicks on `INPUT#btn_translate`
- The translation of “Hello” is displayed in the HTML tag `DIV#hello`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API
- Works when it is imported from the `HEAD` tag

#### Task 13
[103-script.js](103-script.js) is a JavaScript script that fetches and prints how to say “Hello” depending on the language.
- Uses this API service: [https://www.fourtonfish.com/hellosalut/hello/](https://www.fourtonfish.com/hellosalut/hello/)
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation is fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
- The translation of “Hello” is displayed in the HTML tag `DIV#hello`
- Does not use `document.querySelector` to select the HTML tag
- Uses the JQuery API
- Works when it is imported from the `HEAD` tag
