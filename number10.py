Characters = ["Makunouchi", "Zangief", "Takeshi", "Ricardo"]
name = input("Enter a character's name: ")
name = name.capitalize()
if name in Characters:
    print("It's inside")
else:
    print("It's not")