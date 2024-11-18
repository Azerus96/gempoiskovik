from elasticsearch import Elasticsearch
from crawler.indexer.elasticsearch_config import ELASTICSEARCH_HOST

class ElasticsearchPipeline:
    def __init__(self):
        self.es = Elasticsearch([ELASTICSEARCH_HOST])

    def process_item(self, item, spider):
        self.es.index(index="pages", body={"url": item["url"], "content": item["content"]})
        return item
