

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        values = original_func(*args, **kwargs)
        even_number = []
        odd_number = []
        for i in values:
            if i % 2 == 0:
                even_number.append(i)
            else:
                odd_number.append(i)
        return f"Juft sonlar ro'yxati\n{even_number}\nToq sonlar ro'yxati\n{odd_number}"
    return wrapper_func


@decorator_func
def get_item(item):
    return item


items = get_item([i for i in range(1, 11)])
print(items)