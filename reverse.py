def create_dictionary():
    a = int(input("Input the number of dictionary elements: "))
    dictionary = {}
    for i in range(a):
        b = ("Input the name of the "+ str(i+1) + " key: ")
        c = ("Input the name of the " + str(i+1) + " value: ")
        key = input(b)
        value = input(c)
        try:
            key = float(key)
            value = float(value)
        except:
            pass
        dictionary.__setitem__(key, value)
    return dictionary

def reverseLookup(dictionary, value):
    a = []
    for i, j in dictionary.items():
        if j == value:
            a.append(i)
    return a

dictionary_1 = ({"a": 1, "b": 1, "c": 2})
dictionary_2 = ({"a": 99, "b": 1, "c": 2})
dictionary_3 = ({"a": 1, "b": 1, "c": 2})
dictionary_4 = create_dictionary()

print("Creating own dictionary: ", reverseLookup(dictionary_4, input("What do you want to find: ")))
print("More than one answers: ", reverseLookup(dictionary_1, 1))
print("One answer: ", reverseLookup(dictionary_2, 1))
print("No answer: ", reverseLookup(dictionary_3, 4))