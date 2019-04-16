
# 股票数据定向爬虫 爬取文本到指定文件夹下的文件中
import os

# 股票数据定向爬虫，爬取文本到指定文件夹下的文件中


import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url, code='utf-8'):  # 参数code缺省值为‘utf-8’(编码方式)
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0  #
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})  # 用空格分开，得到股票名称

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='UTF-8') as f: # a 追加模式，也能写,在文件的末尾添加内容
                f.write(str(infoDict) + '\n')
                count = count + 1  #
                print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), end='')  # 动态显示进度，‘\r’实现光标移动，即为不换行的效果
        except:
            count = count + 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), end='')  # 动态显示进度，‘\r’实现光标移动，即为不换行的效果
            # traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    if os.path.isdir('D:\\test'):
        print("此文件夹已存在")
    else:
        os.makedirs('D:\\test')
    output_file = 'D:\\test\\date.txt' # 文件路径
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)



main()