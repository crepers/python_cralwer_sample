import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

login_area = bsObj.find("div", {"class":"section_login"})
naver_Sign_in = login_area.find("i")

# print(login_area)
print(naver_Sign_in.text)