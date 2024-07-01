import requests, sys, bs4, webbrowser

print('Searching ...')

res = requests.get('https://pypi.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
	print('Opening', urlToOpen)
	webbrowser.open(urlToOpen)
