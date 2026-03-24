import requests
from lxml import html
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard&hotlist_flag=999"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# def fetch_image_xpath(href):
#     response = requests.get(href, headers=HEADERS, verify=False)
#     response.raise_for_status()
#     tree = html.fromstring(response.content)
#     # XPath 경로로 영역 선택
#     img_area = tree.xpath('/html/body/div[6]/div[2]/div[3]/div/table[3]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody')
#     if img_area:
#         img_tag = img_area[0].xpath('.//img')
#         if img_tag and img_tag[0].get('src'):
#             return img_tag[0].get('src')
#     return None

def fetch_image_from_board(href):
    try:
        print(f"[DEBUG] 게시글 링크 접속: {href}")
        response = requests.get(href, headers=HEADERS, verify=False)
        print(f"[DEBUG] 응답 코드: {response.status_code}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # .board-contents 클래스 기준으로 영역 선택
        board_contents = soup.select_one(".board-contents")
        if not board_contents:
            print("[DEBUG] .board-contents 영역을 찾지 못함")
            return None
        img_tag = board_contents.find("img")
        if img_tag:
            print(f"[DEBUG] 이미지 태그 발견: {img_tag}")
        else:
            print("[DEBUG] 이미지 태그 없음")
        if img_tag and img_tag.get("src"):
            print(f"[DEBUG] 이미지 src: {img_tag['src']}")
            return img_tag["src"]
        return None
    except Exception as e:
        print(f"[DEBUG] 예외 발생: {e}")
        return None

def fetch_titles_and_links():
    response = requests.get(URL, headers=HEADERS, verify=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for a_tag in soup.select('a.baseList-title'):
        href = a_tag.get('href')
        span = a_tag.find('span')
        # span 텍스트가 없는 경우 제외
        if not span or not span.get_text(strip=True):
            continue
        span_text = span.get_text(strip=True)
        # 상대경로일 경우 절대경로로 변환
        if href and not href.startswith('http'):
            href = "https://www.ppomppu.co.kr/zboard/" + href
        img_href = fetch_image_from_board(href)
        results.append((href, span_text, img_href))
    return results

if __name__ == "__main__":
    items = fetch_titles_and_links()
    for idx, (href, text, img_href) in enumerate(items, 1):
        print(f"{idx}: {text}\n   {href}")
        if img_href:
            print(f"   이미지: {img_href}")
        else:
            print("   이미지 없음")