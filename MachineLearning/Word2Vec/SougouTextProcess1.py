# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:05:35 2016

@author: Shenjunling
"""
#<doc>
#<url>http://news.sohu.com/20120612/n345428229.shtml</url>
#<docno>c172394d49da2142-69713306c0bb3300</docno>
#<contenttitle>公安机关销毁１０余万非法枪支　跨国武器走私渐起</contenttitle>
#<content>中广网唐山６月１２日消息（记者汤一亮　庄胜春）据中国之声《新闻晚高峰》报道，今天（１２日）上午，公安机关２０１２年缉枪制爆专项行动“统一销毁非法枪爆物品活动”在河北唐山正式启动，１０万余只非法枪支、２５０余吨炸药在全国１５０个城市被统一销毁。黄明：现在我宣布，全国缉枪制爆统一销毁行动开始！随着公安部副部长黄明一声令下，大量仿制式枪以及猎枪、火药枪、气枪在河北唐山钢铁厂被投入炼钢炉。与此同时，在全国各省区市１５０个城市，破案追缴和群众主动上缴的１０万余支非法枪支被集中销毁，在全国各指定场所，２５０余吨炸药被分别销毁。公安部治安局局长刘绍武介绍，这次销毁的非法枪支来源于三个方面。刘绍武：打击破案包括涉黑、涉恶的团伙犯罪、毒品犯罪，还有从境外非法走私的枪支爆炸物。在销毁现场，记者看到了被追缴和上缴的各式各样的枪支。刘绍武：也包括制式枪，有的是军用枪、仿制的制式抢，还有猎枪、私制的火药枪等等。按照我国的枪支管理法，这些都是严厉禁止个人非法持有的。中国是世界上持枪犯罪的犯罪率最低的国家之一。中美联手破获特大跨国走私武器弹药案近日，中美执法部门联手成功破获特大跨国走私武器弹药案，在中国抓获犯罪嫌疑人２３名，缴获各类枪支９３支、子弹５万余发及大量枪支配件。在美国抓获犯罪嫌疑人３名，缴获各类枪支１２支。这是公安部与美国移民海关执法局通过联合调查方式侦破重大跨国案件的又一成功案例。２０１１年８月２５日，上海浦东国际机场海关在对美国纽约发往浙江台州，申报品名为扩音器（音箱）的快件进行查验时，发现货物内藏有手枪９支，枪支配件９件，长枪部件７件。经检验，这些都是具有杀伤力的制式枪支及其配件。这引起了公安部和海关总署的高度重视。公安部刑侦局局长刘安成：因为是从海关进口的货物中检查出来夹带，说明来源地是境外，或是说国外，这应该是一起特大跨国走私武器弹药的案件。上海市公安局和上海海关缉私局成立联合专案组，迅速开展案件侦查。专案组于８月２６日在浙江台州ＵＰＳ取件处将犯罪嫌疑人王挺（男，３２岁，台州市人）抓获。王挺交代，他通过一境外网站上认识了上家林志富，２００９年１１月以来，林志富长期居住美国，他通过互联网组建了一个走私、贩卖、私藏枪支弹药的群体，通过网络在国内寻找枪支弹药买家，并通过美国ＵＰＳ联邦速递公司将枪支弹药从纽约快递给多名类似王挺的中间人，再通过中间人发送给国内买家。此案中，犯罪分子依托虚拟网络进行犯罪交易，隐蔽性强，涉案人员使用的身份、地址、联系方式都是虚构的，侦查难度很大。刘安成说，此案体现了是新型犯罪，特别是现代犯罪的新特点。刘安成：他不受距离的限制、经常是跨国跨境，甚至是跨一个、数个、甚至数十个国家。这种犯罪手法的改变和新型犯罪的特点，要求我们各国警方充分合作。作者：汤一亮　庄胜春</content>
#</doc>
import numpy as np
import re
from jieba import analyse,posseg
import jieba
import os
#analyse.set_stop_words("G:/data/SougouNews/stopWords.txt")
analyse.set_stop_words("D:/data/SougouNews/stopwords/stop.txt")
jieba.load_userdict("D:/OneDrive/codes/python/Word2Vec/tfidf/userdict.txt")   

"""
,"x":0:标点
"""
def lineCut(line):
    line1=""
    filters={"nr":0,"ns":0,"nt":0,"m":0,"mq":0,"q":0,"qv":0,"qt":0}
    tmp=posseg.cut(line)
    for w in tmp:
        ab=w.flag.encode("utf-8")      
        if (filters.has_key(ab)): 
#            print ab
            continue
        line1=line1+" "+w.word.encode("utf-8")
#        print w.word,ab
    return line1.strip()


#basePath="D:/data/SougouNews"
#f1Path=basePath+"/news_tensite_xml.dat"
##f1Path=basePath+"/1.txt"
#f2Path=basePath+"/sougouNewsCut.txt"
#f3Path=basePath+"/sougouNewsContent.txt"
#
#f1=open(f1Path,"rb")
#f2=open(f2Path,"w")
#f3=open(f3Path,"w")
#line =f1.readline()
#n=0
#strinfo = re.compile("\\.|。|，|,|\"|“|”|‘|’|；|：|！|、|| |《|》|<|>|…|:|;|？|\\n")
#
#
#while(line!=""):
#    line=line.strip()
#    if line.find("<doc>",0,20)==0:
#        print n
#        n=n+1
#    elif line.find("<url>",0,20)==0:
#        line=line[5:-6]
#        f2.write(line+"\t")
#    elif line.find("<docno>",0,20)==0:
#        line=line[7:-8]
#        f2.write(line+"\t")
#    elif line.find("<contenttitle>",0,20)==0:
#        line=line[14:-15]
#        title=line
#        line = strinfo.sub('',line)
#        line=lineCut(line)
##        f2.write(line.decode("utf-8")+"\t")
#        f2.write(line+"\t")
#    elif line.find("<content>",0,20)==0:
#        line=line[9:-10]
#        line = strinfo.sub('',line)
#        line=lineCut(line)
##        f2.write(line.decode("utf-8")+"\t")
#        if line.strip()!="":
#            f2.write(line)
#            if len(line)>20 and title.strip()!="":
#                f3.write(line+"\n")
#    elif line.find("</doc>",0,20)==0:
#        line=f1.readline()
#        f2.write("\n")
#        continue
#    line=f1.readline()

basePath="D:/data/SougouNews/SogouCA"
fileLists=os.listdir(basePath)

#f1Path=basePath+"/1.txt"
f2Path=basePath+"/sougouNewsCut1.txt"
f3Path=basePath+"/sougouNewsContent1.txt"
f2=open(f2Path,"w")
f3=open(f3Path,"w")

n=0
#strinfo = re.compile("\\.|。|，|,|\"|“|”|‘|’|；|：|！|、|| |《|》|<|>|…|:|;|？|\\n")
strinfo = re.compile("| |《|》|<|>|…|？|\\n")

for f1 in fileLists:
    print f1
    f1Path=basePath+"/"+f1
    f1=open(f1Path,"rb")
    line =f1.readline()
    while(line!=""):
        line=line.strip()
        if line.find("<doc>",0,20)==0:
            print n
            n=n+1
        elif line.find("<url>",0,20)==0:
            line=line[5:-6]
            f2.write(line+"\t")
        elif line.find("<docno>",0,20)==0:
            line=line[7:-8]
            f2.write(line+"\t")
        elif line.find("<contenttitle>",0,20)==0:
            line=line[14:-15]
            title=line
            line = strinfo.sub('',line)
            line=lineCut(line)
    #        f2.write(line.decode("utf-8")+"\t")
            f2.write(line+"\t")
        elif line.find("<content>",0,20)==0:
            line=line[9:-10]            
            line = strinfo.sub('',line)            
            line=lineCut(line)
    #        f2.write(line.decode("utf-8")+"\t")
            if line.strip()!="":
                f2.write(line)
                if len(line)>20 and title.strip()!="":
                    f3.write(line+"\n")
        elif line.find("</doc>",0,20)==0:
            line=f1.readline()
            f2.write("\n")
            continue
        line=f1.readline()
    f1.close()
f2.close()
f3.close()

