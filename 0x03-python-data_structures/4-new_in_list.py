def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    for i in range(len(my_list)):
        new_list.append(element if i == idx else my_list[i])
    return new_list
