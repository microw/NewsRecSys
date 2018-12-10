#-*-coding:utf-8-*-
"""
 Author: thinkgamer
 Desc：不同预料库下的新闻关键词抽取-基于TFIDF
"""

import os
import xlrd
import jieba.analyse

class SelectKeyWord:
    def __init__(self,file):
        self.file = file
        self.news_dict = self.loadData()
        self.key_words = self.getKeyWords()

    # 加载数据
    def loadData(self):
        news_dict = dict()
        # 使用xlrd加载xlsx格式文件,返回一个table对象
        table = xlrd.open_workbook(self.file).sheets()[0]
        # 遍历每一行
        for row in range(1,table.nrows):
            # 将每一列返回为一个数组
            line = table.row_values(row, start_colx=0, end_colx=None)
            new_id = int(line[0])
            news_dict.setdefault(new_id,{})
            news_dict[new_id]["tag"] = line[1]
            news_dict[new_id]["title"] = line[5]
            news_dict[new_id]["content"] = line[-1]
        return news_dict

    # 调用结巴分词获取每篇文章的关键词
    def getKeyWords(self):
        news_key_words = list()
        for new_id in self.news_dict.keys():
            # allowPOS 提取地名、名词、动名词、动词
            keywords = jieba.analyse.extract_tags(self.news_dict[new_id]["title"]+self.news_dict[new_id]["content"],withWeight=True,allowPOS=('ns', 'n', 'vn', 'v'))
            kws = list()
            for kw in keywords:
                kws.append( kw[0] +":" +str(kw[1]) )
            news_key_words.append(str(new_id) + '\t'+",".join(kws) )
        return news_key_words

    # 将关键词获取结果写入文件
    def writeToFile(self,file):
        fw = open("./../data/keywords/%s.txt" % file.split("-")[0],"w")
        fw.write("\n".join(self.key_words))
        fw.close()
        print("文件 %s 的关键词写入完毕。" % file)

if __name__ == "__main__":
    # 原始数据文件路径
    original_data_path = "./../data/original/"
    files = os.listdir(original_data_path)
    for file in files:
        print("开始获取文件 %s 下的关键词。" % file)
        skw = SelectKeyWord(original_data_path + file )
        skw.writeToFile(file)
    print("\n关键词获取完毕，数据写入路径 z-othersd/data/keywords")