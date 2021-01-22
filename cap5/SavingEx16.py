from cap5.SavingEx15 import gcd

'''
N = 50
triples = sorted(
    ((a,b,c) from a,b,c in (
             ((m**2 - n**2), ( 2*m*n), ( m**2 + n**2))
                for m in range(1, int(N**.5)+1)
                for n in range(1,m)
                if (m-n) % 2 and gcd(m,n) == 1
             )if c <= N), key= lambda *triple: sum(*triple)
)
'''


def gen_triples(N):
    for m in range(1, int(N ** .5) + 1):
        for n in range(1, m):
            #print('--------')
            #print("m,n", m, n)
            #print("gcd: ", gcd(m, n))
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m ** 2 + n ** 2
                #print("c : " , c)
                if c <= N:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    #print("(a, b, c)" , (a, b, c))
                    yield (a, b, c)


triples = sorted(gen_triples(50), key=lambda *triple: sum(*triple))

print(triples)
