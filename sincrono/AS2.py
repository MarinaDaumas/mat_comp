def sum67(nums):
    sum = 0
    last_was_6 = False
    
    for item in nums:
        if item == 6:
            last_was_6 = True
        else:
            pass

        if not last_was_6:
            sum += item
            
        elif item == 7:
            last_was_6 = False
    
    return sum

sum67([1, 4, 6, 6, 8, 3, 7, 2, 6, 8, 8, 8, 7, 9])