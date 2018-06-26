def MergeMeeting(list1):
    if len(list1) < 2:
        raise IndexError('Less than two numbers are not allowed')

    s = sorted(list1)
    s1 = [s[0]]

    for start, end in s[1:]:
        start1, end1 = s1[-1]

        if (start <= end1):
            s1[-1] = (start1,max(end1, end))
        else:
            s1.append((start, end))

    return s1
