 
 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymysql
from scrapy.exceptions import DropItem

class DangdangPipeline(object):
	# def __init__(self):
	# 	self.file=codecs.open(r"F:\python爬虫\dangdang.json","wb",encoding="utf-8")
	# 	self.conn=pymysql.connect(host="127.0.0.1",user='root',passwd="123456",db="lgwdb")
	# 	self.conn.query("CREATE TABLE dangdang(id CHAR(255) NOT NULL,name CHAR(255),price CHAR(255),comments CHAR(255),link CHAR(255))")
	# 	self.num=1
	def process_item(self, item, spider):
		print("开始保存到本地json文件以及mysql数据库中***************")
		for i in range(0,len(item["name"])):		
			name=item["name"][i]
			price=item["price"][i]
			comments=item["comments"][i]
			link=item["link"][i]
		# 	goods={"name":name,"price":price,"comments":comments,"link":link}
		# 	sql="insert into dangdang(id,name,price,comments,link) VALUES('"+str(self.num)+"','"+name+"','"+price+"','"+comments+"','"+link+"')"
		# 	self.num+=1
		# 	self.conn.query(sql)
		# 	self.conn.commit()
		# 	i=json.dumps(dict(goods),ensure_ascii=False)
		# 	line=i+"\n"
		# 	self.file.write(line)
		# print("成功！")	
		return item
#去重
class ItemDuplicatePipeline(object):
	def __init__(self):
		self.file=codecs.open(r"F:\python爬虫\dangdang.json","wb",encoding="utf-8")
		self.conn=pymysql.connect(host="127.0.0.1",user='root',passwd="123456",db="lgwdb")
		self.conn.query("CREATE TABLE dangdang1(id CHAR(255) NOT NULL,name CHAR(255),price CHAR(255),comments CHAR(255),link CHAR(255))")
		self.num=1
		self.name_set=set()
		# self.price_set=set()
		# self.comments_set=set()
		# self.link_set=set()
	def process_item(self,item,spider):
		for i in range(0,len(item["name"])):
			name=item["name"][i]
			# price=item["price"][i]
			# comments=item["comments"][i]
			# link=item["link"][i]
			print("开始去重！")
			if name in self.name_set:
				raise DropItem("去重成功！")
			self.name_set.add(name)
			goods={"name":name,"price":price,"comments":comments,"link":link}
			sql="insert into dangdang1(id,name,price,comments,link) VALUES('"+str(self.num)+"','"+name+"','"+price+"','"+comments+"','"+link+"')"
			self.num+=1
			self.conn.query(sql)
			self.conn.commit()
			i=json.dumps(dict(goods),ensure_ascii=False)
			line=i+"\n"
			self.file.write(line)
			print("成功！")	
			
		return item
	def close_spider(self,spider):
		self.file.close()
		self.conn.close()