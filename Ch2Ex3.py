name, word=input("Enter your name and char by comma separate:").split(",")
#x=word.lower()
print("Lengh of the name is:",(len(name)))
#print(f"No. of times {name} is their:",x.count(x))
print(f"No. of times {word} is their:{name.lower().count(word.lower())}")