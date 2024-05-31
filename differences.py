# 1. Get Name

# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# def get_name():
#     name = input("What is your name? ")
#     return name

# print(get_name())

# 2. Reverse It

# Write a method that reverses a string. Here’s the javascript:


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

# def reverse_it(string):
#     reverse = ''
#     for letter in string:
#         reverse = letter + reverse
#     print(reverse)

# reverse_it('hello world')

# 3. Swap Em

# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

# def swapEm():
#     a = 1
#     b = 2
#     [a, b] = [b, a]
#     print('a is now ' + str(a) + '. and b is now '+ str(b))
# swapEm()

# 4. Multiply Array/List

# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# def multiplyList(list):
#     total = 1
#     for x in range(len(list)):
#         total *= list[x]
#     print(total)

# multiplyList([2, 3, 4])

# 5. Fizz Buzzer

# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

# def fizzBuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print('fizzbuzz')
#     elif number % 5 == 0:
#         print('buzz')
#     elif number % 3 == 0:
#         print('fizz')

# fizzBuzz(15)

# 5. Nth Fibonacci

# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

# the fibonacci numbers are 0,1,1,2,3,5,8,13,21,34,…

# def get_fib():
#     fibs = [0, 1]
#     selection = input('Which Fibonnacci number do you want? Please pick an integer greater than zero. ')
#     selection = int(selection)
#     if selection < 1:
#         print("Bye.")
#     elif selection < 3:
#         print(fibs[selection -1])
#     else: 
#         while len(fibs) < selection:
#             fibs.append(fibs[-2] + fibs[-1])
#         print(fibs[-1])

# get_fib()

# 6. Search Array/List

# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

# def isInList(list, val):
#     if val in list:
#         return True
#     else:
#         return False

# print(isInList([1, 2, 'x'], 1))

# 7. Palindrome

# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

# def isPalindrome(string):
#     forwards = string
#     backwards = ''
#     for letter in string:
#         backwards = letter + backwards
#     if backwards == forwards:
#         return True
#     else:
#         return False
    
# print(isPalindrome('racecar'))

# 8. hasDupes

# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

# def hasDupes(list):
#     dictionary = {}
#     for i in range(len(list)):
#         if str(list[i]) in dictionary:
#             return True
#         else:
#             dictionary[str(list[i])] = True
#     return False

# print(hasDupes([1, 2, 'x', 'x']))