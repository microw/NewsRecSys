import fetch from '../../axios/fetch'
//主页分类数据
export const getCateNewsData = (getdata) => fetch('/api/index/home/', getdata, 'get')
//主页分类
export const getCateData = () => fetch('/api/news/cates/', '', 'get')
