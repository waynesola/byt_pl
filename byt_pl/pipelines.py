# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import BytPlItem
import sqlite3


class BytPlPipeline(object):
    def process_item(self, item, spider):
        if item.__class__ == BytPlItem:  # 此句非必要，在多个items时可能需要用到
            # 数据库名即目录存放地址
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            # 表名是 byt_pl
            sql = "insert into byt_pl(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        return item
