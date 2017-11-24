from __future__ import print_function
from textrankr import TextRank

number=['1','2','3','4','5','6','7','8','9','0']
notinclude=["기자","뉴스"]
str=""

f= open("urls.txt","r")

while True:
    line =f.readline()
    if not line: break
    for i in range(0,len(line)-1):
        if (line[i]=='기' and line[i+1]=='자') or (line[i]=='뉴' and line[i+1]=="스") or (line[i]=='사' and line[i+1]=='진'):
            line=f.readline()
            break
    if not line: break  
    if len(line)>=10:
        if len(line)>=18 and line[-2] in number and line[-18] in number:
            title=line[0:-45]
            day=line[-18:-2]
            if str!="":
                # print(str)
                textrank=TextRank(str)
                print(textrank.summarize()+"\n\n")
            print("-----"+day+"-----")
            print(title+"\n")
            str=""
        else:
            str+=line
    

    
           

f.close()

