food = 0
power = 0
brain = 0
a1 = input("do you know how to cook? (yes/no): ")
if a1 == "yes":
    food = food + 2
else:
    power = power + 1
a2 = input("are you strong? (yes/no): ")
if a2 == "yes":
    power = power + 2
else:
    brain = brain + 1
a3 = input("are you good at solving problems? (yes/no): ")
if a3 == "yes":
    brain = brain + 2
else:
    food = food + 1
a4 = input("can you run fast and stay calm? (yes/no): ")
if a4 == "yes" and power > 0:
    power = power + 2
else:
    brain = brain + 1
a5 = input("do you like learning or trying new stuff? (yes/no): ")
if a5 == "yes" or brain > 1:
    brain = brain + 2
else:
    food = food + 1

print("scores:", food, power, brain)

if food > power and food > brain:
    print("you survive by finding food")
elif power > food and power > brain:
    print("you survive with strength")
elif brain > food and brain > power:
    print("you survive by being smart")
else:
    print("you are balanced")