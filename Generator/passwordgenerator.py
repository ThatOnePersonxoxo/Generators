passwordgenerator
import random

Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Symbols = ['#', '%', '$', '_', '-', '*', '^', '&']
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

c1 = random.choice(seq=Letters)
c2 = random.choice(seq=Numbers)
c3 = random.choice(seq=Symbols)
c4 = random.choice(seq=Symbols)
c5 = random.choice(seq=Letters)
c6 = random.choice(seq=Letters)
c7 = random.choice(seq=Numbers)
c8 = random.choice(seq=Symbols)
c9 = random.choice(seq=Numbers)
c10 = random.choice(seq=Symbols)
c11 = random.choice(seq=Numbers)
c12 = random.choice(seq=Letters)

password = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12

print('Your very random password is: ', password)