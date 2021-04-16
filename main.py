speed = int(input("What was your average speed in km/h: "))
allowed = int(input("What was the allowed speed in km/h: "))
demirit_new = int((speed - allowed)//5)


if speed < allowed:
    print("OK")
else: 
    var = speed > allowed
    print("Points: " + str(demirit_new))
    if demirit_new >= 12:
        print("Your going to jail!")










