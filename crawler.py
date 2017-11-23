from bs4 import BeautifulSoup
import time,requests,re,lxml
start_time = time.time()


def crawlBestReplysite():
    linkUrl_before = ""

    year = 2017
    urlFile = open('urls.txt', 'w', encoding="UTF-8")
    for month in range(1,13):
        for date in range(1,32):   #월일 별로 순환
            if month < 10:         #한자리수인 경우에 변환
                monthStr = "0" + str(month)
            else:
                monthStr = str(month)
            if date < 10:
                dateStr = "0" + str(date)
            else:
                dateStr = str(date)
            url = "http://media.daum.net/ranking/bestreply/?regDate="+str(year)+monthStr+dateStr

            try:
                sourceCode = requests.get(url)
                soup = BeautifulSoup(sourceCode.text, 'lxml')
                for link in soup.find_all("a", class_ ="link_txt"):
                    title = link.text
                    linkUrl = link.get("href")

                    if linkUrl == linkUrl_before:
                        continue

                    if not "http://v.media." in linkUrl: #링크가 뉴스인 경우만
                        continue
                    else:
                        linkUrl_before = linkUrl
                        sourceCodeNews = requests.get(linkUrl)
                        soupNews = BeautifulSoup(sourceCodeNews.text, 'lxml')
                        article = ""
                        for linkNews in soupNews.find_all("div", id="harmonyContainer"):
                            article += linkNews.text+" "
                        urlFile.write(title+"\t" + linkUrl + article +"\n")
            except Exception as ex:
                print(ex)
                continue
    urlFile.close()

crawlBestReplysite()