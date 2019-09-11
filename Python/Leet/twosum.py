def twoSum(target):
    try:
        target
    except Exception:
        print('Not a number.')
    else:
        nums = [3, 2, 5, 1, 7, 9]
        for n in range(0, len(nums)):
            for m in range(0, len(nums)):
                if nums[n] + nums[m] == target and n != m:
                    return [m, n]
           