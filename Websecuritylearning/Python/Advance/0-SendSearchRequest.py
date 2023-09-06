import urllib.request

url = "https://cn.bing.com/search?q="
keyword = 'Python'
keyword_code = urllib.request.quote(keyword)
urls = url + keyword_code
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request = urllib.request.Request(urls,headers=header)
response = urllib.request.urlopen(request).read()

fl = open('searchresult.html','wb')
fl.write(response)
fl.close