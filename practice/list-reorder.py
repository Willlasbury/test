def reorder(list):
    n = len(list)

    new_list = list

    new_list[0] = list[n-1]
    new_list[-1] = list[0]

    return new_list

    

