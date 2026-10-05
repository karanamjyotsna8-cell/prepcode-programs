blocked_list=["guest","test","admin"]
user_name=input("enter the username:")
if user_name not in blocked list:
    print("user name is allowed")
else:
    print("user name is not allowed")