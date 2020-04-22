# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class IndianmoviecelebritiesPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("indanmoviescelebrities.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS celebrities_tb""")
        self.curr.execute("""create table celebrities_tb(
                        celebrity_name text,
                        celebrity_image_link text,
                        celebrity_role text,
                        celebrity_detail text
                        )""")



    def process_item(self, item, spider):
        self.store_db(item)
        
        return item
    def store_db(self,item):
        self.curr.execute("""insert into quotes_tb values (?,?,?,?)""",(
            item['celebrity_name'][0],
            item['celebrity_image_link'][0],
            item['celebrity_role'][0],
            item['celebrity_detail'][0]
        ))
        self.conn.commit()

