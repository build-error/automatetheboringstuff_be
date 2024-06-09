import requests

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
print(res)

print(res.raise_for_status())
