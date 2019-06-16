import random
from dangdang.settings import UAPOOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class Uamid(UserAgentMiddleware):
	"""docstring for Uamid"""
	def __init__(self, user_agent=''):
		self.user_agent=user_agent
	def process_request(self,request,spider):
		thisua=random.choice(UAPOOL)
		print('*************************'+thisua)
		request.headers.setdefault('user-agent:',thisua)
