def xor(a,b):
    'a,b are hex'
    return hex(int(a,16)^int(b,16))[2:]

def str_to_hex(a):
    res = ''
    for i in range(len(a)):
        res = res+hex(ord(a[i]))[2:]
    return res

# k,c都是16进制字符串     
def xor_D(k,c):
    m = []
    len_k = len(k)
    x = 0
    for i in range(0,len(c),2):
        ci = c[i:i+2]
        ki = k[x:x+2]
        mi = int(ci,16)^int(ki,16)
        x = (x+2)%len_k
        m.append(chr(mi))
    return ''.join(m)

# k,m都是16进制字符串     
def xor_E(k,m):
    c = []
    len_k = len(k)
    x = 0
    for i in range(0,len(m),2):
        mi = m[i:i+2]
        ki = k[x:x+2]
        ci = int(mi,16)^int(ki,16)
        x = (x+2)%len_k
        a= hex(ci)[2:]
        if len(a)<2:    #补0
            a = '0'+a
        c.append(a)       #去掉0x
    return ''.join(c)

def xor_find(c):
    key = []
    res = []
    for i in range(0xff+1):
        m = xor_D(hex(i)[2:],c)
        for j in range(len(m)):
            if m[j] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,\'\" ?!()-;:\n':
                break
            if j == len(m)-1:
                key.append(chr(i))
                res.append(m)
    return (key,res)
    

if __name__ == '__main__':

    q2a = '1c0111001f010100061a024b53535009181c'
    q2b = '686974207468652062756c6c277320657965'
    print('Q2:',xor(q2a,q2b))

    q3c = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    q3k,q3m = xor_find(q3c)
    print('Q3:','key:',q3k,'; m:',q3m)

    f = open('4.txt','r')
    q4c = f.read().split('\n')
 
    for i in q4c:
       # print(i)
        if xor_find(i) != ([],[]):
            q4k,q4m = xor_find(i)
            print('Q4:',';key:',q4k,'; m:',q4m)

        
    


    
