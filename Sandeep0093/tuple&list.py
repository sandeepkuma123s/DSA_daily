# difference between tuple and list in python
# tuple is immutable    
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)   
my_list = [1, 2, 3]
print("List before modification:", my_list)
my_list[0] = 10
print("List after modification:", my_list)
# my_tuple[0] = 10  # This will raise an error