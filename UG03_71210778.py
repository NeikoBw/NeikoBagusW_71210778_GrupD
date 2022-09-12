import timeit

def deret_ajaib_iteratif(n):
    x=[1,2,3,4,5]
    for i in range(n, 100):
        a = x[(i-3)-1]*x[(int(i/2))-1]
        x.append(a)
        start = timeit.default_timer()
        end = timeit.default_timer()
        print("Waktu yg Ditempuh:",end-start)

def deret_rekursif(n):        
    if n < 6:
        return n
    else:
        return deret_rekursif(n-2) + deret_rekursif(n//2)

def deret_ajaib_rekursif(n):
    start = timeit.default_timer()
    for i in range(100):
        deret_rekursif(n)
        end = timeit.default_timer()
        print("Waktu yg Ditempuh: ",end-start)

deret_ajaib_rekursif(6)
deret_ajaib_iteratif(6)