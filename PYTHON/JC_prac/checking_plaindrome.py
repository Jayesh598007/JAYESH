name1 = 'madam'
name2 = 'madame'

# Plaindrome are words which reads same when reversing it
# wow, nayan, madam, pop, etc

# this program is to check whether a word is a plaindrome or not

isPlaindrome1 = name1.find(name1[::-1])==0
isPlaindrome2 = name2.find(name2[::-1])==0
print(isPlaindrome1)
print(isPlaindrome2)
