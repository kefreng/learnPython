import pyqrcode
url = pyqrcode.create("http://janihatesyouall.blogspot.com/")
url.svg('uca-url.svg', scale=4)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))