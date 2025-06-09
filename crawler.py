import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=news&query=일론머스크"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 클래스가 두 개 이상인 div 중 하나 선택 (여러 개가 있을 수 있으니 select_all로 리스트로 받음)
container_divs = soup.select("div.sds-comps-base-layout.sds-comps-full-layout")

for container_div in container_divs:
    # 각 div 안에서 첫 번째 a 태그 찾기
    first_a = container_div.find("a")
    if first_a:
        # a 태그 안의 span 태그 찾기
        title_span = first_a.find("span")
        if title_span:
            print(title_span.text.strip())
    # 10개만 출력하도록 제한
    if container_divs.index(container_div) >= 9:
        break
