import random
import numpy as np
m = 239
temp_ = [['0']*m]*m
lambda_ = []
temp_2 = []
for i in range(0,len(temp_)):
    for j in range(0,len(temp_[i])):
        if ((2**i + 2**j)%(2*m + 1) == 1) or ((2**i - 2**j)%(2*m + 1) == 1) or ((2**j - 2**i)%(2*m + 1) == 1) or (((2**i + 2**j)*(-1))%(2*m + 1) ==1):
            temp_2.append(1)
        else:
            temp_2.append(0)
    lambda_.append(temp_2)
    temp_2 = []
def randomizer(n):
    a = ''
    for i in range(0,n):
        a +=str(random.randint(0,1))
    return a
def summa(a,b):
    c = ''
    a = a[::-1]
    b = b[::-1]
    if len(a)<len(b):
        a,b = b,a
    for i in range(0,len(b)):
        c = c + str(int(a[i],2)^int(b[i],2))
    c = c + a[len(b):]
    c = c[::-1]
    return c
def mult(a,b):
    a_copy = [int(i) for i in a]
    b_copy = [int(i) for i in b]
    lambda_copy = np.array(lambda_)
    z = []
    for i in range(0,len(a)):
        a_int = np.array(a_copy[i:] + a_copy[:i])
        b_int = np.array(b_copy[i:] + b_copy[:i]).transpose()
        z.append(str(a_int.dot(lambda_copy).dot(b_int)%2))
    return z
def stepenb(a,n):
    t = int(n,2)
    a_copy = [int(i) for i in a]
    b_copy = [int(i) for i in a]
    z = mult(a_copy,b_copy)
    while t-2>0:
        z = [int(i) for i in z]
        z = mult(a_copy, z)
        t-=1
    return z
chill1 = randomizer(m)
chill2 = randomizer(m)
a = '111' + '0'*12 + '1' + '0'*223+'1'
a = a[::-1]
print(chill1)
print(''.join([i for i in stepenb(chill1,'101')]))
#print(int('10',2),int('11',2))
#print(''.join([i for i in mult(chill1,chill1)]))
#print(chill1,chill2)
#print(''.join([i for i in mult(chill1,chill2)]))
#print(summa(chill1,chill2))
#print(chill1,chill2)
'1101001110000100001010010011111011100'