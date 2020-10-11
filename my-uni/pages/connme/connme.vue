<template>
	<view class="contact">
		<image class="img" src="http://img4.imgtn.bdimg.com/it/u=3760369061,3456924807&fm=26&gp=0.jpg"></image>
	
	<view class="contact-info">
		<view @click="call">联系电话: 12121212121(点击拨打)</view>
		<view>联系地址: 北京市朝阳区望京街道</view>
	</view>
	<map class="map" :longitude="longitude" :scale="scale" :latitude="latitude" :markers="markers"></map>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				longitude:116.490569,
				latitude:39.998296,
				scale:15,
				markers:[
					{
						longitude:116.490569,
						latitude:39.998296,
						iconPath:"../../static/icon/n1.png",
						width:30,
						height:30
					}
				]
			}
		},
		methods: {
			call(){
				uni.makePhoneCall({
					phoneNumber:"12121212121"
				})
			}
		}
	}
</script>

<style lang="scss">
	.contact{
		padding: 10rpx 20rpx;
		font-size: 30rpx;
		.img{
			width: 750rpx;
			height: 320rpx;
		}
		.contact-info{
			line-height: 60rpx;
			border-bottom: 1px solid #eee;
		}
		.map{
			margin-top: 20px;
			width: 100%;
			height: 750rpx;
		}
	}
</style>
