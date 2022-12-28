from bs4 import BeautifulSoup
import requests

base_url ="https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

keyword = input("검색어를 입력하세요 :")
search_url = base_url + keyword

r = requests.get(search_url)
soup = BeautifulSoup(r.text, "html.parser")
items = soup.select(".total_wrap.api_ani_send")
for rank_num,item in enumerate(items,1) :
    print(f"<{rank_num}>" ) 
    ad = item.select_one(".link_ad")
    if ad:
        print("광고입니다.")
        continue
    
    blog_title = item.select_one(".sub_txt.sub_name").text
    print(f"{blog_title}" )
    post_title = item.select_one(".api_txt_lines.total_tit._cross_trigger")
    print(f"{post_title.text}" )
    print(f"{post_title.get('href')}" )
    print()