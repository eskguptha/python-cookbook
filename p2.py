# reverse of a string 
def UpdateSentenceStyle(val):
    try:
        result = ' '.join([(item[::-1]) for item in val.split(' ')])
    except Exception as e:
        result = "Please Enter Valid Sentense."+str(e)
        pass
    return result


input_val = raw_input("Please Enter any Sentence?")
output_val = UpdateSentenceStyle(input_val)
print output_val