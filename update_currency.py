import re

# Read the file
with open('pages/reports.py', 'r') as file:
    content = file.read()

# Find all instances of f"${...}" and replace with format_currency(...)
pattern = r'f"\$\{([^}]+)\}"'
# First, fix the simple replacements
replaced_content = re.sub(pattern, r'format_currency(\1)', content)

# Now fix any instances where the formatting part (:,.2f) was incorrectly included
pattern2 = r'format_currency\(([^:]+):,.2f\)'
replaced_content = re.sub(pattern2, r'format_currency(\1)', replaced_content)

# Write the updated content back to the file
with open('pages/reports.py', 'w') as file:
    file.write(replaced_content)

print("Currency formatting updated in reports.py")
