import random

def password():
    one = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    otvet = ''
    for i in range(11):
        otvet += random.choice(one)
    return otvet


passw = password()
print(passw)
