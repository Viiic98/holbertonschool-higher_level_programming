## 0x13. Javascript - Objects, Scopes and Closures
### Objects, Scopes and Closures

------------

#### Rectangle [0-rectangle.js](./0-rectangle.js)
- Empty class Rectangle that defines a rectangle

#### Rectangle [1-rectangle.js](./1-rectangle.js)
- Class Rectangle that defines a rectangle
	-  Constructor must take 2 arguments w and h

#### Rectangle [2-rectangle.js](./2-rectangle.js)
- Class Rectangle that defines a rectangle
	- Add a condition `if  w or h <= 0` create an empty object

#### Rectangle [3-rectangle.js](./3-rectangle.js)
- Class Rectangle that defines a rectangle
	- Add an instance method called `print` that prints the rectangle using the character `X`

#### Rectangle [4-rectangle.js](./4-rectangle.js)
- Class Rectangle that defines a rectangle
-	- Add an instance method called `rotate` that exchanges the `width` and the `height` of the rectangle
	- Add an instance method called `double` that multiples the `width` and the `height` of the rectangle by 2

#### Square [5-square.js](./5-square.js)
- class Square that defines a square and inherits from Rectangle of [4-rectangle.js](./4-rectangle.js)
	- The constructor of Rectangle is called using `super()`

#### Square [6-square.js](./6-square.js)
- class Square that defines a square and inherits from Square of [5-square.js](./5-square.js)
	- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`

#### Occurrences [7-occurrences.js](./7-occurrences.js)
- Function that returns the number of occurrences in a list

#### Esrever [8-esrever.js](./8-esrever.js)
- Function that returns the reversed version of a list

#### Log me [9-logme.js](./9-logme.js)
- Function that prints the number of arguments already printed and the new argument value.

#### Number conversion [10-converter.js](./10-converter.js)
- Function that converts a number from base 10 to another base passed as argument

#### Factor index [100-map.js](./100-map.js)
- Script that imports an array and computes a new array.
	- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
	- Print both the initial list and the new list

#### Sorted occurences [101-sorted.js](./101-sorted.js)
- Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

#### Concat files [102-concat.js](./102-concat.js)
- Script that concats 2 files.
	- Did it using fs library
