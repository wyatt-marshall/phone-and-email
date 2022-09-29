#! python3
# phoneAndEmail.py - simple program to find phone numbers and email addresses on the clipboard

import re, pyperclip

def dups(lst):
    noDups = []
    for string in lst:
        if string not in noDups:
            noDups.append(string)
    
    
    for x in range(len(noDups)):
        count = lst.count(noDups[x])
        if count != 1:
            noDups[x] = noDups[x] + ' ({})'.format(count)

    return noDups

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?                   #area code
    (\s|-|\.)?                          #separator
    (\d{3})                             #first three digits
    (\s|-|\.)                           #separator
    (\d{4})                             #last 4 digits
    (\s*|(ext.|x|ext)\s*(\d{2,5}))?     #extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   #username
    @                                   #@ symbol
    [a-zA-Z0-9.-]+                      #domain name
    (\.[a-zA-Z]{2,4})                   #dot something
)''', re.VERBOSE)

text = str(pyperclip.paste())           #string from clipboard

phoneNums = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    phoneNums.append(phoneNum)
phoneNums = dups(phoneNums)

emails = []
for groups in emailRegex.findall(text):
    emails.append(groups[0])
emails = dups(emails)

matches = []
if len(phoneNums) == 0:
    phoneNums = "No phone numbers found."
else:
    phoneNums = 'Phone numbers: ' + ', '.join(phoneNums)
matches.append(phoneNums)

if len(emails) == 0:
    emails = "No emails found."
else:
    emails = 'Emails: ' + ', '.join(emails)
matches.append(emails)

finalCopy = '\n'.join(matches)
pyperclip.copy(finalCopy)
print(finalCopy)

