
def seperator():
    print("-" * 50 )
    print("inside")

def print_menu():
    seperator()
    print('Welcome to Python')
    seperator()
    print('[1] -Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    if(opc == 'x'):
        break 

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == '1'):
        res = sum(num1, num2)
        print("Result: " + str(res))
    elif(opc =='2'):
        res = sub(num1, num2)
        print("Result: " + str(res))
    elif(opc =='3'):
        res = mul(num1, num2)
        print("Result: " + str(res))
    

    input("Press enter to continue...")

print("Byte byte!")

