# Python 3
import re
import sys

def validate(s):
    import re
    if not s[0] in "456": return False
    if not re.match("[0-9-]+", s): return False
    if sum([1 if "0" <= _ and _ <= "9" else 0 for _ in s]) != 16: return False
    if not (len(s) == 16 or len(s) == 19 and s[4] == "-" and s[9] == "-" and s[14] == "-"): return False
    s = s.replace("-", "")
    for i in range(len(s)-3):
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]: return False
    return True


stdin = sys.stdin
t = int(stdin.readline())
for z in range(t):
    line = stdin.readline().rstrip()
    if(validate(line)):
        print("Valid")
    else:
        print("Invalid")

"""
Sample Input 

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid

"""