
# IO

## Input && Output
### input() / print()

input_data = input("Input Data: ")
print(f"input_data: {input_data}, type: {type(input_data)}")

## File Input && Output
### open() / write() / read() / readline() / readlines() / close()

### check test.txt file
f = open("test.txt", "w")
f.write("Welcome New World!!!")
f.close()

f = open("test.txt", "r")
result = f.read()
print(result)
f.close()

### check new_test.txt file
with open("new_test.txt", "w") as f:
    for i in range(1, 10):
        f.write(f"Hello {i}\n")

with open("new_test.txt", "r") as f:
    for text in f.readlines():
        print(text, end="")