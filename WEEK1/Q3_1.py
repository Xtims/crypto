import base64

table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def str_to_hex(s):
    res = ''
    for i in range(len(s)):
        res += hex(ord(s[i]))[2:]
    return res


def hex_to_base64(h):
    m = ''
    for i in range(0, len(h), 6):
        if len(h) - i >= 6:
            x = 6
        elif 4 == len(h) - i:  # 余两个
            x = 4
        else:  # 余一个
            x = 2
        hi = h[i:i + x]
        b = bin(int(hi, 16))
        b = b[2:]
        if len(b) < x * 4:
            b = '0' * (x * 4 - len(b)) + b  # 补零
        # print('xx')
        # for i in range(0,len(b),8):
        #     print(b[i:i+8])
        for j in range(0, len(b), 6):
            if x == 4 and j == 12:  # 余两个时取6+6+4
                y = 4
            elif x == 2 and j == 6:  # 余一个时取6+2
                y = 2
            else:
                y = 6
            t = b[j:j + y]
            if y < 6:
                t = t + '0' * (6 - y)  # 二进制位补零
            bi = int(t, 2)
            mi = table[bi]
            m = m + mi
            #    print(bi,mi,m)
            if x == 4 and j == 12:
                m = m + '='
            if x == 2 and j == 6:
                m = m + '=='
    # print(i,m)
    return m


def base64_to_hex(h):
    m = ''
    for i in range(0, len(h), 4):
        hi = h[i:i + 4]
        x = hi.count('=')
        if x == 0:
            for j in range(len(hi)):
                mi = bin(table.find(hi[j]))[2:]
                if len(mi) < 6:
                    mi = '0' * (6 - len(mi)) + mi
                m += mi
        if x == 1:
            for j in range(2):
                mi = bin(table.find(hi[j]))[2:]
                if len(mi) < 6:
                    mi = '0' * (6 - len(mi)) + mi
                m += mi
            mi = bin(table.find(hi[2]))[2:]
            if len(mi) < 4:
                mi = '0' * (4 - len(mi)) + mi
            m += mi
        if x == 2:
            mi = bin(table.find(hi[0]))[2:]
            if len(mi) < 6:
                mi = '0' * (6 - len(mi)) + mi
            m += mi
            mi = bin(table.find(hi[1]))[2:]
            if len(mi) < 2:
                mi = '0' * (2 - len(mi)) + mi
            m += mi
    return hex(int(m, 2))[2:]


def main():
    q1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    res = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print('Q1    :', hex_to_base64(q1))
    print('answer:', res)


if __name__ == '__main__':
    main()
