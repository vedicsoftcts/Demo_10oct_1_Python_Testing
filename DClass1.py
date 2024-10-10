class employee:
    def __init__(self,name,age):
        #print("Its employee class")
        self.name = name
        self.age = age
    def display(self):
        return f"Hello, I am {self.name}, my age is {self.age}"

if __name__ == "__main__":
    emp1 = employee("Ravi",44)
    emp2 = employee("Vijay",23)

    print(emp1.name)
    print(emp1.display())
    print(emp2.display())
    '''
    expected_output = "Hello, I am Vijay, my age is 23"
    
    if emp2.display() == expected_output:
        print(True)
    else:
        print(False)
    '''
