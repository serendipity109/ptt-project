# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import mysql.connector

# class PttPipeline:
#     def open_spider(self, spider):
#         self.conn = mysql.connector.connect(
#           host = "127.0.0.1",
#           user = "Kris",
#           password = "wowo0825",
#           database = "crawler",
#           )
#         self.cur = self.conn.cursor()
#         self.cur.execute("CREATE TABLE if not exists ptt(title VARCHAR(255), author VARCHAR(255), day VARCHAR(255),url VARCHAR(255))  ENGINE=InnoDB CHARSET=utf8")

#     def close_spider(self, spider):
#         self.conn.commit()
#         self.conn.close()

#     def process_item(self, item, spider):
#         self.cur.execute("INSERT INTO ptt(title, author, day, url) VALUE (%s, %s, %s, %s)" , (item['title'], item['author'], item['date'], item['url']))
#         return item


class PTTPipeline(object):
    def process_item(self, item, spider):
        return item