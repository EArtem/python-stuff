import pandas as pd

list1 = pd.read_csv('file1.txt', header=None).get(0).to_list()

list2 = pd.read_csv('file2.txt', header=None).get(0).to_list()
print(list1, list2)
result = [num for num in list1 if num in list2]

print(result)

same_numbers = list(set(list1) & set(list2))

print(same_numbers)
