# sentiment.py

# ポジティブ・ネガティブに使いそうな単語をとりあえず登録
POSITIVE_WORDS = [
    "最高", "嬉しい", "楽しい", "素晴らしい", "ありがとう",
    "好き", "尊敬", "助かる", "感謝", "良い", "よかった"
]

NEGATIVE_WORDS = [
    "最悪", "ムカつく", "嫌い", "うざい", "だるい", "無理",
    "つらい", "疲れた", "死ね", "ゴミ", "クソ", "やめろ",
    "最悪だ", "腹立つ"
]


def analyze_sentiment(text: str) -> dict:
    """
    とてもシンプルなルールベースの感情分析。
    - ポジ単語が多ければポジティブ
    - ネガ単語が多ければネガティブ
    - 同じくらい or どちらもないなら中立
    """
    if not text:
        return {
            "label": "中立",
            "score": 0,
            "pos_hits": [],
            "neg_hits": [],
        }

    score = 0
    pos_hits = []
    neg_hits = []

    for w in POSITIVE_WORDS:
        if w in text:
            score += 1
            pos_hits.append(w)

    for w in NEGATIVE_WORDS:
        if w in text:
            score -= 1
            neg_hits.append(w)

    if score > 0:
        label = "ポジティブ"
    elif score < 0:
        label = "ネガティブ"
    else:
        label = "中立"

    return {
        "label": label,
        "score": score,
        "pos_hits": pos_hits,
        "neg_hits": neg_hits,
    }


if __name__ == "__main__":
    # コマンドラインからテストするとき用
    sample = input("コメントを入力してください: ")
    result = analyze_sentiment(sample)
    print(result)
