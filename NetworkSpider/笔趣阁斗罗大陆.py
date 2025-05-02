import requests
from lxml import etree

url='https://www.zibq.cc/html/45765/7.html'

# 伪装请求头
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
# 开始前先清空文件内容
open('斗罗大陆.txt','w',encoding='utf-8')

while True:
    # 用来判断是否是最后一页
    if url=='https://www.zibq.cc/html/45765':
        break

    # 获取html源码
    resp=requests.get(url,headers=headers)

    # 重新编码，防止乱码
    resp.encoding='utf-8'

    # 将获取的html内容转化为树形来处理
    e=etree.HTML(resp.text)

    # 获取小说内容和标题
    content=e.xpath("//div[@class='Readarea ReadAjax_content']")[0]

    # 把标题两端的空格删掉
    title=e.xpath("string(//div[@class='content']/h1)").strip()

    # 用来存储处理后的文本行
    lines=[]

    # 用来遍历content元素下所有文本节点和br标签
    for element in content.xpath(".//text() | .//br"):
        # 如果当前元素是否为字符串
        if isinstance(element, str):
            # 清理全角空格和首尾空格
            cleaned = element.replace('\u3000', ' ').strip()
            # 如果处理后的元素不为空，就加入到lines中
            if cleaned:
                lines.append(cleaned)
        # 如果当前元素是br标签
        else:
            # lines换行
            lines.append('\n')

    # 每章节的最后六句是广告，不需要收录
    lines=lines[:-6]

    # 将lines中的元素合并为一个字符串
    formatted_content = ''.join(lines)

    # 将连续的空行合并成一个
    formatted_content = formatted_content.replace('\n\n', '\n')

    # 去除每行首尾的空格，并过滤掉空行
    formatted_content = '\n'.join(
        [line.strip() for line in formatted_content.split('\n') if line.strip()]
    )

    # 将连续多个换行合并为两个换行，保持段落间距
    while '\n\n\n' in formatted_content:
        formatted_content = formatted_content.replace('\n\n\n', '\n\n')

    # 更新下一章的地址，手动补全前面的地址
    url=f'https://www.zibq.cc{e.xpath("//div[@class='Readpage pagedown']//a[@id='pb_next']/@href")[0]}'

    # 用于提示爬取进度
    print(title+' 已获得')

    # 把整理好的文本写入到txt文档中
    with open('斗罗大陆.txt','a',encoding='utf-8') as f:
        f.write(title+'\n\n'+formatted_content+'\n\n')