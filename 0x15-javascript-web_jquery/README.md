# 0x15. Javascript - Web JQuery

------------

#### No jQuery [0-script.js](./0-script.js)
- Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)`.

#### With jQuery [1-script.js](./1-script.js)
- Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)`.
    - Using JQuery API

#### Click and turn red [2-script.js](./2-script.js)
- Script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#red_header`.

#### Add `.red` class [3-script.js](./3-script.js)
- Script that adds the class red to the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#red_header`.

#### Toggle classes [4-script.js](./4-script.js)
- Script that toggles the class of the HTML tag `HEADER` to red `(#FF0000)` when the user clicks on the tag `DIV#toggle_header`.
    - The `HEADER` tag must always have one class: red or green, never both in the same time, never empty.
    - If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.

#### List of elements [5-script.js](./5-script.js)
- Script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`.

#### Change the text [6-script.js](./6-script.js)
- Script that updates the text of the HTML tag `HEADER` to “New Header!!!” when the user clicks on `DIV#update_header`.

#### Star wars character [7-script.js](./7-script.js)
- Script that fetches and replaces the `name` of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

#### Star Wars movies [8-script.js](./8-script.js)
- Script that fetches and lists all movies `title` by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

#### Say Hello! [9-script.js](./9-script.js)
- Script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML’s tag `DIV#hello`

#### No jQuery - document loaded [100-script.js](./100-script.js)
- script that updates the text color of the HTML tag `HEADER` to red `(#FF0000)`
    - Note: Your script must be imported from the HEAD tag, not at the end of the HTML

#### List, add, remove [101-script.js](./101-script.js)
- script that adds, removes and clears `LI` elements from a list when the user clicks.
    - The new element must be: `<li>Item</li>`
    - The new element must be added to `UL.my_list`
    - When the user clicks on `DIV#add_item`: a new element is added to the list
    - When the user clicks on `DIV#remove_item`: a last element is removed to the list
    - When the user clicks on `DIV#clear_list`: all elements of the list are removed
    - You script must be work when it imported from the `HEAD` tag

#### Say hello to everybody! [102-script.js](./102-script.js)
- Script that fetches and prints how to say “Hello” depending of the language
    - API service: `https://www.fourtonfish.com/hellosalut/hello/`
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
    - The translation must be fetch when the user clicks on `INPUT#btn_translate`
    - The translation of “Hello” must be display in the HTML tag `DIV#hello`

#### And press ENTER [103-script.js](./103-script.js)
- Script that fetches and prints how to say “Hello” depending of the language
    - API service: `https://www.fourtonfish.com/hellosalut/hello/`
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
    - The translation must be fetch when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
    - The translation of “Hello” must be display in the HTML tag `DIV#hello`
