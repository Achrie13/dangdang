from itemadapter import ItemAdapter
import mysql.connector


class DangdangPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="123123", database="book", port=3306
        )
        self.cursor = self.conn.cursor()
        if self.conn.is_connected():
            print("成功连接到数据库")
        else:
            print("no成功连接到数据库")

    def process_item(self, item, spider):
        insert_query = """
            INSERT INTO books (name, price, press, content) 
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(
            insert_query, (item["name"], item["price"], item["press"], item["content"])
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()