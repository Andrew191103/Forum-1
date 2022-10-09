First = int(input("Input a positive integer please: "))
Second = int(input("Input a positive integer please: "))
LCM = Second
bro = True
while bro:
    if LCM % First == 0 and LCM % Second == 0:
        print(LCM)
        bro = False
    LCM += 1