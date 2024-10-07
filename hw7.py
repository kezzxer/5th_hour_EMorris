#Name:ethan morris
#class: 5th hour
#Assignment: hw7

print("hello world")

wifi = True
login = True
admin = True

admincount = 5

if wifi:
    if login:
        if admin:
            print("welcome")
            admincount += 1
            print(admincount)
        else:
            print("missing admin cred")
    else:
        print("invalid login")
else:
    print("no wifi")

