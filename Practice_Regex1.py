import requests
import re

url = 'https://nostarch.com/contactus'
req = requests.get(url)
html = req.text

phoneRegex = re.compile(r'(\+\d\s)?(\d{3})\.(\d{3})\.(\d{4})')
result1 = re.findall(phoneRegex,html)
for phone in sorted(list(set(result1))):
    print(phone[0]+'-'.join([phone[1],phone[2],phone[3]]))

mailRegex = re.compile((r'\w+\@\w+\.com'))
result2 = re.findall(mailRegex,html)
for email in sorted(list(set(result2))):
    print (email)



