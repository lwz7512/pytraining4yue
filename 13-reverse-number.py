# reverse a number:
# for example:
# 123456789  --> 987654321

num = 123456789
rev = 0
while num > 0 :
    Rem = num % 10
    print("Rem: ", Rem)
    num = num // 10
    print("num: ", num)
    rev = rev * 10 + Rem
    print("rev: ", rev)
print("The Reverse of the number: ", rev)

