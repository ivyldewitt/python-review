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
    'defeated_by': {
        'paper',
        'scissors'
    },
    'defeats': {
        'scissors',
        'plastic'
    }
}

print(dictionary['bob'])
dictionary['bob'] += 1
print(dictionary['bob'])
print(dictionary)
dictionary['ivy'] = 2
print(dictionary)
print(f"You are defeated by {dictionary['defeated_by']}.")
print(dictionary.get('other', 42))

#Alternative way to create a dictionary

d = dict()

d_two = dict(bill=2, zoe=7, michael=10)

name = 'zoe'

print(f"Wins by {name} are {d_two[name]}.")