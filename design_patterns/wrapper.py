# wrapper and decorator demonstration

def outside_fn(inside_fn):
    def wrapper():
        print(1)
        inside_fn()
        print(3)
    return wrapper

#@outside_fn
def inside_fn():
    print(2)
    
if __name__ == '__main__':
    outside_fn(inside_fn)()





