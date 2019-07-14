import bs4

html_str = "<html><body><div>Find this tag</div></body></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))