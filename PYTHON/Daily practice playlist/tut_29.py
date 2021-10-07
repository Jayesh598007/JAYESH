# Seek(), tell() & More On Python Files

f = open("jayesh.txt")
print(f.tell())         # to tell(know) the file poiner location
print(f.readline())
print(f.tell())
print(f.seek(12))         # to position the file pointer at given space
print(f.readline())
print(f.tell())

f.close()