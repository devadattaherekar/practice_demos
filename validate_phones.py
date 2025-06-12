import re

phones="""
1-212-456-7890
001-212-456-7890
191-212-456-7890
+91-9850166398
9850166398
8806330448
+918806330448
+91-8806330448
+91 8806330448
"""
pattern="[\+]91"
for each_match in re.finditer(pattern,phones):
    print(each_match.group(0))