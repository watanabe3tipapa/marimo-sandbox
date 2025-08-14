import marimo

__generated_with = "0.14.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# NEWS SCRAPER""")
    return


@app.cell
def _():
    import requests
    from bs4 import BeautifulSoup
    import json
    from datetime import datetime

    class GoogleNewsScraper:
        def __init__(self):
            self.base_url = "https://news.google.com/rss"
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

        def get_news(self, country='JP', language='ja', max_results=10):
            """
            ニュースを取得する
            :param country: 国コード（例：JP）
            :param language: 言語コード（例：ja）
            :param max_results: 取得するニュース数
            :return: ニュース記事のリスト
            """
            url = f"{self.base_url}?hl={language}&gl={country}&ceid={country}:{language}"

            try:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item', limit=max_results)

                news_list = []
                for item in items:
                    news = {
                        'title': item.title.text,
                        'link': item.link.text,
                        'published_date': item.pubDate.text,
                        'source': item.source.text if item.source else None,
                        'description': item.description.text if item.description else None
                    }
                    news_list.append(news)

                return news_list

            except Exception as e:
                print(f"エラーが発生しました: {str(e)}")
                return []

    def save_news_to_file(news_list, filename):
        """
        ニュースをJSONファイルに保存する
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(news_list, f, ensure_ascii=False, indent=2)

    if __name__ == "__main__":
        scraper = GoogleNewsScraper()

        # 日本のニュースを取得
        news = scraper.get_news(country='JP', language='ja', max_results=10)

        # 結果を表示
        for i, article in enumerate(news, 1):
            print(f"\n記事 {i}:")
            print(f"タイトル: {article['title']}")
            print(f"リンク: {article['link']}")
            print(f"公開日: {article['published_date']}")
            print(f"ソース: {article['source']}")

        # 結果をJSONファイルに保存
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_news_to_file(news, f'news_{current_time}.json') 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---

    """
    )
    return


if __name__ == "__main__":
    app.run()
