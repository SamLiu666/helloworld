# Target 

1. Understand the differences between `array` and `dynamic array`;
2. Be familiar with `basic operations` in the array and dynamic array;
3. Understand `multidimensional arrays` and be able to use a `two-dimensional array`;
4. Understand the concept of `string` and the different features string has;
5. Be able to apply the `two-pointer technique` to practical problems.



## Strings

`Immutable` means that you can't change the content of the string once it's initialized.

1. In some languages (like C++), the string is `mutable`. That is to say, you can modify the string just like what you did in an array. 
2. In some other languages (like Java), the string is `immutable`. This feature will bring several problems. We will illustrate the problems and solutions in the next article.

### Modification Operation

------

Obviously, an immutable string cannot be modified. If you want to modify just one of the characters, you have to create a new string.

**convert it to** **a char** **array****.**

 **If you have to concatenate strings often, it will be better to use some other data structures like** **`StringBuilder`****. The below code runs** **in** **`O(n)`** **complexity****.**

## Two-pointer Technique

Iterate the array from two ends to the middle.

One pointer starts from the beginning while the other pointer starts from the end.

Given an array and a value, remove all instances of that value [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.