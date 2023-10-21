temperature = input("Choose Celsius or fahrenheit : ").lower()
degrees = int(input("input degrees : "))
if temperature == "celsius":
    print(degrees * (9/5) + 32)
elif temperature == "fahrenheit":
    print((degrees - 32)* 5/9)
else:
    print("isn`t celsius or fahrenheit")