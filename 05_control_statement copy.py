# 제어문

## 조건문
### if문: if ~ elif ~ else
### 중첩

print("----if----")

int_var = 14

if int_var > 10:
    print("int_var is bigger than 10")
if int_var > 5: 
    print("int_var is bigger than 5")

print("----END----")

print("----if ~ else----")

if int_var > 10:
    print("int_var is bigger than 10")
else:
    print("int_var is not bigger than 10")

print("----END----")

print("----if ~ elif ~ else----")

if int_var > 10:
    print("int_var is bigger than 10")
elif int_var > 5: 
    print("int_var is bigger than 5")
else:
    print("else")

print("----END----")


## 반복문
### while문
### for ... in (iterable 객체)

print("----While----")
i = 0
while i < 10:
    print("Hello {i}")
    i += 1

print("----END----")

print("----FOR----")
for i in range(10):
    print("Hello {i}")

print("----END----")

## break, continue

print("----Break----")

for i in range(10):
    if i == 3:
        break
    print(f"Hello {i}")
print("end for")

print("----END----")


print("----Continue----")

for i in range(10):
    if i == 3:
        continue
    print(f"Hello {i}")
print("end for")

print("----END----")