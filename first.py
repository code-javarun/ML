PYTHON STRINGS:
     There are six type of strings they are
        1.slicing string
        2.modify string
        3.concatenate string
        4.format string
        5.escape characters
        6.string methods

        
SLICING STRING:
1.slicing from start
  #Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
2.slicing to the end
   Example:
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
3.negative indexing
  Example
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]).


MODIFY STRING:
1.upper case
   #it changes the statement into uppercase.
   a = "Hello, World!"
print(a.upper())

2.lower case
   #The lower() method returns the string in lower case

      a = "Hello, World!"
      print(a.lower())
3.remove whitespace
   
   #The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
4.replace string
   
   #The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
5.split string
   
   #The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


CONCATINATE STRING:
#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)



FORMAT STRING:
1.f-string
     #f can be used in front of string.
     age = 36
txt = f"My name is John, I am {age}"
print(txt)
2.placeholders and modifiers
#Add a placeholder for the price variable:
     price = 59
txt = f"The price is {price} dollars"
print(txt)


ESCAPE STRING:
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."



STRING METHODS:
    1.Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
