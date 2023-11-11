print("ax^2+bx+c = 0")
a = int(input("input a"))
b = int(input("input b"))
c = int(input("input c"))

print(f"{a}x**2+{b}x+{c}=0")

D = (b**2) - (4 * a * c)
print("discriminant :",D)
if D > 0:
    x1 = (-1 * b) - (D ** (1/2))
    x2 = (-1 * b) + (D ** (1/2))
    print("answers : x1 = {answer1}, {answer2}".format(answer1 = x1,answer2 = x2))
elif D == 0:
    x = (-1 * b) - (D ** (1/2))
    print("D = 0. One answer : ",x)
else:
    print("D < 0", D)