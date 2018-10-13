
#找到所有密文可能对应的key
def D(c):
    ans = []
    for i in range(0,len(c),2):
        t = []
        ci = int(c[i:i+2],16)
        for ki in range(0xff+1):
            mi = ci^ki
            if chr(mi) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?\n\'':
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
    #对密文长度遍历,找到在第一组里合适的key,确定长度为7
    for i in range(1,40):
        k_i = k[::i]
        t = []
        for a in k_i[0]:
            for j in range(len(k_i)):
                if a not in k_i[j]:
                    break    
            if j == len(k_i)-1:
                lenk = i
                print('The length of key is:',i)
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
    print('The key is:',res)
    return res

def c_to_m(c,res):
    #恢复明文
    m = ''
    x = 0
    for i in range(0,len(c),2):
        ci = c[i:i+2]
        ki = res[x]
        mi = int(ci,16)^ki[0]
       # print(ci,ki,mi,chr(mi))
        x = (x+1)%7
        m = m+chr(mi)
    print('The m is:\n',m)
    return m


c = 'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'
k = []
k = D(c)
len_k = find_length(c,k)
res = find_key(k,len_k)
m = c_to_m(c,res)



    
        
