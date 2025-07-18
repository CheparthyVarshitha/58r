data_types = ['int', 'float', 'str', 'bool']

# Conversion Table Header
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("From\\To", "int", "float", "str", "bool"))
print("-" * 50)

# Conversion possibilities
for from_type in data_types:
    row = [from_type]
    for to_type in data_types:
        if from_type == to_type:
            row.append("✓")  # Same type
        elif from_type == 'str' and to_type in ['int', 'float', 'bool']:
            row.append("✓ (if valid)")
        elif from_type in ['int', 'float', 'bool'] and to_type in ['str', 'bool']:
            row.append("✓")
        elif from_type == 'float' and to_type == 'int':
            row.append("✓")
        elif from_type == 'int' and to_type == 'float':
            row.append("✓")
        else:
            row.append("✗")
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*row))
