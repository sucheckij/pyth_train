import time

def decoratorMethod(func):

    def wrapper(*args,**kwargs):
        print("-*-"*10)
        start = time.time()
        res = func(*args,**kwargs)
        print("-*-"*10)
        print(f"Czas wykonania: {time.time()-start:.2f}")
        print("-*-"*10)
        return res

    return wrapper


