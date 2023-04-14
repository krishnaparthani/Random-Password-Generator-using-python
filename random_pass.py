import random as ran
import array as arr
 
 

MAX_LEN = 12
 

DIGITS_VALUE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS_VALUE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS_VALUE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS_VALUE = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
COMBINED_LIST_VALUE = DIGITS_VALUE + UPCASE_CHARACTERS_VALUE + LOCASE_CHARACTERS_VALUE + SYMBOLS_VALUE
 
# randomly select at least one character from each character set above
rand_digit_value = ran.choice(DIGITS_VALUE)
rand_upper_value = ran.choice(UPCASE_CHARACTERS_VALUE)
rand_lower_value = ran.choice(LOCASE_CHARACTERS_VALUE)
rand_symbol_value = ran.choice(SYMBOLS_VALUE)
 
temp_pass = rand_digit_value + rand_upper_value + rand_lower_value + rand_symbol_value
 

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + ran.choice(COMBINED_LIST_VALUE)
    temp_pass_list = arr.array('u', temp_pass)
    ran.shuffle(temp_pass_list)
 

password = ""
for x in temp_pass_list:
        password = password + x
         

print(password)