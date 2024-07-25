def length(x):
    count = 0
    for i in x:
        count += 1
    return count 
string = input('Input your string type data ')
result = length(string)
print("Your string's length", result)