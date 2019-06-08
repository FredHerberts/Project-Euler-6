import time
start = time.time()
squares = []
def squared(y):
    for x in range(1,y+1):
        x = x**2
        squares.append(x)
    print(abs(sum(squares)-(((1+y)*y)/2)**2))

squared(100)
end = time.time()
print(end - start)
