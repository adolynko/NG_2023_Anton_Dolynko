elements = input("input everything you want : ").split()

array = []

for element in elements:
    try:
        int(element)
        array.append(element)
    except:
        pass
        

print(array)