def filter_leap(years):
    return filter(lambda y: (y % 4 == 0 and y % 100 != 0) or y % 400 == 0, years)

if __name__ == '__main__':
    years = range(1992, 2401)
    print('leap years are: {}'.format(filter_leap(years)))
