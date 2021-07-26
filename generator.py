def gen_func(num):
    for i in range(num):
        yield i+1  
g=gen_func(5)
print(next(g)) # 1
print(next(g)) # 2