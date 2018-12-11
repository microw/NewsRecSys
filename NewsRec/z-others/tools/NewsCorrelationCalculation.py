# -*- coding: utf-8 -*-
"""
 Author: thinkgamer
 Desc：每个类型下新闻的相似度计算
"""
import os

class Correlation:
    def __init__(self, file):
        self.file = file
        self.news_tags = self.loadData()
        self.news_cor_list = self.getCorrelation()

    # 加载数据
    def loadData(self):
        print("开始加载文件数据：%s" % self.file)
        news_tags = dict()
        for line in open(self.file, "r", encoding="utf-8").readlines():
            try:
                newid, newtags = line.strip().split("\t")
                news_tags[newid] = newtags
            except:
                pass
        return news_tags

    # 计算相关度
    def getCorrelation(self):
        news_cor_list = list()
        for newid1 in self.news_tags.keys():
            id1_tags = set(self.news_tags[newid1].split(","))
            for newid2 in self.news_tags.keys():
                id2_tags = set(self.news_tags[newid2].split(","))
                if newid1 != newid2:
                    print( newid1 + "\t" + newid2 + "\t" + str(id1_tags & id2_tags) )
                    cor = ( len(id1_tags & id2_tags) ) / len (id1_tags | id2_tags)
                    if cor > 0.0:
                        news_cor_list.append(newid1+","+newid2+","+format(cor,".2f"))
        return news_cor_list

    # 将相关度写入文件
    def writeToFile(self,file):
        fw = open("./../data/correlation/%s" % file, "w")
        fw.write("\n".join(self.news_cor_list))
        fw.close()
        print("文件 %s 的相关度计算写入完毕。" % file)

if __name__ == "__main__":
    # 原始数据文件路径
    original_data_path = "./../data/keywords/"
    files = os.listdir(original_data_path)
    for file in files:
        print("开始计算文件 %s 下的新闻相关度。" % file)
        cor = Correlation(original_data_path + file)
        cor.writeToFile(file)
    print("\n相关度计算完毕，数据写入路径 z-othersd/data/correlation")

    # 分析
    fileid = 1
    id = "100005"
    _dict = dict()
    for line in open("./../data/correlation/%s.txt" % fileid, "r").readlines():
        id1, id2, cor = line.strip().split(",")
        if id1 == id:
            _dict[id2] = float(cor)
    print(sorted(_dict.items(), key=lambda k: k[1], reverse=True)[:10])

