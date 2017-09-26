
def valber_check_palindrome(val):
	try:
		val = int(val)
		n = val
		sum1 = 0
		while val!=0:
			rem=val%10
			sum1=sum1*10+rem
			val=val/10
		if sum1==n:
			return  n, "is palindrome"
		else:
			return n, "is not palindrome"
	except Exception as e:
		pass
		return "Please Enter Valid Number"



input_val = raw_input("Please Enter any Number?")
output_val = valber_check_palindrome(input_val)
print output_val
