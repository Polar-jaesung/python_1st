from bs4 import BeautifulSoup
import requests

head_address= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" }
url = "https://www.melon.com/chart/index.htm"
    
result = requests.get(url,headers=head_address)


html = result.text

soup = BeautifulSoup(html,"html.parser")


top1_50= soup.select(".lst50")
top50_100 = soup.select(".lst100")
top1_100 = top1_50+top50_100

for count,i in enumerate(top1_100,1):
    title = i.select_one(".ellipsis.rank01 a ")
    album = i.select_one(".ellipsis.rank03 > a")
    print(f"<{count}>")
    print(title.text)
    print(album.text)

    singers = i.select(".ellipsis.rank02 >a")
    for singer in singers:
        print(singer.text)
    print()