import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.qgsydw.com/qgsydw/examinfo.html?channel=bmsj'

# 发送HTTP请求并获取响应
response = requests.get(url)
response.encoding = 'utf-8'

# 使用BeautifulSoup解析响应内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到文章列表
article_list = soup.select('div.list ul li')

# 用一个空列表来保存结果
result_list = []

# 遍历文章列表并提取标题、发布时间和链接
for article in article_list:
    title = article.select_one('a').text
    publish_time = article.select_one('span').text
    link = article.select_one('a')['href']
    
    # 将提取的数据添加到结果列表中
    result_list.append({
        'title': title,
        'publish_time': publish_time,
        'link': link
    })

# 将结果保存到JSON文件中
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False)
