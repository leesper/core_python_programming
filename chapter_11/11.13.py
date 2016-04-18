def multi(x, y):
    return x * y

print('8! = {}'.format(reduce(multi, range(1, 9))))
print('9! = {}'.format(reduce(lambda x, y: x * y, range(1, 10))))
