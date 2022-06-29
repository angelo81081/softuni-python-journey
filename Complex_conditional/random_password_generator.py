import random

lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "0987654321"
symbols =".?!,/:;|\@%^&*"

all_combinations = lower + upper + numbers + symbols
lenght = 8

password = ''.join(random.sample(all_combinations, lenght))
print(password)