import csv
from konlpy.tag import Twitter
from konlpy.utils import pprint
from collections import Counter

#뉴스데이터 토큰화
def tokenize(postagger, news):
    monthTitle = []
    monthArticle = []

    for k in range(12):
        monthTitle.append("")
        monthArticle.append("")

    for row in news:
        month = eval(row[3])
        date = eval(row[4])


        monthTitle[month-1] += row[0]
        monthArticle[month-1] += row[2]


    for i in monthTitle:
        titlepos = postagger.pos(i, stem=True, norm=True)
        cnt = Counter(titlepos)
        pprint(cnt.most_common(10))


    for j in monthArticle:
        articlepos = postagger.pos(j, stem=True, norm=True)
        cnt2 = Counter(articlepos)
        pprint(cnt2.most_common(10))
'''
        for word in article:
            if word[1] not in ['Email','Punctuation', "Foreign"]:
                articleStrfied +=word[0]+word[1]+" "

        articleStrfied
'''



        #주별 빈출 키워드
nlp = Twitter()
news = csv.reader(open("urls.txt","r",encoding='utf-8'), delimiter='\t')
tokenize(nlp, news)



#키워드 데려오기



#주별 단어 스트링화



#주별 빈출 단어 추출




#월별 빈출 키워드



#월별 단어 스트링화



#월별 빈출 단어 추출



