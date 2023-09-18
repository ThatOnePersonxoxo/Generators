# Character Generator, a project made by ThatOnePersonXoxo
# Can generate character looks and names
# This is pretty useful for writing books
# Note : This generator is only for humans

import random

hairColor = ['white', 'blonde', 'gray', 'balayage', 'burgundy', 'brown', 'black', 'auburn', 'brunette']
skinTone = ['fair', 'light', 'medium', 'deep']
eyeColor = ['green', 'blue', 'red', 'yellow', 'white', 'brown']
personality = ['Carefree', 'Dark', 'Flirty', 'Mean', 'Ambitious', 'Happy']

RndHair = random.choice(hairColor)
RndSkin = random.choice(skinTone)
RndEye = random.choice(eyeColor)
RndPersona = random.choice(personality)

print('Your character has', RndHair, 'hair')
print('Your character has', RndSkin, 'skin')
print('Your character has', RndEye, 'eyes')
print('Your character is', RndPersona)