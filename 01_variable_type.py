# Variable
## name_var = iteral_value

num_var = 10

# Type
## Numbers: int, float, complex
## String: ' ', " ", ''' ''', %, format, f-string 
## Boolean: True, False

int_var = 5
float_var = 4.0
str_var1 = 'Hello'
str_var2 = f'Hello {int_var}'
bool_var1 = True
bool_var2 = False

print("----Test----")

print(f"int_var: {int_var}, type: {type(int_var)}")
print(f"float_var: {float_var}, type: {type(float_var)}")
print(f"str_var1: {str_var1}, type: {type(str_var1)}")
print(f"str_var2: {str_var2}, type: {type(str_var2)}")
print(f"bool_var1: {bool_var1}, type: {type(bool_var1)}")
print(f"bool_var2: {bool_var2}, type: {type(bool_var2)}")

print("------------")

# Type Conversion
## Number: int() / float()
## String: str()
## Boolean: bool()

int_to_float = float(int_var)
print(f"int_to_float: {int_to_float}, type: {type(int_to_float)}")
float_to_int = int(float_var)
print(f"float_to_int: {float_to_int}, type: {type(float_to_int)}")
int_to_str = str(int_var)
print(f"int_to_str: {int_to_str}, type: {type(int_to_str)}")
float_to_str = str(float_var)
print(f"int_to_str: {float_to_str}, type: {type(float_to_str)}")

