a = input("Enter the text:\n")   # text will be provided by user

if("make a lot of money" in a):  # spam text
    spam = True
elif("buy now" or "buy this" in a):  # spam text
    spam = True
elif("click this" or "click below link" in a):  # spam text
    spam = True
elif("subscribe this" or "order this" in a):  # spam text
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")  # if the input text is provided by user has above spam text, it will flash this message
else:
    print("this text is not spam")  # if not spam, it will flash this message


