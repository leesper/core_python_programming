def zip_map(lst1, lst2):
    return map(None, lst1, lst2)

if __name__ == '__main__':
    print('zip_map: {}'.format(zip_map([1, 2, 3], ['abc', 'def', 'ghi'])))
    print('zip: {}'.format(zip([1, 2, 3], ['abc', 'def', 'ghi'])))
