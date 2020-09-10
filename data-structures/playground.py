# Data Structures
# 1. Dictionaries
# 2. Lists / Arrays 
# 3. Sets

lst = [4, 1, 1, 33, 1, 63]
print(lst)
lst.append(15)
print(lst)
lst.remove(1)
print(lst)
lst.sort()
print(lst)

#Collection of distinct items

ste = {4, 33, 1, 63}
print(ste)
ste.add(1)
ste.add(63)
print(ste)

# Dictionaries – key-value pairs

dictionary = {
    'bob': 0,
    'sarah': 0,
}

print(dictionary['bob'])
dictionary['bob'] += 1
print(dictionary['bob'])
print(dictionary)
dictionary['ivy'] = 2
print(dictionary)