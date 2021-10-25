

for i in range(2, 21):   # multi tables files of 2 to 20
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:  # multi tables names as per given
        for j in range(1, 11):   # multi tables of '2 to 20' X '1 to 10'
            f.write(f"{i} X {j} = {i*j}\n")  # multi tables from 2 to 20 in this given form
            
print("done") # thus multiplication tables ar created in (tables-folder)

