<template>
    <!--index.wxml-->
    <div class="container1">
        <div class="header">
            <div class="headertitle">
                <span class="text-title">{{header.title}}</span>
            </div>
            <div class="headerinfo">
                <span class="text-info">{{header.info}}</span><br>
                
            </div>
            <div class="headerlabel">
                
                <div :class="{'tagbox':nowpage!=index,'tagchangebox':nowpage==index}"  v-for="(label,index) in header.pages" :key='index' @click="changeDorm(index)">{{label}}</div>
            
            </div>
        </div>
        <!-- <v-touch v-on:swipeleft="onSwipeLeft" v-on:swiperight="onSwipeRight" > -->
        <div class="main">
              
              <template v-if="nowpage==0">
                
              <div class="ration-search">
                <div class="ration">
                  
                    <label style="font-size">宿舍楼：</label>
                    <select v-model="nowdoem" @change="bindPickerChange">
                        <option v-for="(item,index) in labels" :key="index">{{item.name}}</option>
                    </select><br>
                </div>
                <div class="search">
                    <input class="search-input" placeholder="Search..." v-model="search" @keyup.enter="searchFuc(search)"/>  
                    <!-- <icon class="searchcion" size='20' type='search'></icon> -->
                    <!-- <img src="https://s3.ax1x.com/2020/12/26/rhxQdU.png" style="width:8%;height:100%;"> -->
                </div>
              </div>
              
              <template v-if="!isloading&&!iserror">
              <div class="list">
              <template v-if="westlist.length != 0">
              <div class="list-left-right">
                  <div class="itembox" v-for="(item,index) in westlist" :key="index" :style="[{'border-top-color':item.status=='using'?'#F03029':'#59B8F8'},{'background-color':item.status=='using'?'rgba(255,0,0,0.3)':''}]">
                  <div class="imgbox">
                      <template v-if="item.status=='using'">
                      <img src="https://s1.ax1x.com/2020/10/27/BQzaIs.png" style="width:100%;height:100%;"/>
                      </template>
                      <template v-else>
                      <img src="https://s3.ax1x.com/2020/12/25/rWq6Rf.png" style="width:100%;height:100%;"/>
                      </template>
                  </div>
                  <div class="item-location">{{item.location}}</div>
                  <div class="item-info">
                      
                      <div v-if="item.status=='using'">工作状态:工作中</div>
                      <div v-else>工作状态:空闲</div>
                      <div v-if="item.remainTime!='-1'">剩余时间:{{item.remainTime}}分钟</div>
                      <div v-else>剩余时间:未知</div>
                      <div>洗衣机牌子:{{item.belong}}</div>
                  </div>
                  </div>
          
              </div>
              <div class="list-left-right">
                  <div class="itembox" v-for="(item,index) in eastlist" :key="index" :style="[{'border-top-color':item.status=='using'?'#F03029':'#59B8F8'},{'background-color':item.status=='using'?'rgba(255,0,0,0.3)':''}]">
                  <div class="imgbox">
                      <template v-if="item.status=='using'">
                      <img src="https://s1.ax1x.com/2020/10/27/BQzaIs.png" style="width:100%;height:100%;"/>
                      </template>
                      <template v-else>
                      <img src="https://s3.ax1x.com/2020/12/25/rWq6Rf.png" style="width:100%;height:100%;"/>
                      </template>
                  </div>
                  <div class="item-location">{{item.location}}</div>
                  <div class="item-info">
                    <div v-if="item.status=='using'">工作状态:工作中</div>
                      <div v-else>工作状态:空闲</div>
                      <div v-if="item.remainTime!='-1'">剩余时间:{{item.remainTime}}分钟</div>
                      <div v-else>剩余时间:未知</div>
                      <div>洗衣机牌子:{{item.belong}}</div>
                  </div>
                  </div>
              </div>
              </template>
              <template v-else>
                  <div style="font-size:5vmin;color:red;margin:0 auto;text-align:center;">{{errormsg}}</div>
              </template>
              </div>
              </template>
          </template>
        <template v-else-if="nowpage==1">
            <div class="feedback">
                <textarea class="feedbacktext"
                    placeholder="意见反馈......" v-model="inputText" @input="changeVal">
                </textarea>

            <button @click="submitFeedback"  class="feedbutton" >提交</button>
            </div>
        </template>
        <template v-else>
            <div class="more">敬请期待！</div>
        </template>
        <template v-if="isloading">
                <vue-loading type="bars" color="#d9544e" :size="{ width: '10vmin', height: '10vmin' }"></vue-loading>
        </template>
        </div>
        <!-- </v-touch> -->
        <div class="footer">
            
            <span>xWash团队</span>
                @2020-
            <br><span>联系我们：495572661@qq.com</span>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
// import vueLoading from 'vue-loading-template'
export default {
  name: 'Index',
    
  data () {
    return {
        header:{
            title:"xWash",
            info:"xWash（衣闲）为大家免费提供洗衣机工作情况",
            pages:["主页","反馈","更多"],
            warn:"因为某种神秘力量，有时候苏打校园的状态处于不可观测状态",
        },
        labels:[{name:"东四",url:""},{name:"东十二",url:""},{name:"东十三",url:""},
        {name:"东十四",url:""},{name:"东十九",url:"/api/all"},{name:"西二",url:""},{name:"西三",url:""},{name:"西五",url:""}],
        search:"",
        nowdoem:"东十九",
        westlist:[],
        eastlist:[],
        nowpage:0,
        isloading:true,
        iserror:false,
        inputText:"",
        errmsg:"",
        errormsg:"抱歉！暂时不支持该宿舍楼",
    }
  },
  mounted(){
        var that=this
        axios.get('/api/all',{       
        timeout:3000
        }).then(function(res){
          console.log(res)
            if(res.status==200){
                var obj=res.data;
                console.log(obj)
                that.westlist=res.data.slice(6,12)
                that.eastlist=res.data.slice(0,6)
                that.iserror=false
            }else{
       
                that.iserror=true
                that.errmsg=res.message
            }
            that.isloading=false
        }).catch(function (error) {
            that.iserror=true
            that.errmsg="500服务器连接超时"
            that.isloading=false
        });
       this.$notify({
          title: '温馨提示',
          message: this.header.warn,
          type: 'warning',
          //position: 'bottom-right',
          offset: 50,
          duration:8000,
         
        });
    },
  methods:{
      changeDorm:function(idx){//切换主页
        console.log(idx)
        this.nowpage=idx
        
    },
    bindPickerChange:function(e){//选择宿舍楼
        
        let index = e.target.selectedIndex
        console.log("index",index)
        let url = this.labels[index].url
        console.log("url",url)
        if(url==""){
            this.westlist=[]
            this.eastlist=[]
            return
        }
    
        this.getworkMsg(url)
    },
    changeVal:function (val) {//反馈意见
        //this.inputText = val.target.innerText;
        console.log(this.inputText)
    },
    submitFeedback:function () {//提交反馈
        alert("抱歉！该功能尚未完善");
        return
        if(this.inputText==""){
            
            alert("反馈内容不能为空哦！")
        }

    },
    searchFuc:function(e) {
        alert("抱歉！搜索功能尚未完善");
        return
        if(e==""){
            
            alert("搜索内容不能为空哦！")
        }
    },
    getworkMsg:function(url) {
      let that = this
      that.isloading=true,
      that.iserror=false,
      console.log("getworkMsg")
        axios.get(url,{       
        timeout:3000
        }).then(function(res){
            if(res.status==200){
                var obj=res.data;
                that.westlist=res.data.slice(6,12)
                that.eastlist=res.data.slice(0,6)
                that.iserror=false
            }else{
       
                that.iserror=true
                that.errmsg=res.message
            }
            that.isloading=false
        }).catch(function (error) {
            that.iserror=true
            that.errmsg="500服务器连接超时"
            that.isloading=false
        });
    },
    onSwipeLeft: function () {//左滑动
      if(this.nowpage>0){
        this.nowpage=this.nowpage-1;
      }
    },
 
    onSwipeRight: function () {//右滑动
      if(this.nowpage<2){
        this.nowpage=this.nowpage+1;
      }
    },
    
        

  }
}
</script>

<style scoped>
    /**index.wxss**/
.container1{

  font-family:"Comic Sans MS","幼圆","黑体","sans-serif";
  
}
.header{
   color:  rgb(54, 167, 243);
  background-color: rgb(89, 184, 248);
  height: 48vmin;
  width: 100%;
  border-top:1px solid #fcf8f8;
  color: #ffffff;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;

}
.text-title{
  font-size: 7vmin;
}
.text-info{
 
  font-size: 4vmin;
}
.headerlabel{
  margin-top: 6vmin;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: space-around;
  flex-wrap: wrap;
}
.tagbox{
  width: 16vmin;
  height: 7vmin;
  background-color: #ffffff;
  border-radius: 25px;
  color: #000000;
  font-size: 4vmin;
  margin-top: 15px;
  margin-left: 15px;
}
.tagchangebox{
    width: 16vmin;
    height: 7vmin;
    background-color: rgb(54, 167, 243);
    border-radius: 25px;
    color: #ffffff;
    font-size: 4vmin;
    margin-top: 15px;
    margin-left: 15px;
}
.main{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 80%;
  margin: 0 auto;
}
.ration-search{
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.ration{
  font-size: 4vmin;
  display: flex;
  flex-direction: row;
}
option:hover {
  background:#666;
}
select {
  display:flex;
  flex-direction: column;
  position:relative;
  height:6vmin;
  font-size: 4vmin;
  font-family:"Comic Sans MS","幼圆","黑体","sans-serif";
  color: #646161;
  border: none;
  outline: none;
}

option {
  font-family:"Comic Sans MS","幼圆","黑体","sans-serif";
  font-size: 5vmin;
  padding:0 30px 0 10px;
  min-height:40px;
  display:flex;
  align-items:center;
  background:rgb(177, 174, 174);
  border-top:#222 solid 1px;
  position:absolute;
  top:0;
  width: 100%;
  pointer-events:none;
  order:2;
  z-index:1;
  transition:background .4s ease-in-out;
  box-sizing:border-box;
  overflow:hidden;
  white-space:nowrap;
  color: #646161;
}
select:focus option {
  position:relative;
  pointer-events:all;
}
.search{
  width: 30%;
  display: flex;
  flex-direction: row;
  border: 1px solid #d0d0d0;  
  border-radius: 20px; 
  height: 5vmin;
}
.search-input{
  text-align: left;
  font-size: 4vmin;
  border: none!important;
  outline:none;
  width: 80%;
  margin-left: 2vmin;
}
.list{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 5vmin;
}
.list-left-right{
  width:45%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  
}
.doemstyle{
  color: #818080;
}
.itembox{
  width: 100%;
  height: 48vmin;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 10px;
  border-top:8px solid #000000;
  box-shadow:0px 0px 20px #d0d0d0;
  margin-top: 30px;

}
.itemboxusing{
  background: rgba(255,0,0,0.3);
}
.item-location{
  margin-top: 10px;
  font-size: 4vmin;
  text-align: center;
  
}
.item-info{
  width: 70%;
  color: #7a7878;
  font-size: 3vmin;
  text-align: center;
  margin:0 auto;
  margin-top: 1.5vmin;
}
.imgbox{
  width: 14vmin;
  height: 14vmin;
  margin: 0 auto;
}
.feedback{
  width: 100%;
  margin-top:50px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.feedbacktext{
    margin: 0 auto;
    border-radius:1vmin;
    background-color:rgb(245, 239, 239);
    width: 90%;height: 50vmin;
    font-size: 5vmin;
    padding: 10px;resize: none;
    outline: none;
}
.feedbutton{

    margin: 0 auto;
    margin-top: 5vmin;
    width: 50vmin;
    height: 8vmin;
    background-color: rgb(89, 184, 248);
    
    color: #ffffff;
    font-size: 3vmin;
    border: none;
    border-radius: 2vmin;
    outline: none;
}
.more{
    margin-top:50px;
    text-align: center;
    font-size: 5vmin;
}
.footer{

  margin: 0 auto;
  margin-top:50px;
  width:100%;
  height:20px;
  text-align: center;
  color: #646161;
  font-size: 3.5vmin;
}
.error{
  margin: 0 auto;
  font-size: 5vmin;
  color:#f03029;
  text-align: center;
  margin-top:5vmin;

}

</style>
