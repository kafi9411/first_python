# open('word.txt','x')

# x = open('word.txt', 'w')
# x.write('Iam Md Abdul Kafi')
# x.close()

# x = open('word.txt', 'r')
# print(x.read())
# x.close

x = open('word.txt', 'r')
count = 0
for i in x.read():
    # count += 1
    if x == ' ':
        continue
    count += 1
x.close()

print(count)