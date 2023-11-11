fileName = input("input file name: ")

with open(fileName, 'r') as file:
    content = file.read()
    symbolCount = {}
    for symbol in content:
        symbolCount[symbol] = symbolCount.get(symbol, 0) + 1
    for symbol, count in symbolCount.items():
        print(f"'{symbol}': {count}")



