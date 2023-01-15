import random
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
def umnojenie(a,b,n):
    c = '0'
    a = standartization(a)
    b = standartization(b)
    for i in range(len(b)-1,-1,-1):
        if b[i] == '1':
            c = summa(c,bin(int(a,2)<<len(b)-i-1)[2:])
        if b[i] == '0' and int(b,2) == 0:
            b = '0'*(len(b)+i)
    c = mod(c,n)
    return c
#def LongCMP(a,b):
#    if len(a)>len(b):
#        return a
 #   elif len(a)<len(b):
 #       return b
#    else:
 #       for i in range(0,len(a)):
 #           if int(a[i],2) > int(b[i],2):
 #               return a
   #         elif int(a[i],2) < int(b[i],2):
  #              return b
     #   return a
def LongCMP(a,b):
    if int(a,2)>int(b,2):
        return a
    elif int(a,2)<int(b,2):
        return b
def Ranzniza(a,b):
    c = ''
    a = a[::-1]
    b = b[::-1]
    for i in range(0,len(b)):
        if a[i] =='1' and b[i] == '0' or (a[i] == '0' and b[i] == '1' and i!=(len(b)-1)):
            #c = c + str(int(a[i],2)&int(b[i],2))
            c = c + "1"
        else:
            c = c + '0'
    c = c + a[len(b):]
    c = c[::-1]
    return c
def standartization(a):
    kul = 0
    for i in a:
        if i =='0':
            kul+=1
        else:
            break
    if int(a,2) != 0:
        return a[kul:]
    else:
        return '0'
def mod(a,b):
    k = len(b)
    R = a
    Q = '0'
    if len(a)<len(b):
        return a
    #else:
    #    b = '0'*(len(a)-len(b)) + b
    while LongCMP(R,b)==R or R==b:
        #print(R,b,LongCMP(R,b),'сравнение')
        t = len(R)
        #print(int(b,2)<<(t-k),t,k)
        C = bin(int(b,2)<<(t-k))[2:]
        #print(C)
        if LongCMP(R,C) == C:
            t = t-1
            C = bin(int(b, 2) << (t - k))[2:]
        print(R,C)
        R = Ranzniza(R,C)
        R = standartization(R)
    return R
def randomizer(n):
    a = ''
    for i in range(0,n):
        a +=str(random.randint(0,1))
    return a
def stepenb(a,b,n):
    C = '1'
    for i in range(0,len(b)):
        if b[i] == '1':
            print(C,a)
            C = umnojenie(C,a,n)
            print(C)
        a = umnojenie(a,a,n)
    return C
chill1 = randomizer(150)
chill2 = randomizer(40)
a = '111' + '0'*12 + '1' + '0'*223+'1'
a = a[::-1]
print(stepenb(chill1,chill2[::-1],a))
print(chill1,chill2)

