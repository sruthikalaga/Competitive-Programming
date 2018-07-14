import random


def randomnumber(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(list_nums):
    # Shuffle the input in place
    if len(list_nums) <= 1:
        return list_nums

    l = len(list_nums) - 1

    for x in range(0, l):
        randomnum = randomnumber(x, l)
        if randomnum != x:
            list_nums[x], list_nums[randomnum] = list_nums[randomnum], list_nums[x]
