def contains(ordered_list, number):

    
    floor_index = 0
    ceiling_index = len(ordered_list)
    
    while floor_index < ceiling_index:
        guess_index = (floor_index + ceiling_index) // 2
        guess_value = ordered_list[guess_index]
        
        
        if guess_value == number:
            return True

        if guess_value > number:

            ceiling_index = guess_index - 1

        else:
            
            floor_index = guess_index + 1

    return False
