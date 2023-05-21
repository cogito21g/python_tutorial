# String
## 한 줄 표기

print("----One Line String----")

str_var1 = 'Hello World!!!'
str_var2 = "Hello World!!!"
print(f"str_var1 = {str_var1}") 
print(f"str_var2 = {str_var2}") 

print("----End----")

## 여러 줄 표기

print("----Multi Line String----")

str_var3 = ''' Multi
Line
String'''
str_var4 = """ Multi
    Line 
String
"""
print(f"str_var3 = {str_var3}") 
print(f"str_var4 = {str_var4}") 

print("----END----")

## format: %, format, f-string

print("----Format----")

str_format1 = "var %3d" % (10)
str_format2 = "var {}".format(10)
str_format3 = f"var {10}"

print(f"str_format1: {str_format1}")
print(f"str_format2: {str_format2}")
print(f"str_format3: {str_format3}")

print("----END----")

## escape sequence: \t, \n, \\, \*

print("----Escape Sequence----")




print("----END----")