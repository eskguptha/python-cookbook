# converting decimal to binary and binary to decimal     
def ConverDecToBinary(val):
    try:
        dec_val  = int(val)
        if dec_val == 0:
            return "Value Required"
        result = bin(dec_val)
    except (TypeError, ValueError) as e:
        result = "Input value should be number. "+str(e)
        pass
    return result


input_val = raw_input("Please Enter Number?")
output_val = ConverDecToBinary(input_val)
print output_val