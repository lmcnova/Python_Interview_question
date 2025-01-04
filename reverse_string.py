# Reverse String 
value = "String"
print(value[::-1])

# Using a Function
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# Using a For Loop
s = "hello"
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
print(reversed_string) 

# Using the reversed() Function
s = "hello"
reversed_string = "".join(reversed(s))
print(reversed_string)  


# Using Recursion
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

print(reverse_string_recursive("hello"))  
