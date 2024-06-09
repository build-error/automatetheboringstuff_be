import webbrowser, sys, pyperclip

# webbrowser.open('https://inventwithpython.com/')

print(sys.argv)

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

print(address)

webbrowser.open('https://www.google.com/maps/place/' + address)
