elements = input("input everything you want : ")
digits = ["1","2","3",'4','5','6','7',"8","9"]
answer = []

for item in elements:
    if item in digits:
        answer.append(item)

print(answer)