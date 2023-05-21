# Operator
## 산술 연산자: +, -, *, /, ?, //, **, @

print(f"----  산술 연산자 ----")

num1 = int(input("Input Integer Number: "))
num2 = int(input("Input Integer Number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 % num2}")

print("----End----")

## 비교 연산자: <, <=, >, >=, ==, !=

print(f"----  비교 연산자 ----")

num3 = int(input("Input Integer Number: "))
num4 = int(input("Input Integer Number: "))

print(f"{num3} < {num4} = {num3 < num4}")
print(f"{num3} <= {num4} = {num3 <= num4}")
print(f"{num3} > {num4} = {num3 > num4}")
print(f"{num3} >= {num4} = {num3 >= num4}")
print(f"{num3} == {num4} = {num3 == num4}")
print(f"{num3} != {num4} = {num3 != num4}")

print("----End----")

## 논리 연산자: and, or, not
### 단락 회로

print(f"----  논리 연산자 ----")

state = bool(input("Input Boolean(True/False): "))
n_state = not state

print("----AND----")
print(f"{state} and {state} , result = {state and state}")
print(f"{state} and {n_state} , result = {state and n_state}")
print(f"{n_state} and {state} , result = {n_state and state}")
print(f"{n_state} and {n_state} , result = {n_state and n_state}")
print("----OR----")
print(f"{state} or {state} , result = {state or state}")
print(f"{state} or {n_state} , result = {state or n_state}")
print(f"{n_state} or {state} , result = {n_state or state}")
print(f"{n_state} or {n_state} , result = {n_state or n_state}")
print("----NOT----")
print(f"not {state}, result = {not state}")
print(f"not {n_state}, result = {not n_state}")

print("----End----")

## 비트 연산자: &, |, ^, ~
### bin(0b1101)

print(f"---- 비트 연산자 ----")
print(f"{bin(0b1001)} & {bin(0b1101)} = {bin(0b1001 & 0b1101)}")
print(f"{bin(0b1001)} | {bin(0b1101)} = {bin(0b1001 | 0b1101)}")
print(f"{bin(0b1001)} ^ {bin(0b1101)} = {bin(0b1001 ^ 0b1101)}")
print(f"~{bin(0b1001)} = {bin(~0b1001)}")
print(f"{bin(0b1001)} >> 2 = {bin(0b1001 >> 2)}")
print(f"{bin(0b1001)} << 1 = {bin(0b1001 << 1)}")

print("----End----")
