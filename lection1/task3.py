temperature = input("Type 1)Celsius or 2)Fahrenheit : ")
degrees = int(input("input degrees : "))
if temperature == 1:
    print(degrees * (9/5) + 32)
elif temperature == 2:
    print((degrees - 32)* 5/9)
else:
    print("isn`t celsius or fahrenheit")