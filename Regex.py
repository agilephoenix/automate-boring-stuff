import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # 1. area code
    (\s|-|\.)?                        # 2. separator
    (\d{3})                           # 3. first 3 digits
    (\s|-|\.)                         # 4. separator
    (\d{4})                           # 5. last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # 6. extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)

for group in emailRegex.findall(text):
    matches.append(group[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')
