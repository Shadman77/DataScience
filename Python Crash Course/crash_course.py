def incrementIter():
    incrementIter.i += 1
    print(str(incrementIter.i) + ' -------- look below')


incrementIter.i = 0


# 1.exponents
incrementIter()
print('7 to the power 4 is ' + str(7 ** 4))

# 2.split a string into a list
incrementIter()
s = 'Hello there Anonno!'
print(s.split())

# 3.using .format
incrementIter()
planet = 'Earth'
diameter = 12742
print('The diameter of {} is {} kilometers'.format(planet, diameter))
print('The diameter of {a} is {b} kilometers'.format(a=planet, b=diameter))

# 4.get domain
incrementIter()


def getDomain(email):
    return email.split('@')[1]


print(getDomain('user@domain.com'))

# 5.find keyword case insensitive
incrementIter()


def findInString(s):
    return 'dog' in s.lower().split()


print(findInString('The Dog jumps over the quick brown fox.'))

# 6. find number of dogs in the string
incrementIter()


def countOccurances(s):
    count = 0
    for word in s.lower().split():
        if word == 'dog':
            count += 1
    return count


print(countOccurances('There are three dogs, dog dog dog'))

# 7. filter out words starting with s using a lambda function
incrementIter()
seq = ['dog', 'salad', 'soup', 'cat']
print(list(filter(lambda word: word[0] == 's', seq)))
