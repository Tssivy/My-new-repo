from random import choice as ch
with open('test.txt') as file:
    txt = [c.strip('\n') for c in file.read().split('\n\n') if c]
print(txt)