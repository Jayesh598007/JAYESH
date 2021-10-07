subscribers = int(input("Enter your Subscribers: "))
likes = int(input("Enter your Likes: "))
comments = int(input("Enter your Comments: "))

# for any conditions to be fulfilled

# can be also written as
'''
if(subs>50 or likes>59 or comment>40):
    print("Awesome video")
'''

conditions= {
    subscribers>150,
    likes>150, 
    comments>50
}
 
if any(conditions):
    print('This is an Awesome video')
else:
    print("You dont have enough subscribers")

    
