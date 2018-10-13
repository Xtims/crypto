import base64

#找到所有密文可能对应的key
def D(c):
    'c是bypes'
    ans = []
    for i in range(len(c)):
        t = []
        for ki in range(0xff+1):
            mi = c[i]^ki
            if chr(mi) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?\n\'\"-:':
                continue
            t.append(ki)
        ans.append(t)
    return ans

def hex_to_ascii(a):
    'a是16进制字符串'
    res = []
    for i in range(0,len(a),2):         #ascii码是8bits,对应于2个hexs
        res.append(chr(int(a[i:i+2],16)))
    return ''.join(res)

def str_to_hex(a):
    'a是字符串'
    res = []
    for i in range(len(a)):
        res.append(hex(ord(a[i]))[2:])
    return ''.join(res)
    

# k,c都是16进制字符串     
def Decrypt(k,c):
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
def Encrypt(k,m):
    c = []
    len_k = len(k)
    x = 0
    for i in range(0,len(m),2):
        mi = m[i:i+2]
        ki = k[x:x+2]
        ci = int(mi,16)^int(ki,16)
        x = (x+2)%len_k
        c.append(hex(ci)[2:])       #去掉0x
    return ''.join(c)

def find_length(c,k):
    #对密文长度遍历,找到在第一组里合适的key,确定长度
    for i in range(1,40):
        k_i = k[::i]
        t = []
        for a in k_i[0]:
            for j in range(len(k_i)):
                if a not in k_i[j]:
                    break    
            if j == len(k_i)-1:
                lenk = i
                return lenk

def find_key(k,len_k):
    #找到所有的key
    res = []
    for i in range(len_k):
        kk = k[i::len_k]
        ans = []
        for a in kk[0]:
            for j in range(len(kk)):
                if a not in kk[j]:
                    break
            if j == len(kk)-1:
               # print(i,a)
                ans.append(a)
        res.append(ans)
    return res

def c_to_m(c,key):
    #恢复明文
    m = ''
    x = 0
    for i in range(0,len(c)):
        ki = key[x]
        mi = c[i]^ki[0]
        x = (x+1)%len(key)
        m = m+chr(mi)
    return m



with open('6.txt') as f:
    c = base64.b64decode(f.read())
k = []
k = D(c)
len_k = find_length(c,k)
res = find_key(k,len_k)
m = c_to_m(c,res)
key = ''.join(chr(i[0]) for i in res)
print('The length of key is:',len_k)
print('The key is:[',key,']')
print('The message is:','\n',m)


