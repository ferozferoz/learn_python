if __name__== "__main__":
    #input simply take input from keyboard and print to output screen
    ##name = input("what is your name \n")
    #print("My name is "+name)
    #number = input ("enter the number to be operated \n")
    #number2  = int(number) + 15
    #print(number2)
    # width and precision defined together
    print('%.5f %s cost $%8.2f' % (6, 'bananas', 0931.749))

    file_pointer = open('../test.txt',"w");
    file_pointer.write("hello")
    for i in range(10):
        file_pointer.write(str(i)+'\n')
    file_pointer.close()

    file_pointer = open('../test.txt', "r");
    str = file_pointer.read(10)
    print(str)

