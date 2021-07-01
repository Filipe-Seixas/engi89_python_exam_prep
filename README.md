# Python Exam Preparation

## Variables

- Define a variable - `name = "Filipe"`
- Find variable type - `print(type(name))`
- Get user input - `name = input("Enter name:  ")`

## Strings

- Use one backslash to add a single quote inside single quotes -  `single_quote = 'These\'s are single quotes and working perfectly fine!'`
```python
print(len(example_text))  # gives lengths of characters in string
print(example_text.strip())  # removes whitespaces before and after string
print(example_text.count("text"))  # count() method counts the number of times a word appears in string
print(example_text.lower())  # transforms text to lower case
print(example_text.upper())  # transforms text to upper case
print(example_text.capitalize())  # transforms first letter to upper
print(example_text.replace("with", ","))  # specified value is replaced with a specified value

greeting = "Hello World!"
# In python indexing starts with 0
print(greeting[6:])  # slicing the string from index 0 to 4
print(greeting[-6:])  # slicing string right to left
```

## Collections

### Lists

- Create list - `shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]`
```python
print(shopping_list[1]) # will display eggs
print(shopping_list[-1]) # will display the last item (bread)

shopping_list[0] = "mango"  # replace first item with mango
shopping_list.append("tuna")  # add tuna to the end of the list
shopping_list.pop(3)  # delete item with index 3
```
- Lists can have multiple data types mixed (int, strings, bool, ...)

### Tuples

- Create tuple - `essentials = ("paracetamol", "milk", "butter")`
- Tuples are IMMUTABLE, you can't change the date inside.
- `essentials.pop(2)` Will throw an ERROR because you can't delete data from tuples

### Dictionaries

- Create dictionary - `student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
  "completed_lesson_names": ["data types", "git and github", "operators", "Lists and Tuples"]}`
- dict = {'KEY': 'value', ...}
- No duplicates
```python
print(student_1["stream"])  # Get Value of 'stream' KEY
print(student_1.get("stream")) # Get Value of 'stream' KEY
print(student_1["completed_lesson_names"][-2]) # Print the second last index of key completed_lesson_names

student_1["completed_lessons"] = 3 # Update
student_1["completed_lesson_names"].remove("operators") # Delete

# Built in methods to use in dicts
print(student_1.keys())  # keys() gets all the key names
print(student_1.values())  # values() gets all the values inside each key
print(student_1.items())  # items() gets a list of the key:value pairs
if "stream" in student_1: # check if stream is present in dict
```

### Sets

- Create set - `myset = {"apple", "banana", "cherry"}`
- Unordered - Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- They also are unchangeable - Once a set is created, you cannot change its items, but you can add new items.
- No duplicates
- Can have mixed data types
```python
for x in thisset:  # Iterate through set
  print(x)

print("banana" in thisset) # check if banana is in set
thisset.add("orange") # add orange to set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical) # add items from tropical to thisset
thisset.remove("banana") # remove banana from set
thisset.discard("banana") # remove banana from set but if banana doesn't exist in set, don't throw error
thisset.clear() # clear set
```