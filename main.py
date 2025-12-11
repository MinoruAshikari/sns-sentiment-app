# main.py  — テンプレートを使わない1ファイル完結版

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from sentiment import analyze_sentiment

app = FastAPI()


def render_page(text: str = "", result: dict | None = None) -> str:
    """HTMLをそのまま文字列で組み立てる"""
    html = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
      <meta charset="UTF-8" />
      <title>SNSコメント感情分析ツール</title>
    </head>
    <body>
      <h1>SNSコメント感情分析ツール</h1>
      <p>Twitter / Radiotalk / YouTube のコメントを貼り付けて、ざっくりポジ・ネガをチェックできます。</p>
      <form method="post">
        <textarea name="text" rows="8" cols="60" placeholder="ここにコメントを貼り付けてください。">""" + (
        text or ""
    ) + """</textarea>
        <br>
        <button type="submit">分析する</button>
      </form>
    """

    if result is not None:
        pos = "、".join(result.get("pos_hits") or []) or "なし"
        neg = "、".join(result.get("neg_hits") or []) or "なし"
        html += f"""
        <hr>
        <h2>分析結果</h2>
        <p>判定：{result.get("label")}（スコア: {result.get("score")}）</p>
        <p>ポジティブ単語のヒット：{pos}</p>
        <p>ネガティブ単語のヒット：{neg}</p>
        """

    html += """
    </body>
    </html>
    """
    return html


@app.get("/", response_class=HTMLResponse)
async def form_get() -> HTMLResponse:
    """最初に開いたときの画面"""
    return HTMLResponse(content=render_page())


@app.post("/", response_class=HTMLResponse)
async def form_post(text: str = Form(...)) -> HTMLResponse:
    """フォームから送られたテキストを分析して表示"""
    result = analyze_sentiment(text)
    return HTMLResponse(content=render_page(text=text, result=result))
