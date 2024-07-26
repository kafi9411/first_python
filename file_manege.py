        #    file create code 
"""open("demofile.txt", 'x')  """
        # file write code
""" ver = open('demofile.txt', 'w')
ver.writelines('Iam MD Abdul Kafi.')
ver.close() """
        # add or line  code 
""" ver = open('demofile.txt', 'a')
ver.writelines(' Iam new Developer. ')
ver.close() """
        #Read 'r' code
ver = open('demofile.txt','r')
print(ver.read())
ver.close




        # Read 'r' ar for loop code d
# ver = open('demofile.txt', 'r')
# count = 0
# for i in ver.read():
#     print(i, end='')
#     count += 1
# ver.close()
# print(count)