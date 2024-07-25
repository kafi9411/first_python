user_account = [
    {
        "name": "kafi",
        "phone": "01768893384",
        "address": "IslamNagar, Thakurgaon.",
        "password": "1234"
    },
]

def check_unique(phone):
    for user in user_account:
        if user['phone'] != phone:
            return True
            
    return False


def check_available(name, phone, address, password):
    if name:
        if phone:
            if address:
                if password:
                    return True
                else:
                    return f'Password field is required.'
            else:
                return f'Address field is required.'
        else:
            return f'Phone field is required.'
        
    else:
        return f'Name field is required.'
        

phone = input("Enter your phone: ")

if check_unique(phone):
    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    
    result = check_available(name, phone, address, password)
    if result == True:
        user = {
            "name": name,
            "phone": phone,
            "address": address,
            "password": password
        }
        
        user_account.append(user)
        print(user_account)
    else:
        print(result)

else:
    print('This phone number is already exists.')