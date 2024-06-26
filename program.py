import random 
import string 

pass_length = 12
char_value = string.ascii_letters + string.punctuation + string.digits


# LIST COMPREHENSION 

password = "".join([random.choice(char_value) for i in range(pass_length)])
print("Your RANDOM PASSWORD is :",password)


# another simple way using loops
# password = ""
# for i in range(pass_length) :
#     password += random.choice(char_value) 

    
# print("Your Random Password is :" , password)