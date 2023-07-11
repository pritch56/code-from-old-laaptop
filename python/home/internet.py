import urllib.request 
webUrl = urllib.request.urlopen('https://www.google.co.uk/?safe=active&ssui=on')
print('result code:' + str(webUrl.getcode()))
data = webUrl.read()


textjl = open (r'C:\Users\Ben Pritchard\python\indexx.html', 'w')

textjl.write(str(data))

textjl.close()