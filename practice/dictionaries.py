###
# d = create d using core concepts above.

# print(d["Sam"])          # outputs 7
# print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
# print(d.get('Sarah'))    # outputs None
# print(d.get('Jeff', -1)) # outputs -1
# print(d['done'])         # outputs True


dictionary_test = {
    'Sam': 7,
    'rolls': {
        'rock', 
        'paper',
        'scissors'
    },
    'done': True,
}

print(dictionary_test.get('Jeff', -1))
print(dictionary_test.get('Sarah'))
print(dictionary_test['Sam'])
print(dictionary_test['rolls'])
print(dictionary_test['done'])