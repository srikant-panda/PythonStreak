#le?ts define a string then porform methods on it
my_string = "backend using python."

## string slicing

# sliced_string = my_string[0:4]
# print(sliced_string)   #It starts from 0 index and go to 3 index.

# print(my_string[-2:-1]) # negetive indexing


## Upper Case upper()

# print(my_string.upper()) # converts whole string to upper case

##Lower Case

# print(my_string.lower()) #converts whole string to lower case

##remove Whitespace
# a = " python"
# print(a.strip())

## Split string using split() which return a kist containig the spited text

# a = "Hello, World"
# print(a.split(","))
# print(my_string.split())

## String Concatination

# a= "Do "
# print(a+my_string)

## String Format "f-strings"

# time = 6

# print(f"Do backend using python in {time} months.")

##placeholders
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)