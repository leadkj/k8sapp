<template>
	<view class="good_list">
		<view class="good_item" v-for="item in goods" :key="item.id">
			<image :src="item.img_url"></image>
			<view class="price">
				<text>￥{{item.sell_price}}</text>
				<text>￥{{item.market_price}}</text>
			</view>
			<view class="good_name">
				{{item.title}}
			</view>
		</view>
		
	</view>
</template>

<script>
	export default{
		props:["goods"] //接受外界传给组件的数据
	}
</script>

<style lang="scss">
	.good_list{
		padding: 0 2px;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		.good_item{
			background: #fff;
			margin: 5px 0;
			width: 365rpx;
			height: 450rpx;
			//text-align: center;
			box-sizing: border-box;//盒子不会被称大，内容变小
			image{
				width: 80%;
				height: 300rpx;
				display: block; //元素居中
				margin:10px auto;//元素自己居中
			}
			
			.price{
				
				color: #DD524D;
				font-size: 35rpx;
				text:nth-child(2){
					color: #ccc;
					font-size: 28rpx;
					margin-left: 7px;
					text-decoration: line-through;
				}
			}
			.good_name{
				font-size: 28rpx;
				line-height: 35rpx;
				padding-top: 10rpx;
				padding-bottom: 15rpx;
			}
		}
	}
</style>
