import feedparser

url ="https://www.ntv.com.tr/son-dakika.rss"
haberler = feedparser.parse(url)
for i in haberler['items']:
    print(i["title"]+"\n"+i["summary"]+"\n")
    
input()