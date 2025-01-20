# 1st way


def reverse_string(string):
    reversed_str=""
    for char in string:
        reversed_str=char + reversed_str
    return reversed_str


input_string="Hello"
print("Original string:", input_string)
print("reversed string:", reverse_string(input_string))



 # 2nd Way

def reverse_string2(s):
     return s[::-1]
print(reverse_string2("Superbman"))