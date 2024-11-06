# 

from random import randint
correct = randint(16,64)
number = None
while number != correct:

    print("Guess my number!!!")
    number = int(input())
    if number > correct:
        print("LOWER")
    if number < correct:
        print("HIGHER")
    if number == correct:
        print("YOU WON WOOOHOO")


five_less = correct - 5 gv
five_more = correct + 5
print("ALMOST WITHIN 5")