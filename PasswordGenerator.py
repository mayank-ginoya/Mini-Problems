import random
import array
from unicodedata import digit

from numpy import tensordot

MIN_LEN = 8
MAX_LEN = 12

digits = '0 1 2 3 4 5 6 7 8 9'.split()
lowerAlp = 'a b c d e f g h i j k l m n o p q r s t u v w z y z'.split()
upperAlp = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
symbols = '@ # $ % = : ? . / | ~ > * ( ) <'.split()

overall = digits + lowerAlp + upperAlp + symbols

dig = random.choice(digits)
lwr_Alp = random.choice(lowerAlp)
upr_Alp = random.choice(upperAlp)
sym = random.choice(symbols)
pass_required = int(input("Enter Number of Passwords Required :- "))
for pwd in range(pass_required):
    temp_password = dig + lwr_Alp + upr_Alp + sym
    # MAX_LEN = int(input("Enter Length of Password you Required(Default = 12)"))
    for text in range(MAX_LEN-4):
        temp_password += random.choice(overall)
        temp_password = list(temp_password)
        random.shuffle(temp_password)
        temp = ''.join(temp_password)
        # random.shuffle(temp_password)

    password = temp
    print(f'Password {pwd} : {password}')