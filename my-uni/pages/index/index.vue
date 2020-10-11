<template>
	<view class="home">
		<swiper indicator-dots circular>
			<swiper-item v-for="item in swipers" :key=item.id>
				<image :src="item.img" mode="scaleToFill"></image>
			</swiper-item>
		</swiper>
		
		<!--导航-->
		<view class="nav">
			<view class="nav_item" v-for="(item,index) in navs" :key="index" @click="navItemclick(item.path)">
				<view :class="item.icon"></view>
				<text>{{item.title}}</text>
			</view>
		</view>
		<!--推荐-->
		<view class='hot_goods'>
			<view class="title">
				推荐商品
			</view>
			<!--调用组件-->
			<goods-list :goods="goods"></goods-list>
		</view>
	</view>

</template>

<script>
	import goodsList from '../../components/goods-list/goods-list.vue'  //导入组建
	export default {
		data() {
			return {
				swipers:[
					{
						id:1,
						img:"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3252521864,872614242&fm=26&gp=0.jpg",
						url:""
					},
					{
						id:2,
						img:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1594117848281&di=f2f94fe09d0f91066a240074e0b44b19&imgtype=0&src=http%3A%2F%2Fa3.att.hudong.com%2F14%2F75%2F01300000164186121366756803686.jpg",
						url:""
					},
					{
						id:3,
						img:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1594117848281&di=519e59f9ee6e285416eb54ac71b5caf8&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F56%2F12%2F01300000164151121576126282411.jpg",
						url:""
					}
				],
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
				navs:[
					{
						icon:'iconfont iconaliwangwang',
						title:'星',
						path:'/pages/goods/goods'
					},
					{
						icon:'iconfont iconchart-relation',
						title:'元',
						path:'/pages/connme/connme'
					},
					{
						icon:'iconfont iconlightbulb-fill',
						title:'商',
						path:'/pages/pics/pics'
					},
					{
						icon:'iconfont iconintegral',
						title:'城',
						path:'/pages/goods/goods'
					},
				]
			}
		},
		components:{ //注册组建
			"goods-list":goodsList 
		},
		methods: {
			//获取幻灯片数据
			async getSwipers(){
				const res = await this.$myRequest({
						url:''
					})
				this.swipers = res.data
			},
			//导航条点击时间
			navItemclick(url){
				console.log(url)
				uni.navigateTo({
					url:url
				})
			},
			//获取推荐商品
			async getHotGoods(){ 
				const res = await this.$myRequest({
					url:''
				})
				this.goods = res.data
			}
		},
		onLoad() {
			this.getSwipers()
			this.getHotGoods()
		}
	}
</script>

<style lang="scss">
	.home{
		swiper{
			width: 750rpx;
			height: 350rpx;
			image{
				height: 100%;
				width: 100%;
			}
		}
	}
	.nav{
		display: flex;
		.nav_item{
			width: 25%;
			text-align: center;
			view{
				width: 120rpx;
				height: 120rpx;
				background: #f80000;
				border-radius: 60rpx;
				margin: 10px auto;
				line-height: 120rpx;
				color: #fff;
				font-size: 50rpx;
			}
			.iconaliwangwang{
				font-size: 45rpx;
			}
			text{
				font-size: 40rpx;
			}
		}
	}
	.hot_goods{
		background-color: #eee;
		overflow: hidden;
		.title{
			height: 50px;
			line-height: 50px;
			color: #DD524D;
			text-align: center;
			letter-spacing: 20px;
			background-color: #fff;
			margin: 10rpx 0;
		}
	}
	
</style>
