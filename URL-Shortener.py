import pyshorteners

def shorten(link):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(link)

link = input("Enter Link Here --> ")
print(f'Shortened URL --> {shorten(link)}')
