<template>
	<view>
		<scroll-view class="right" scroll-y >
			<view class="item" v-for="item in imgdata" :key="item.id">
				<image @click="preview(item.imgurl)" :src="item.imgurl"></image>
				<text>{{item.title}}</text>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	
	export default {
		props:["imgdata"],
		methods:{
			preview(current){
		
				const urls=this.imgdata.map(item=>{
					return item.imgurl
				})
				console.log(urls)
				uni.previewImage({
					current,
					urls
				})
				
			}
		}
	}
	
</script>

<style lang="scss">

	
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
		text{
			font-size: 30rpx;
			line-height: 60rpx;
		}
	}
}


</style>
