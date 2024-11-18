from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    url = data.get('url')
    try:
        subprocess.run(['scrapy', 'crawl', 'site', '-a', f'start_urls={url}'], cwd='./crawler/crawler')
        return jsonify({"message": "Crawling started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
