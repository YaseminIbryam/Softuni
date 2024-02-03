def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)
        print("After calling function")
        return result

    return wrapper


@my_decorator
def my_function(x):
    return x * 2


result = my_function(5)
print(result)
