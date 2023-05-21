# Data Structure
## List

### create empty list
list_data1 = []
list_data2 = list()

### initialize list
list_data3 = [4, 2, 5, 2, True, 0, 7, "Hello"]

### read value
print(f"list_data3[3]: {list_data3[3]}")

### update value
list_data3[0] = "change"
print(f"list_data3 change list_data3[0]: {list_data3}")
list_data3.append(10)
print(f"list_data3 append(10): {list_data3}")
list_data3.append([14, 25])
print(f"list_data3 append([14, 25]): {list_data3}")
list_data3.extend([62, 32])
print(f"list_data3 extend([62, 32): {list_data3}")
list_data3.insert(1, "value")
print(f"list_data3 insert(1, 'value'): {list_data3}")

### delete value
del list_data3[0]
print(f"list_data3 del list_data3[0]: {list_data3}")

### copy, deep copy
print("\n----Before Copy----")
list_data4 = list_data3
list_data4[0] = "copy"
print(f"list_data3: {list_data3}\nlist_data4: {list_data4}")

print("\n----After Shallow Copy----")
list_data5 = list_data3.copy()
list_data5[0] = "new"
list_data5[-3][0] = "deep copy fail"
print(f"list_data3: {list_data3}\nlist_data5: {list_data5}")


print("\n----After Deep Copy----")
import copy
list_data6 = copy.deepcopy(list_data3)
list_data6[0] = "test"
list_data6[-3][0] = "deep copy success"
print(f"list_data3: {list_data3}\nlist_data6: {list_data6}")

## Dictionary

### create empty dict
dict_data1 = {}
dict_data2 = dict()

### initialize dict
dict_data3 = {"key": "value", "eun": 20, "dou": 25}

### read value
print(f"dict_data3[key]: {dict_data3['key']}")
print(f"dict_data3[key]: {dict_data3.get('extra', None)}")

### update value
dict_data3["new"] = 10
print(f"dict_data3: {dict_data3}")
dict_data3.update({"next": 214, "elder": True})
print(f"dict_data3 update: {dict_data3}")

### delete value 
dict_data3["new"]
print(f"dict_data3 del dict_data3[new]: {dict_data3}")

## Tuple



## Set

