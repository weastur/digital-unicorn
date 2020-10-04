def pred(item):
    return item == 42

def first_true(iterable, default=False, pred=None):
    return next(filter(pred, iterable), default)

print(first_true([1, 2, 3, 42], 100500, pred))
print(first_true([1, 2, 3], 100500, pred))
