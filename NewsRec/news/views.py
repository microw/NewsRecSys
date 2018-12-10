# -*- coding: utf-8 -*-
from django.http import JsonResponse
from news.models import new,cate

# 获取每篇新闻的请求接口
def one(request):
    newid = request.GET.get("newid")
    newone = new.objects.filter(new_id=newid)[0]
    result = {
        "new_id": newone.new_id,
        "new_title": newone.new_title,
        "new_time": newone.new_time,
        "new_content": str(newone.new_content),
        "new_seenum": newone.new_seenum,
        "new_disnum": newone.new_disnum,
        "new_cate": newone.new_cate.cate_name
    }
    return JsonResponse(result)

# 获取新闻的所属类别
def cates(request):
    cateslist = cate.objects.all()
    result = dict()
    result["data"]=list()
    for cateone in cateslist:
        result["data"].append({
            "cate_id":cateone.cate_id,
            "cate_name":cateone.cate_name
        })
    return JsonResponse(result)