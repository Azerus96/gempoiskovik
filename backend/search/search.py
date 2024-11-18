from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from search.elasticsearch_config import ELASTICSEARCH_HOST

app = Flask(__name__)
es = Elasticsearch([ELASTICSEARCH_HOST])

@app.route('/search', methods=['GET'])
def search():
    url = request.args.get('url')
    query = request.args.get('query')

    body = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"content": query}},
                    {"match": {"url": url}}
                ]
            }
        }
    }

    res = es.search(index="pages", body=body)
    results = [hit["_source"]["content"] for hit in res['hits']['hits']]
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
