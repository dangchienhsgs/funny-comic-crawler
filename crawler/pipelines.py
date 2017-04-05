# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
import logging

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from sqlalchemy.orm import sessionmaker

from .models import ImageItem
from .models import db_connect, create_images_table

logger = logging.getLogger(__name__)


class MyImagesPipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, download_func, settings)

        # create engine
        logger.info("Create engine for database")
        engine = db_connect()
        create_images_table(engine=engine)
        self.session = sessionmaker(bind=engine)()

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_path'] = image_paths[0]
        id = self.hash_url(item['image_url'])

        record = ImageItem(id=id, title=item['title'], filename=item['image_path'], url=item['image_url'])
        self.session.add(record)
        self.session.commit()
        return item

    def hash_url(self, url):
        return hashlib.sha1(url.encode()).hexdigest()
