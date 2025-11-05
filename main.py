from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['POST'])
def notice():
    url = "https://game.naver.com/lounge/Trickcal/board/1"  # 공지 게시판
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    item = soup.select_one("ul.list_board li a")
    title = item.select_one("strong").text.strip()
    link = "https://game.naver.com" + item["href"]

    message = f"📢 트릭컬 최신 공지\n\n{title}\n{link}"

    return jsonify({
        "version": "2.0",
        "template": {"outputs": [{"simpleText": {"text": message}}]}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
