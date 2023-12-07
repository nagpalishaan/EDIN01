def hamming(x, y):
    d = 0

    for x_i, y_i in zip(x, y):
        if x_i != y_i:
            d += 1

    return d    


def LFSR(c, s, L, N):
    while len(s) != N:
        next_state = 0
        for i in range(L):
            next_state -= c[i] * s[len(s)-i-1]

        next_state %= 2

        s += [next_state]

    return s

def generate(z, c):
    L = len(c)
    N = len(z)
    
    min_p = 1
    min_s = []
    for k in range(pow(2, L)):
        b = format(k, "b").zfill(L)
        s = []
        for char in b:
            if char == "0":
                s.append(0)
            else:
                s.append(1)
        
        u = LFSR(c, s, L, N)
        p = hamming(u, z) / N

        if p <= min_p:
            min_p = p
            min_s = s
    
    print(1 - min_p)
    return min_s


if __name__ == '__main__':
    z_txt = "1110000100101110110001101001000110010000010100110101100101101011110100010001001010110010111111011011000100011011001101011110110111110000111001101011001111110010110000111011010011011111111011001"
    z = []
    for char in z_txt:
        z.append(int(char))
    
    s1 = []
    s2 = []
    s3 = []
    c1 = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
    c2 = [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
    c3 = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]

    t1 = generate(z, c1)
    t2 = generate(z, c2)
    t3 = generate(z, c3)

    print(t1[:13])
    print(t2[:15])
    print(t3[:17])

    # Check for errors
    for i1, i2, i3, x in zip(t1, t2, t3, z):
        if i1 + i2 + i3 >= 2:
            if x == 0:
                print("wrong")
        else:
            if x == 1:
                print("wrong")
