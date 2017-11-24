import csv
from konlpy.tag import Twitter
from konlpy.utils import pprint

#뉴스데이터 토큰화
def tokenize(postagger, news):

    for row in news:
        title = postagger.pos(row[0], stem=True, norm=True)
        article = postagger.pos(row[2], stem=True, norm=True)
        month = eval(row[3])
        date = eval(row[4])

        pprint(article.vocab().most_common(10))


        articleStrfied = ""
        for word in article:
            if word[1] not in ['Email','Punctuation', "Foreign"]:
                articleStrfied +=word[0]+word[1]+" "













#주별 빈출 키워드
nlp = Twitter()

news = csv.reader(open("4test.txt","r",encoding='utf-8'), delimiter='\t')

tokenize(nlp, news)



#키워드 데려오기



#주별 단어 스트링화



#주별 빈출 단어 추출




#월별 빈출 키워드



#월별 단어 스트링화



#월별 빈출 단어 추출



