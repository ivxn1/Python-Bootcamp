from bs4 import BeautifulSoup

with open('website.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup)
    a_els = soup.select_one("a")
    print(a_els.href)

