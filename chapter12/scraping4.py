import bs4

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]

print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexsistent_addr') == None)
print(spanElem.attrs)
