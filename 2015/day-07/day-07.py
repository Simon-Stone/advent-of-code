import re


with open('2015/day-07/input.txt') as f:
    lines = f.readlines()


code_chars = 0
printed_chars = 0

r = re.compile(r'\\x[0-9]{2}')
for line in lines:
    s = line.strip()
    print(s)
    code_chars += len(s)
    s = re.sub(r, 'a', s)    
    s = re.sub(r'\\{2}', r'\\', s)
    s = re.sub('^"', '', s)
    s = re.sub('"$', '', s)
    printed_chars += len(s)
    print(s)
    
print(f'{code_chars - printed_chars = }')
