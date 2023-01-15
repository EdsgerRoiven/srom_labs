import time
A = 'D4D2110984907B5625309D956521BAB4157B8B1ECE04043249A3D379AC112E5B9AF44E721E148D88A942744CF56A06B92D28A0DB950FE4CED2B41A0BD38BCE7D0BE1055CF5DE38F2A588C2C9A79A75011058C320A7B661C6CE1C36C7D870758307E5D2CF07D9B6E8D529779B6B2910DD17B6766A7EFEE215A98CAC300F2827DB'
A = 'D4D'
N = '269D7722EA018F2AC35C5A3517AA06EAA1949059AE8240428BBFD0A8BE6E2EBF91223991F80D7413D6B2EB213E7122710EDEC617460FA0191F3901604619972018EBEF22D81AED9C56424014CADCC2CCDEE67D36A54BFC500230CA6693ABA057B374746622341ED6D52FE5A79E6860F54F197791B3FEF49FD534CB2C675B6BDB'
N = '269'
#A = '791EDB102DA183759979CEF70E1405AF14B98CD4'
#A = '170076B15F9575D21DE39D5C429799BBCDDB867016DE2248E3CFDE73A4D70C8636A9E41ABE671E7B9FB4739A5FF64DF9D0D3A64E0C9B20BFE58F1C62B28477EE9FD202010BAC440ADF3CA016A32DB844F23DEC2AB93AE869A6262FC23C5CE419807CDBA930A5433884E3B34B22477289BD3A7712CDD4B4110BD9887E7428FDF7'
B = '3A7EF2554E8940FA9B93B2A5E822CC7BB262F4A14159E4318CAE3ABF5AEB1022EC6D01DEFAB48B528868679D649B445A753684C13F6C3ADBAB059D635A2882090FC166EA9F0AAACD16A062149E4A0952F7FAAB14A0E9D3CB0BE9200DBD3B0342496421826919148E617AF1DB66978B1FCD28F8408506B79979CCBCC7F7E5FDE7'
B = '3A7'
#B = '3A7EF2554E8940FA9B93B2A5E822CC7BB262F4'
def int_transform(number):
    return [int(number[::-1][i:i+4][::-1],16) for i in range(0,len(number),4)][::-1]
def bin_to_int(number):
    return [int(i,2) for i in number]
def hex_transform(number):
    temp_number =  [hex(i).lstrip("0x").rstrip("L") for i in number]
    for i in range(0,len(temp_number)-1):
        while len(temp_number[i])<4:
            temp_number[i] = '0' + temp_number[i]
    return ''.join(i for i in temp_number[::-1])
    #return temp_number[::-1]

def len_equalizer(number_1,number_2):
    if len(number_1) == len(number_2):
        return number_1,number_2
    while len(number_1)>len(number_2):
        number_2 = number_2 + [0]
    while len(number_2) > len(number_1):
        number_1 = number_1 + [0]
    return number_1,number_2
def len_equalizerBin(number_1,number_2):
    if len(number_1) == len(number_2):
        return number_1,number_2
    while len(number_1)>len(number_2):
        number_2 = '0' + number_2
    while len(number_2) > len(number_1):
        number_1 = '0' + number_1
    return number_1,number_2
def LongAdd(A_,B_):
    carry = 0
    C_ = []
    A_,B_ = len_equalizer(A_,B_)
    for i in range(0,len(A_)):
        temp = A_[i] + B_[i] + carry
        C_.append(temp%int('10000',16))
        carry = temp//int('10000',16)
    C_ =  C_ + [carry]
    return hex_transform(C_)

def LongSub(A_,B_):
    borrow = 0
    C = []
    A_, B_ = len_equalizer(A_, B_)
    for i in range(0,len(A_)):
        temp = A_[i] - B_[i] - borrow
        if temp >= 0:
            C.append(temp)
            borrow = 0
        else:
            C.append(int('10000',16) + temp)
            borrow = 1
    return hex_transform(C)
def LongSubBin(A_,B_):
    borrow = 0
    C = []
    A_, B_ = len_equalizerBin(A_, B_)
    for i in range(0,len(A_)):
        temp = A_[i] - B_[i] - borrow
        if temp >= 0:
            C.append(temp)
            borrow = 0
        else:
            C.append(1 + temp)
            borrow = 1
    return hex_transform(C)
def LongCmp(A_,B_):
    #A_, B_ = len_equalizer(A_, B_)
    if len(A_)> len(B_):
        return 1
    elif len(B_) > len(A_):
        return -1
    else:
       #print(True)
        i = len(A_)-1
        #print(i,A_[i])
        while A_[i] == B_[i]:
            i-=1
            if i==-1:
                break
        if i == -1:
            return 0

        else:
            #print(True)
            #print(A_[i],B_[i])
            if A_[i]>B_[i]:
                return 1
            else:
                return -1
def LongCmpBin(A_,B_):
    #A_, B_ = len_equalizer(A_, B_)
    if len(A_)> len(B_):
        return 1
    elif len(B_) > len(A_):
        return -1
    else:
        i = len(A_)-1
        while A_[i] == B_[i]:
            i-=1
            if i == -1:
                break
        if i == -1:
            return 0

        else:
            if int(A_[i],2)>int(B_[i],2):
                return 1
            else:
                return -1
def LongMulOneDigit(A_,b):
    carry = 0
    C = []
    for i in range(0,len(A_)):
        temp = A_[i]*b + carry
        C.append(temp%int('10000',16))
        carry = temp // int('10000', 16)
    C.append(carry)
    return hex_transform(C)
def LongMul(A_,B_):
    C = [0]
    for i in range(0,len(B_)):
        temp = int_transform(LongMulOneDigit(A_,B_[i]))
        temp = temp + [0]*i
        C = int_transform(LongAdd(C[::-1],temp[::-1]))
    return hex_transform(C[::-1])
def Bin_converter(number):
    temp = [bin(i)[2:] for i in number]
    for i in range(0,len(temp)):
        if i!=0:
            while len(temp[i]) < 16:
                temp[i] = '0' + temp[i]
    return temp[::-1]
def BitLength(number):
    temp = number.copy()
    #for i in range(0,len(temp)):
    #    while len(temp[i]) < 16:
     #       temp[i] = '0' + temp[i]
    return len(''.join(i for i in temp))
def LongShiftBitToHigh(number,st):
    temp = ''.join(i for i in number)
    temp = temp + '0'*st
    return [temp[::-1][i:i+16][::-1] for i in range(0,len(temp),16)][::-1]
def LongDivMod(A_,B_):
    A_b = Bin_converter(A_)[::-1]
    B_b = Bin_converter(B_)[::-1]
    k = BitLength(B_b)
    R = A_b
    Q = 0
    j = 0
    while LongCmpBin(R[::-1],B_b[::-1]) in (0,1):
        t = BitLength(R)
        C = LongShiftBitToHigh(B_b,t-k)
        if LongCmpBin(R[::-1],C[::-1]) == -1:
            t -=1
            C = LongShiftBitToHigh(B_b,t-k)
        R = Bin_converter(int_transform(LongSub(bin_to_int(R)[::-1],bin_to_int(C)[::-1])))[::-1]
        if t-k>=0:
            Q += 2**(t-k)
        j+=1
    return hex_transform(bin_to_int(R[::-1])),hex(Q).lstrip("0x")
def Euclide(A_,B_):
    A_c = A_
    B_c = B_
    d = 1
    j = 0
    while LongDivMod(A_c,[2])[0] == '' and LongDivMod(B_c,[2])[0] == '':
        A_c =int_transform(LongDivMod(A_c, [2])[1])
        #print(hex_transform(int_transform(A_c)[::-1]),True)
        B_c = int_transform(LongDivMod(B_c, [2])[1])
        d = d*2
    while LongDivMod(A_c,[2])[0] == '':
        A_c = int_transform(LongDivMod(A_c, int_transform('2'))[1])
    while B_c!=[]:
        while LongDivMod(B_c,[2])[0] == '':
            B_c = int_transform(LongDivMod(B_c, [2])[1])
        print(A_c[::-1],B_c[::-1])
        if LongCmp(A_c[::-1],B_c[::-1]) in (0,1):
            #print(hex_transform(A_c[::-1]),hex_transform(B_c[::-1]))
            #print(''.join([hex(i)[2:] for i in A_c]))
            A_c,B_c = B_c, int_transform(LongSub(A_c[::-1],B_c[::-1]))
            #print(hex_transform(A_c[::-1]),hex_transform(B_c[::-1]))
           # print('part1')
            print(len(A_c),len(B_c))
        else:
            #print(A_c, B_c)
            A_c,B_c = A_c,int_transform(LongSub(B_c[::-1],A_c[::-1]))
            #print(A_c,B_c)
            #print('part2')
            print(len(A_c),len(B_c))
        print(A_c,B_c)
    print(d,A_c)
    d = LongMul(A_c,[d])
    return d
def KillLastDigits(x,k):
    return x[:-k]
def BarrettReduction(x,n):
    if LongCmp(n[::-1],x[::-1]) == 1:
        return hex_transform(x)
    else:
        nu = int_transform(LongDivMod([int('10000',16)] + [0]*(len(n)-1),n)[1])
        k = int(len(x)/2)
        q = KillLastDigits(x,k-1)
        q = int_transform(LongMul(q[::-1],nu[::-1]))
        q = KillLastDigits(q, k + 1)
        if q == []:
            q = [1]
        #return null
        r = int_transform(LongSub(x[::-1],int_transform(LongMul(q[::-1],n[::-1]))[::-1]))
        while LongCmp(r[::-1],n[::-1]) == 1:
            r = int_transform(LongSub(r[::-1],n[::-1]))
            print(len(r),len(n))
        return hex_transform(r[::-1])
def LongAddMod(A,B,N):
    sum = LongAdd(int_transform(A)[::-1],int_transform(B)[::-1])
    #print(sum[:-1])
    return BarrettReduction(int_transform(sum),int_transform(N))
def LongSubMod(A,B,N):
    sub = LongSub(int_transform(A)[::-1],int_transform(B)[::-1])
    #print(sum[:-1])
    return BarrettReduction(int_transform(sub),int_transform(N))
def LongMulMod(A,B,N):
    mul = LongMul(int_transform(A)[::-1],int_transform(B)[::-1])
    #print(sum[:-1])
    print(mul)
    return BarrettReduction(int_transform(mul),int_transform(N))
#print(KillLastDigits(int_transform(A),15))
#print(LongAddMod(A,B,N))
#print(LongSubMod(A,B,N))
#print(LongDivModMod(A,B,N))
print(LongMulMod(A,B,N))
#print(BarrettReduction(int_transform(B),int_transform(N)))
#print(LongDivMod(int_transform(A),int_transform(B)))
#print(LongDivMod(int_transform(A),int_transform(B))[0])
#print(Euclide(int_transform(A),int_transform(B)))
