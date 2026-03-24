import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://aagag.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_titles():
    response = requests.get(URL, headers=HEADERS, verify=False)  # 인증서 검증 끔
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    # id=content > div.clear:nth-child(1) > div:nth-child(1) > div:nth-child(2)
    target_div = soup.select_one("#content > div.clear:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
    if not target_div:
        print("대상 영역을 찾을 수 없습니다.")
        return []
    titles = [span.get_text(strip=True) for span in target_div.find_all("span", class_="title")]
    return titles

if __name__ == "__main__":
    titles = fetch_titles()
    for idx, title in enumerate(titles, 1):
        print(f"{idx}: {title}")