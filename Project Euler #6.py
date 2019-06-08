import time
start = time.time()

def squared(y):
    x = sum(x**2 for x in range(1,y+1))
    print(abs((x-(((1+y)*y)/2)**2)))

squared(100)
end = time.time()
print(end - start)
