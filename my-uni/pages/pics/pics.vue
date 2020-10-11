<template>
	<view class="pics">
		<scroll-view class="left" scroll-y >
			<view @click="leftclick(index,item.url)" :class="active===index?'active':''" v-for="(item,index) in imgcate" :key="item.id">{{item.title}}</view>
		
		</scroll-view>
		
		<img-list :imgdata="imgdata"></img-list>
		<view v-if="imgdata.length===0">暂无数据</view>
	</view>
</template>

<script>
	import imgList from '../../components/imglist/imglist.vue'
	export default {
		data() {
			return {
				imgcate:[
					{
						id:1,
						title:"美女图片",
						url:"urls"
					},
					{
						id:2,
						title:"美女图片",
						url:"urls"
					}
					
				],
				active:0,
				imgdata:[
					{
						id:1,
						imgurl:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1594117848281&di=f2f94fe09d0f91066a240074e0b44b19&imgtype=0&src=http%3A%2F%2Fa3.att.hudong.com%2F14%2F75%2F01300000164186121366756803686.jpg",
						title:"hehe"
					},
					{
						id:2,
						imgurl:"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3252521864,872614242&fm=26&gp=0.jpg",
						title:"疯狂大家快来发动机奥利弗看得见啊算法"
					}
				]
			}
		},
		components:{"img-list":imgList},
		methods: {
		async getPicCate(){
			const res = await this.$myRequest({
					url:url
				})
				this.imgcate = res.data
				this.leftclick(0,imcate[0].url)//页面载入获取分类的同时，获取第一个分类的图片
			},
		async leftclick(index,url){
				this.active = index
				const res = await this.$myRequest({
					url:url
				})
				this.imgdata=res.data
				
			}
			
		},
		onLoad() {
			this.getPicCate()
		}
	}
</script>

<style lang="scss">
page{
		height: 100%;
}
.pics{
	//width: 100%;
	height: 100%;
	display: flex;
	.left{
		width: 200rpx;
		height: 100%;
		margin: 1px 1px;
		//border-top: 1px solid #333333;
		view{
			height: 40px;
			line-height: 40px;
			text-align: center;
			font-size: 10px;
			margin: 1px 0;
			-moz-box-shadow:0 0 1px #06c;
			-webkit-box-shadow:0 0 1px #06c;
			box-shadow:0 0 1px #06c;
		}
	}
	.right{
		width: 520rpx;
		height: 100%;
		margin: 10px auto;
		.item{
			image{
				width: 520rpx;
				height: 520rpx;
				border-radius: 5px;
			}
		}
	}
	.active{
		background-color: #DD524D;
		color: #fff;
	}
}

</style>
