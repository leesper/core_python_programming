def average(nums):
    return reduce(lambda x, y: x + y, nums) / float(len(nums))

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(average(nums))
