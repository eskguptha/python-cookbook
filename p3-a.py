# Program to check if a string
#  is palindrome or not
def str_check_palindrome(val):
    try:
        val = val.lower()
        rev_str = reversed(val)
        if list(val) == list(rev_str):
           return ("It is palindrome")
        else:
           return ("It is not palindrome")
    except Exception as e:
        pass        
        return  "Please enter valid string "

input_val = raw_input("Please Enter any string?")
output_val = str_check_palindrome(input_val)
print (output_val)