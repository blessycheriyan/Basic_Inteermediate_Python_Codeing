# First Approach for Unique Elements of the list
# Iterate list_values on the list

def unique_values(list_values):
        new_list = []    
        for _ in list_values:
                # Adding only unique elements in new list
                if _ not in new_list:
                    new_list.append(_)
                        
        return new_list  

list_values  = [1,2,3,4,50,1,2,3,6,9,8,100,234]
new_values = unique_values(list_values)
print(new_values)

################################### OUTPUT ############

#  [1, 2, 3, 4, 50, 6, 9, 8, 100, 234]


                 