from requests_html import HTMLSession
session = HTMLSession()

r = session.get("http://gx.news.163.com/special/nngg/")
news = r.html.find('p.nr-tit a')

for new in news:
    print(new.text) 
    print(new.absolute_links)  