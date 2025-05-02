import requests
from lxml import etree

url='https://www.zibq.cc/html/45765/7.html'

# 伪装请求头
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

while True:
    # 最后一页
    if url=='https://www.zibq.cc/html/45765':
        break

    # 获取html源码
    resp=requests.get(url,headers=headers)

    # 重新编码
    resp.encoding='utf-8'

    # 将获取的html内容转化为树形来处理
    e=etree.HTML(resp.text)

    # 获取小说内容和标题
    content=e.xpath("//div[@class='Readarea ReadAjax_content']")[0]
    title=e.xpath("string(//div[@class='content']/h1)").strip()

    lines=[]
    for element in content.xpath(".//text() | .//br"):
        if isinstance(element, str):  # 处理文本节点
            # 清理全角空格和首尾空格
            cleaned = element.replace('\u3000', ' ').strip()
            if cleaned:
                lines.append(cleaned)
        else:  # 处理<br>标签
            lines.append('\n')  # 每个<br>换一行
    # 合并文本并优化换行
    formatted_content = ''.join(lines)
    formatted_content = formatted_content.replace('\n\n', '\n')  # 合并连续空行
    formatted_content = '\n'.join(
        [line.strip() for line in formatted_content.split('\n') if line.strip()]
    )
    # 将连续多个换行合并为两个换行（段落间距）
    while '\n\n\n' in formatted_content:
        formatted_content = formatted_content.replace('\n\n\n', '\n\n')

    # 更新下一章的地址
    url=f'https://www.zibq.cc{e.xpath("//div[@class='Readpage pagedown']//a[@id='pb_next']/@href")[0]}'
    print(title)
    with open('斗罗大陆.txt','a',encoding='utf-8') as f:
        f.write(title+'\n\n'+formatted_content+'\n\n')