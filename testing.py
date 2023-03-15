total = 0
              
list_values = [1,2,3,4 ,0,4]
for index ,value in enumerate(list_values):
    if value in list_values:
        total += value
print(f" Total {total}")    

