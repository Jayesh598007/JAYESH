letter = '''Dear <|Name|>,
Greetings from ABC Company. We reeived your Resume.
You are selected, pls join us from the below given date

Thanks and Regards
Jayesh Chaudhari
8380884059
Date: <|Date|>
'''

Name = input("Enter your Name:\n")
Date = input("Enter Date\n")
letter = letter.replace("<|Name|>" , Name)
letter = letter.replace("<|Date|>" , Date) 
print(letter)

# this program is to replace the given data in the place and show it in a modified form
