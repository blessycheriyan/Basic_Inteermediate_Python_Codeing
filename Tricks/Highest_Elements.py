
list_values  = [1,2,3,4,5,1,2,3,6,9]
# Iterate li on the list
def unique_values(li):
    new_values = []    
    for i in li:
            # Adding only unique elements in new list
            if i not in new_values:
                    new_values.append(i)
                    
    return new_values   

print(unique_values(list_values))