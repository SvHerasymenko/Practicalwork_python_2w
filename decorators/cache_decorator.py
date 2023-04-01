from cachetools import cached, TTLCache

def kesh(function):
    my_cache = TTLCache(maxsize=100, ttl=300)
    def kesh_func(numbers):
        if my_cache.get('my_key') == function(numbers):
            result = my_cache.get('my_key')
            print(f"cache: {result}")
        else:
            my_cache['my_key'] = f'{function(numbers)}'
            print("update data")
            kesh_func(numbers)
    return kesh_func


@kesh
def kesh_numbers(numbers):
    return f"{numbers}"

kesh_numbers([1,2,3])

