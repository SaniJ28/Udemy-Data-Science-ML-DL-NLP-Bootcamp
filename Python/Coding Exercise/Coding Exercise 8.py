def remove_duplicates(lst):
    unique_list=[]
    for item in lst:
        if item not in unique_list:
           unique_list.append(item)
    return unique_list         

