import sys 
data1=[]
data2=[]
n = 10
for k in range(n):
    a1 = len(data1)
    b1 = sys.getsizeof(data1)
    data1.append("text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111text11111")
    print("Length data1: {0:3d}; Size data1 in bytes: {1:4d}".format(a1, b1))

    a2 = len(data2)
    b2 = sys.getsizeof(data2)
    print("Length data2: {0:3d}; Size data2 in bytes: {1:4d}".format(a2, b2))
    data2.append("")