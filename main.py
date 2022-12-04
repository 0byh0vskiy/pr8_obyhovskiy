import random

def password():
    one = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    two = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    otvet = ''
    for i in range(11):
        otvet += random.choice(one + two)
    return otvet


passw = password()
print(passw)
