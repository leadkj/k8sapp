<template>
	<view class="goods">	
		<goods-list :goods="goods"></goods-list>
		<view class="dixian" v-if="flag">-----我是有底线的-----</view>
		<view class="nav-goods">
			<uni-goods-nav :fill="true"  :options="options" :buttonGroup="buttonGroup"  @click="onClick" @buttonClick="buttonClick" />
		</view>
	</view>
	
</template>

<script>
	import uniGoodsNav from '@/components/uni-goods-nav/uni-goods-nav.vue'
	import goodsList from '../../components/goods-list/goods-list.vue'
	export default {
		components: {uniGoodsNav},
		data() {
			return {
				goods:[
					{
						id:1,
						img_url:"../../static/icon/n2.png",
						sell_price:1499,
						market_price:2000,
						title:"华为p32 4G 256G"
					},
					{
						id:2,
						img_url:"../../static/icon/n2.png",
						sell_price:1499,
						market_price:2000,
						title:"华为p32 4G 256G"
					},
					{
						id:3,
						img_url:"../../static/icon/n2.png",
						sell_price:1499,
						market_price:2000,
						title:"华为p32 4G 256G"
					},
					{
						id:4,
						img_url:"../../static/icon/n2.png",
						sell_price:1499,
						market_price:2000,
						title:"华为p32 4G 256G"
					},
					{
						id:5,
						img_url:"../../static/icon/n2.png",
						sell_price:1499,
						market_price:2000,
						title:"华为p32 4G 256G"
					},
				],
				pageindex:1,
				flag:false,
				options: [{
				            icon: 'headphones',
				            text: '客服'
				        }, {
				            icon: 'shop',
				            text: '店铺',
				            info: 2,
				            infoBackgroundColor:'#007aff',
				            infoColor:"red"
				        }, {
				            icon: 'cart',
				            text: '购物车',
				            info: 2
				        }],
				        buttonGroup: [{
				          text: '加入购物车',
				          backgroundColor: '#ff0000',
				          color: '#fff'
				        },
				        {
				          text: '立即购买',
				          backgroundColor: '#ffa200',
				          color: '#fff'
				        }
				        ]
			}
		},
		components:{'goods-list':goodsList},
		methods: {
		async getGoodsList(callback){
				const res = await this.$myRequest({
					url:'/api/pageindex='+this.pageindex
				})
				this.goods=[...this.goods,...res.data]
				callback() && callback() //有函数就调用没函数就不调用
			},
			onClick (e) {
			        uni.showToast({
			          title: `点击${e.content.text}`,
			          icon: 'none'
			        })
			      },
			      buttonClick (e) {
			        console.log(e)
			        this.options[2].info++
			      }
			
		},
		onLoad(){
			this.getGoodsList()
		},
		onReachBottom(){
			if (this.goods.length<this.pageindex*10)  return this.flag=true
			console.log("到底了")
			this.pageindex++
			this.getGoodsList()
		},
		onPullDownRefresh(){
			console.log("刷新了")
			this.pageindex = 1
			this.goods=[]
			this.flag=false
			setTimeout(()=>{
				this.getGoodsList(()=>{
					uni.stopPullDownRefresh()//传递回调函数停止下拉刷新
				})
			},1000)
			
		}
		
	}
</script>

<style>
	.goods{
		background-color: #eee;
	}
	.dixian{
		text-align: center;
	}
	.nav-goods{
		position: fixed;
		bottom: 0;
		width: 100%;
	}
</style>
