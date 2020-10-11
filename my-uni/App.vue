<script>
	export default {
		onLaunch: function() {
			//console.log('App Launch')
			switch (uni.getSystemInfoSync().platform) {
				case 'android':
					//console.log('运行Android上') 
					plus.navigator.closeSplashscreen();
					break;
				case 'ios':
					//console.log('运行iOS上') 
					plus.navigator.closeSplashscreen();
					break;
				default:
					//console.log('运行在开发者工具上') 
					break;
		}
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	@font-face {font-family: "iconfont";
	  src: url('~@/static/font/iconfont.eot?t=1594174686449'); /* IE9 */
	  src: url('~@/static/font/iconfont.eot?t=1594174686449#iefix') format('embedded-opentype'), /* IE6-IE8 */
	  url('data:application/x-font-woff2;charset=utf-8;base64,d09GMgABAAAAAAW0AAsAAAAACnwAAAVnAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHEIGVgCDVgqHOIZUATYCJAMcCxAABCAFhG0Hehs+CRGVpA+R/Shw18JirDoaq+4RQjw2KX6cdvf1iYf+9/vfnnPmyjdtItaVhCexRCWR8NAsNkIms7qW8H7+Pf1zl0xtZ7QTlWSC0gkP1B+I4AnYXGrSOQERID9hrmzyyfWO7HdOHicr63gZLkIFsAGsf3+omnkeC85n3+Iy18BgKByaQAEaY1O6ucAtsBTAewyvsD14NUHnCQxbZA/diownQEECSeCC15XlhaDg0MoIUugVbcDahPgOsvoyLnMBwDft9+M/uIYCKJoKcNHDsogSCH4+/SIfo//TcrAxGCzOjNsmKvaBJD4HWt8CZkT3YYY/z+DuAhjVK/L39PPlz7e9IF7k/x/gwOUJwRlG2T94hKJKjZZoAUtHKfGJujWEPAkR/F6OKPzehqj8IRDJnzxEw598mUHFd5PHMUYsA8RPRFyPhVTYfiemZkpKKriFWFVDJCgmljMMx/Gg8UlXzGT6PnEJyzJMJHGQBZqxJvc7RByd40RdIE5x3RxHcYIJgvR3F6zbpkceYYAmWZaTJ9N5vlxKMAwhYCaoOF+EOCTlneyo9R4saWF1npxkU66SiKWzJjbpwuLNk1sN0JItAtsQhKRb6kEUHJcLp7CBTIkSjH5Yy0edZMXOMG24mYWCyycsLzATXOIe9/zDUt5uBWow289C6wljpNvvZSd5vx0fd7pwKfqIt8V0OXbTDDYLuGexWfCAkH1akJVBZaL5m7W0d7I8b7Vwq052N/OECP1z+Ofp7NMSkkqnKIIgibkfsm/9E1OUQ5a2V7IgJzokF/JzIvWDdQaLigf1gvVNonq0shzTKdMciV2qdn68B2aeUmCT4WZrELO8qPNahoFbmmp2fEAOHhkml7u7oD00HOCJNQS8cbbMHBvJssi1LCUS9HKttmqqiuhNI8Q1G0l/WKlltkXGxFimea7leeTKshgbkedZ5Zzu/2ccXV8XbYTiTNZzV7RxfS3+cjC5neJlWH5QlHT6wVdqNNhoctPXUCnz/Ba1G0eByZ01h8Wa+7FofIvtPjwa2//XptKKNvaALRt7qd6OwLpXhsOmg+dXjyHmOrdaPOj4dnWvLqlRJAXaZzI8FT5rFhn+bNx99UuY69C5wTjYEkVm50QgyYXLM1yWTbksVW2IQNm5KMJGEvZsygHNWfFilkuBY90OqDbykwuHnFzwD2lcrjCt53teLneEiJyccCS00oX6xu259oFJHmXo2EAIDqHLE/bOmrU3rvyOrNgU58rj984mL3hbVmLadlQqpIVbpc5BmLHH0xRBo3AW1Il+PfUwdvOGYETjvKH4tixrMhXj/Kfvr8Une93f7FjxVDPzHmYpLIPlOAxaADDoTTls7P+v//31fx24T6brXIwGGEgTx/oP5XG+mG8T5btcP3ztR3bvwK+9ezuNnY2bXcvxKJOYd+Cqcz8C80v4FYCuy7dZihJYsqpxE9o6L23c4sTDrI4D1jltR+RziaWuDfmcBUVnAareOjaJ+9AYcQ6t3gUM2/O6ecQMsS9yCLu+EYRJP1CM+wHVpF9sEv+gMe8fWpOxD8Mexf2eIzbDnz0KodIchi14k6LlBj3TC9/ILRnFLtAoXyTFB6CrW3filSJJEQvKyvWqFqykAC/oMmJOkCUtyGg9quZZ09igd6pNCpMzNwRBisyBwRbwjCSySmN15vn5N8RZYkgiqn6YvxBR+N5Bp9YmwL5KY6KqTRlcrDg9pSydZIkkAC/YTJhFE5CDRy0QQ9XGDOFspiG1bFJpXb08zOcuGAYPdVGiRkYTbXTRG381omglxKjTUXGO7NcYnbTwir0bdVjyUFnPfNz7aYZKOfG9foQT5POiKJXxYpgmEwA=') format('woff2'),
	  url('~@/static/font/iconfont.woff?t=1594174686449') format('woff'),
	  url('~@/static/font/iconfont.ttf?t=1594174686449') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
	  url('~@/static/font/iconfont.svg?t=1594174686449#iconfont') format('svg'); /* iOS 4.1- */
	}
	
	.iconfont {
	  font-family: "iconfont" !important;
	  font-size: 16px;
	  font-style: normal;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	}
	
	.iconchart-relation:before {
	  content: "\e78d";
	}
	
	.iconaliwangwang:before {
	  content: "\e79d";
	}
	
	.iconlightbulb-fill:before {
	  content: "\e7ac";
	}
	
	.iconprocess:before {
	  content: "\e854";
	}
	
	.iconintegral:before {
	  content: "\e85e";
	}
	
	.iconstar-circle:before {
	  content: "\e85f";
	}
	
	
</style>
