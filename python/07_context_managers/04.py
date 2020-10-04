def zip_longest(*args, fillvalue=None):
    iterators = [iter(item) for item in args]
    while True:
        current_item = []
        found = False
        for iterable in iterators:
            element = fillvalue
            try:
                element = next(iterable)
                found = True
            except StopIteration:
                pass
            current_item.append(element)
        if not found:
            break
        yield tuple(current_item)

print(list(zip_longest([1], (1, 2), 'abc', fillvalue='empty')))

