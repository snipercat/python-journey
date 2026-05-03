

# List

Use **lists** if order matters and duplicates are allowed

```py
my_list_constructor = list()
my_list_empty = []
my_list_initial_data = [35, 24, 62, 52, 30, 30, 17]
```

# tuple
Use **tuples** for constant data, once created data can't change
```py
my_tuple_constructor = tuple()
my_tuple_empty = ()
my_tuple_initial_data = (35, 1.77, "Python", "Tuple", "values")
```
# set
Use **Sets** to remove duplicates, perform fast rearches and st operations like intersect or union.
Values can not be edited but new data can be inserted or deleted.
Since they are unordered ,can't access with `my_set[0]`

```py
my_set_constructor = set()
my_set_initial_data = {35, 1.77, "Python", "Set", "values"}
#search
print("Set" in my_set_initial_data) # True
````
