import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")

menu_area = bsObj.find("ul", {"class":"an_l"})

li_List = menu_area.findAll("li")

for li in li_List:
    a_tag = li.find("a")
    span_tag = a_tag.find("span", {"class":"an_txt"})
    print(span_tag.text)




