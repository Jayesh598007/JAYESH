subscribers = int(input("Enter your Subscribers: "))
likes = int(input("Enter your Likes: "))
comments = int(input("Enter your Comments: "))


# for all conditions to be fulfilled

# can e also written as
'''
if(subs>50 and likes>59 and comment>40):
    print("Awesome video")
'''

conditions= {
    subscribers>150,
    likes>150, 
    comments>50
}

if all(conditions):
    print('This is an Awesome video')
else:
    print("You dont have enough subscribers")


    
