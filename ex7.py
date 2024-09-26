decimal_number = int(input("輸入一個十進制數字: "))
binary_number = bin(decimal_number)[2:]
octal_number = oct(decimal_number)[2:]
hexadecimal_number = hex(decimal_number)[2:].upper()
print(f"二進制: {binary_number}") 
print(f"八進制: {octal_number}") 
print(f"十六進制: {hexadecimal_number}")