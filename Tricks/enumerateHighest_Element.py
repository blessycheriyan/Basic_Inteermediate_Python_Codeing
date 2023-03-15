# Second Approach of the freq character of  the Strings
def freq_names(person_name):
        frequency = {}
        for _ , name_  in enumerate(person_name):
                
                # Check for presence
                if name_  not in  frequency:
                        frequency[name_ ] = 1 
                # If present increment the frequency by factor of 1                      
                else:
                        frequency[name_ ] += 1
        print(frequency)                
        
person_name  = "Blessen Ninan" 
val_ = freq_names(person_name)
       