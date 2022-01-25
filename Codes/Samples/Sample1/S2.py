# # # fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana’]
# # # # fruits.count('apple’)
# # # print("Apples in list: ",fruits.count('apple’))
# # # x =input("Please add another value to the list: ")
# # # fruits.append(x)

# # # A program to get 5 numbers and return the maximum
# # """
# # Steps:
# #     Take number
# #     Check if it's int or not
# #     if it's int: Append or add to the list
# #     if not:      take another
# #     Repeat until it's 5 numbers in list
# # """

# # numList =[] #List of input numbers

# # while(len(numList) <=4):
# #     try:
# #         num = int(input("Please enter your desired number:"))

# #         if (type(num) == int):
# #             numList.append(num)
# #     except:
# #         print("Please enter a valid number.")

# # print(numList)


# def myFunction(fname ='Akin', lname ='Yildiz'):
#     print(fname + ' ' +lname )

# myFunction('Sarah')

# mySum(a, my_function(3))

def openFunc(filename):
    # Open a file
    fo = open(filename, "wb")
    print ("Name of the file: ", fo.name)
    print ("Closed or not : ", fo.closed)
    print ("Opening mode : ", fo.mode)
    # Close opend file
    fo.close()

openFunc("fos.txt")


def writeFunc(filename, data):
    # Open a file 
    fo = open(filename, "wb")
    fo.write(data+"\n")
    # Close opend file
    fo.close() 


def readFunc(filename):
    contents =''
    # Open a file
    fo = open(filename, "r+") 
    #10 is the number of bytes to be read from the opened file.
    #Without the count number, it’ll load form first to last(how much it can) of file.
    contents = fo.read(10)
    # Close opend file 
    fo.close() 
    return contents

