data = {"1": 23.3, 2: 34}

array = [{"1": 23.3, 2: 34}, {"1": 23.3,
    2: 34}]

d1 = data.items()
d2 = data[2]
d3 = data.update({1: 10, 4: "Hello"})
print(d1)

print('Array', array)

print("Array pushing :", array.append({"12": 34}))

print("Array after adding :", array)