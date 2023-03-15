class Human:
    
    population = 0
    data = []
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
        #self.population
        Human.population +=1
        Human.data.append(self.age)
        
    def greetings(self):
        print(f"Students Names: {self.name} age is {self.age} and {self.population} and {Human.data}")
            
name = ["James","Ninan","George","Abin","Kavitha"]        
va_ = Human(name,27)   
va_.greetings()     