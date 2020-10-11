import requests
import time
ts = int(time.time())
rt = int(time.time()*1000)
# print(ts)

headers = {
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "Hm_lvt_7aa1ece4891bbe95ff97d9fc51c51c42=1581413386; Hm_lpvt_7aa1ece4891bbe95ff97d9fc51c51c42=1581413389",
        "Host": "www.myerong.com",
        "Pragma": "no-cache",
        "Referer": "http://qh168.com.cn",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

url = 'http://www.qh168.com.cn/captcha?id=%d' %ts
res = requests.get(url,headers=headers)
print(res.content)
with open('aa.jpg', 'wb') as f:
    f.write(res.content)
    print('OK')