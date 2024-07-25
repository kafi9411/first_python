
                # Multipol Arument sum funtion

def sum(*x):
    sum = 0
    for i in x:
        sum += i
    print(sum)
sum(5, 5, 5, 12, 5, 90, 3 )


      



            # value type and dict type value sum funtion


def sum(**x):
    sum = 0
    for i in x.values():   
        sum += i
    print(sum)
sum(num1 = 4, num2 = 6)
                        # .values() is a method
                        # dict key ar value ba mane nawar jonno .values() method use kore hoi