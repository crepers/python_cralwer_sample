from urllib.request import urlopen
import bs4

url = "https://news.naver.com"
html = urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")

