#Code for the ricevault.py file
#-----------------------------------------------------------------------------------------------------------------
def isspecial(char):
    if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*' or char == '(' or char == ')' or char == '_' or char == '+' or char == '-' or char == '=' or char == '{' or char == '}' or char == '[' or char == ']' or char == '|' or char ==  '\'' or char == '<' or char == '>' or char == '.'  or char == '/' or char == '?':
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------
#conditions [length, uppercase, lowercase, digits, special], score and input
length_score = 0

diversity_score = 0

bonus_score = 0

penalty = 0

digit_count = 0

special_count = 0

has_upper = False

has_lower = False

has_digits = False

has_Special = False

char_counts = {}

bad_sequences = []


password = str(input("Please enter your password: "))
#Check the password
for char in password:
    if char.isupper() == True:
        has_upper = True
        
    if char.islower() == True:
        has_lower = True
        
    if char.isdigit() == True:
        has_digits = True
        digit_count += 1
    if isspecial(char) == True:
        has_Special = True 
        special_count += 1

for char in password:
    if char in char_counts:
        char_counts[char] += 1 
    else:
        char_counts[char] = 1

for count in char_counts.values():
    if count > 0.4 * float(len(password)):
        penalty += 1

for i in range(1,len(password)):
    if password[i] == password[i-1] and password[i] == password[i-2]:
        penalty += 2


# Scoring
if has_upper == True:
    diversity_score += 1
if has_lower == True:
    diversity_score += 1
if has_digits == True:
    diversity_score += 1
if has_Special == True:
    diversity_score += 2
if len(password) < 8:
    penalty += 3
elif len(password) in range(8,11):
    length_score += 0
elif len(password) in range(11,14):
    length_score += 1
else:
    if len(password) > 20:
        bonus_score += 2
    length_score += 2
if has_upper and has_lower and has_digits and has_Special:
    bonus_score += 1


score = length_score + bonus_score + diversity_score - penalty
print(score)


#Output
#if score <= 3:
 #   print('Your password is very weak.')
#elif score in range(4,7):
 #   print('Your password is okay.')
#else:
  #  print('Your password is Strong!')