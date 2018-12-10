<template>
  <div class="recommonContain">
    <div class="reHeader">
      <div class="headTop">
        <img class="topLogo" src="../assets/img/logo.png" />
      </div>
      <ul class="headNav">
        <li v-for="item in cates" :key="item.cate_id" @click="getCateNews(item.cate_id)" :data-sign="item.cate_id" :class="isActive==item.cate_id ? 'navActive':''">{{item.cate_name}}</li>
      </ul>
    </div>
    <div class="mainContent">
      <div class="mainLeft">
        <ul class="leftContent">
          <li v-for="item in newsData.news" :key="item.new_id" @click="newsDesc(item.new_id)">
            <h3 class="newsTitle">
              {{item.new_title}}
              <span class="newsOther">{{item.new_time}}</span>
            </h3>
            <p class="newsContent">{{item.new_content}}</p>
          </li>
        </ul>
      </div>
      <div class="mainRight">
        <h3 class="hotTitle">{{hot_newsData.cate_name}}</h3>
        <ul class="rightContent">
          <li v-for="item in hot_newsData.news" :key="item.new_id">
            <span>{{item.new_title}}</span>
            <i>{{item.new_time}}</i>
          </li>
        </ul>
      </div>
    </div>
   </div>
</template>

<script>
import {getCateNewsData, getCateData} from '../assets/js/api'
export default {
  name: 'HelloWorld',
  data () {
    return {
      isActive: '1',
      newsData: {},
      hot_newsData: {},
      cates: []
    }
  },
  methods: {
    getCateNews: function (cateId) {
      let getdata = {}
      if (cateId === '2') {
        getdata = {
          cate: '2'
        }
        getCateNewsData(getdata).then((res) => {
          res.news.forEach((item) => {
            item.new_time = this.timeFormat(item.new_time)
          })
          this.hot_newsData = res
        }, (err) => {
          console.log(err)
        })
      } else {
        if (cateId) {
          getdata.cate = cateId
          this.isActive = cateId
        }
        getCateNewsData(getdata).then((res) => {
          res.news.forEach((item) => {
            item.new_time = this.timeFormat(item.new_time)
          })
          this.newsData = res
        }, (err) => {
          console.log(err)
        })
      }
    },

    getCates: function () {
      getCateData().then((res) => {
        res.data.forEach((item, index) => {
          if (item.cate_id === '2') {
            res.data.splice(index, 1)
          }
        })
        this.cates = res.data
      }, (err) => {
        console.log(err)
      })
    },

    newsDesc: function (newId) {
      this.$router.push({
        name: 'news',
        query: {newid: newId}
      })
    }
  },
  mounted () {
    this.getCates()
    this.getCateNews('1')
    this.getCateNews('2')
  }
}
</script>
<style lang="less" scoped>
  @baseColor:red;
  #ellies(@n){
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: @n;
    -webkit-box-orient: vertical;
  }
  .recommonContain{
    width: 100%;
    padding:2% 8%;
    box-sizing: border-box;
    .headNav{
      display:flex;
      justify-content:flex-start;
      align-items: center;
      background: #ddd;
      height:40px;
      li{
        display: inline-block;
        width:120px;
        padding:5px 15px;
        box-sizing: border-box;
        position: relative;
        text-align: center;
        cursor: pointer;
      }
      .navActive::after{
        content: " ";
        display: block;
        position: absolute;
        bottom: -6px;
        width: 30%;
        left: 50%;
        border-bottom: 2px solid @baseColor;
        margin-left: -15%;
      }
    }
    .mainContent{
      width: 100%;
      display: flex;
      box-sizing: border-box;
      .mainLeft{
        width: 60%;
        box-sizing: border-box;
        .leftContent{
          li{
            width: 80%;
            margin:2% 5%;
            padding:1% 3%;
            border:1px solid #666;
            border-radius: 5px;
            box-shadow: 5px 5px 10px #999;
            cursor: pointer;
            .newsTitle{
              font-size: 16px;
              margin-bottom: 10px;
              color: #333;
              line-height: 20px;
              span{
                font-size: 12px;
              }
            }
            .newsContent{
              font-size: 14px;
              line-height: 17px;
              color:#666;
              #ellies(2)
            }
            &:hover{
              padding:2% 3%;
            }
          }
        }
      }
      .mainRight{
        flex: 1;
        &>h3{
          width:100%;
          padding: 10px;
          margin-top:15px;
          background: #dfdfdfdf;
          vertical-align: middle;
          box-sizing: border-box;
        }
        .hotTitle{
          font-size: 18px;
          padding: 5px;
          color: #333;
        }
        .rightContent{
          padding: 5px;
          li{
            width: 100%;
            color: #666;
            height:16px;
            line-height: 16px;
            display: flex;
            margin-bottom: 10px;
            justify-content: space-around;
            cursor: pointer;
            font-size: 14px;
            span{
              #ellies(1);
              width: 70%;
            }
            i{
              font-size: 12px;
              #ellies(1);
              width: 30%;
            }
            &:hover{
              font-size: 15px;
              color:#000
            }
          }
        }
      }
    }
  }
</style>
