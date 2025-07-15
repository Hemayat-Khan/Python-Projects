#---------Traffic Light----------#
for i in range(4):
    light = input("Enter your color: ").strip().capitalize()

    if light == "Green":
        print("You can go")
    elif light == "Yellow":
        print("You should turn on the key")
    elif light == "Red":
        print("You can stop")
    else:
        print("Invalid color entered")
