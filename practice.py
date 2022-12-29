from bs4 import BeautifulSoup
import requests

first_address ="https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q="
search = input("검색할 키워드는? :")

search_daum = first_address +search

result =requests.get(search_daum)
soup = BeautifulSoup(result.text, "html.parser")
articles = soup.select(".wrap_cont")

for rank_count, article in enumerate(articles,1): 
    article_company = article.select_one(".cont_info > a").text
    article_title = article.select_one(".tit_main.fn_tit_u")

    print(f"<{rank_count}>")
    print(f"{article_company} " )
    print(f"{article_title.text} " )
    print(f"{article_title.get('href')} " )
    print()
    
