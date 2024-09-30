'''print("01234567890123456")
print("{0:^7}{1:4}{2:>6s}".format("one", "two", "three"))
print(f"{'one':^7}{'two':4}{'three':>6s}")'''

print("Python")
print("Python"[0])
print("Python"[-1])
print("Python"[:])

str = "Python 123"
print(str)
print(str[0])
print(str[-1])
print(str[:])

strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
print(strNum[1], strNum[-1], len(strNum))
print(strNum[:len(strNum)])
print(strNum[1]+strNum[-3])

n = [22,574,3.14,99.99,-95,77,48]
avg = sum(n)/len(n)
print(f'{min(n)}\n{max(n)}\n{sum(n)}\n{avg:.3f}')
