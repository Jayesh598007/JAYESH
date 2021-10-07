def sum (*a):
    result = 0
    for i in a:
        result = result +i
    return result

res = sum( 2, 5, 6, 6, 2, 3)
print(res)