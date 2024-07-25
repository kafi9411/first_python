students = {
    "user1":{ 
        "user_name": "kafi9411",
        "number": "55353"
        },
    "user2":{ 
        "user_name": "jisad55353",
        "number": "9411"
        },     
}
sin_up = input("inter your user or number ")

if students['user1']["user_name"] == sin_up or students['user1']["number"] == sin_up :
    print("login successfully")
else:
    print("Invalid user")