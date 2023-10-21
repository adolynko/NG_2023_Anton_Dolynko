firstNumber = int(input("input first number : "))
secondNumber = int(input("input second number : "))
sign = input("(+, -, *, /, sqrt, pow) : ")
try:
    match sign:
        case("+"):
            print("Result",firstNumber + secondNumber)    
        case("-"):
            print("Result",firstNumber - secondNumber)        
        case("*"):
            print("Result",firstNumber * secondNumber)        
        case("/"):
           print("Result",firstNumber / secondNumber)                       
        case("sqrt"):
            print("Result",firstNumber ** (1/secondNumber))
        case("pow"):
            print("Result",firstNumber ** secondNumber)
except Exception as e:
    print(e)