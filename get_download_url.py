# 适用网站https://www.993dy.com/
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import sys

def movie(url):
	s = requests.Session()	#会话保持
	response = s.get(url)	#r = requests.get(url)
	'''
	#beautifulesoup获取script内容
	#soup = BeautifulSoup(response.text, "html.parser")
	pattern = re.compile(r'var downurls="(.*?)";',re.MULTILINE | re.DOTALL)	#DOTALL正则中的点（.）能够匹配换行符（\n）
	script = soup.find("script",text=pattern)
	script = str(script)
	'''
	strscript = re.findall(r'var downurls="(.*?)";',str(response.text))[0].split('#')
	# xpath获取标题
	html = etree.HTML(response.text)	# 获取文本r.content
	title = html.xpath('/html/body/div[4]/div[3]/div[1]/div[2]/h1/text()')[0] #xpath后添加/text()可获取文本
	
	# 写入txt
	print(title)
	f = open("move.txt","a+", encoding = "utf-8")
	f.write(title + '\n')
	f.flush()	# 刷新缓冲区,就是立即写入文件，不写刷新就是关闭才能写入文件
	'''
	with open("move.txt", "a+", encoding = "utf-8") as f:
		f.write(title)
		f.write('\n')
	'''
	#strscript.pop() #弹出最后一个元素，因为用#分割完后最后一个元素为空
	for i in strscript[:-1]:
		try:
			print(i.split('$')[1])
			f.write(i.split('$')[1] + '\n')
			f.flush()
		except:
			pass
	f.write('\n')
	f.close()
	print("Finish！")

if __name__ == "__main__":
	if len(sys.argv)!=2:
		print("Usage: python " + sys.argv[0] + " URL")
	else:
		movie(sys.argv[1])