info = [
    {
        "user_name" : "Kafi",
        "user_address" : "Thakurgaon",
        "user_work" : "Student",
        "user_user" : "kafi123",
        "user_pass" : "1234"

    },
    {
        "user_name" : "Al amin",
        "user_address" : "Thakurgaon",
        "user_work" : "Student",
        "user_user" : "alamin123",
        "user_pass" : "1234"

    },
    {
        "user_name" : "Rashed",
        "user_address" : "Thakurgaon",
        "user_work" : "Student",
        "user_user" : "rashed123",
        "user_pass" : "1234"

    },


]



name = input('Input your name ')
address = input('Input your address ')
work = input('Input your work ')
user = input('Input your user ')
password = input('Input your password ')


new = {"user_name":name, 'user_address' : address, "user_work" : work, "user_user" : user, "user_pass" : password }

info.append(new)
print(info)