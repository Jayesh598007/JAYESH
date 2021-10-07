
subs = 2400
likes = 450

print(subs, likes)

#old method
'''
temp = subs  # transfer
subs = likes  # transfer
likes = temp   #transfer
print(subs , likes)
'''

subs, likes = likes, subs
print(subs, likes)


