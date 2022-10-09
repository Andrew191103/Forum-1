x1,y1 = (input("Enter the first coordinate(add a space between x and y):")).split()
x2,y2 = (input("Enter the second coordiante(add a space between x and y):")).split()

xmid = (int(x2)+int(x1))//2
ymid = (int(y2)+int(y1))//2
mid = xmid,ymid

print("The midpoint of the line is:",mid)


