sub1 = int(input("Enter your Marks:"))
sub2 = int(input("Enter your Marks:"))
sub3 = int(input("Enter your Marks:"))

if(sub1<33 or sub2<33 or sub3<33):
    print(" You are fail")
if((sub1+sub2+sub3)/3) <40:
    print(" You are fail")
else:
    print(" Congratulations: You are pass")
    
