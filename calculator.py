def add (num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multyply(num1,num2):
    return num1*num2

def divide (num1,num2):
    return num1/num2

def power (num1, num2):
    return num1**num2

def remainder (num1, num2):
    return num1%num2

def getwholenumber (num1, num2):
    return num1//num2
operation = input('select one of the operations:\n1- Addition     2 - subtraction\n3 - Division    4 - Multiplication\n5 - Exponential     6 - Get remainder\n7 - Get whole umber   8 - QUIT')\

List_operations = ['1','2','3','4','5','6','7','8']

while operation != '8':
    if operation in List_operations:
        num1 = int(input('Enter the first number:'))
        num2 = int(input('Enter the second number:'))
        if operation == '1':
            answer = add(num1,num2)
        elif operation  == '2':
            answer = subtract(num1, num2)
        elif operation  == '3':
            answer = multyply(num1, num2)
        elif operation  == '4':
            answer = divide(num1, num2)
        elif operation  == '5':
            answer = power(num1, num2)
        elif operation  == '6':
            answer = remainder(num1, num2)
        elif operation  == '7':
            answer = getwholenumber(num1, num2)
        print('Answer is:',answer)

    else:
        print('We could not find an operation matching your request, Please Try Again...!\n\n')
    operation = input('select one of the operations:\n1- Addition     2 - sutraction\n3 - Division    4 - Multiplication\n5 - Exponential     6 - Get remainder\n7 - Get whole umber   8 - QUIT')\

