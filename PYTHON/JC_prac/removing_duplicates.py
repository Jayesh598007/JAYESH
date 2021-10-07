a= [1, 5, 8, 5, 8, 3, 6, 9, 2, 5, 8, 4, 9, 2, 0, 3, 6, 5, 7, 0]
print(a)
# long method
'''
a= set(a)
a= list(a)
'''

a= list(set(a))
print(a)