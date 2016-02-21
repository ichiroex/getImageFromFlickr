#coding: utf-8
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import json
import sys
import urllib2


def getImageUrlFromFlickr(API_KEY, query, N):

    NUM_OF_PHOTO = str(N) #取得する画像URLの数
    option = '&sort=relevance&privacy_filter=1&content_type=1&per_page='+ NUM_OF_PHOTO +'&format=json&nojsoncallback=1'
    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key='+ API_KEY + option
    
    #JSON形式で結果を取得
    register_openers()
    datagen, headers = multipart_encode({'text': query})
    request = urllib2.Request(url,datagen, headers)
    response = urllib2.urlopen(request)
    res_dat = response.read()
    
    url_list = [] #URLリスト
    template_url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' #URLのテンプレート
    for i in json.loads(res_dat)['photos']['photo']:
        img_url = template_url % (i['farm'],i['server'],i['id'],i['secret'])
        url_list.append(img_url) #リストに画像URLを追加

    return url_list

if __name__ == '__main__':

    API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'

    query = sys.argv[1]
    #API KEY, クエリ, 取得したい画像の数を渡す
    url_list = getImageUrlFromFlickr(API_KEY, query, 10) 
    
    #取得した画像URLを表示
    for url in url_list:
        print url



