# Random password generator


import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '()[]{};:_-#@.'
number = '0123456789'

all = lower + upper + symbol + number
length = 12
password = "".join(random.sample(all,length))
print("The Generated password is: ", password)