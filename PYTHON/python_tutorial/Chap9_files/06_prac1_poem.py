f = open("poem.txt")  # to check whether 'twinkle' is present or not in the (poem.txt)
t = f.read()
if "twinkle" in t:    
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()