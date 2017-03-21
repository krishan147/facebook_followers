import time
import json
import urllib

class Facebook():

    def __init__(self,fb_handle):

        self.fb_handle = fb_handle

        #FACEBOOK AUTHENTICATION

        access_token = ENTER ACCESS TOKEN HERE

        #FACEBOOK API - LIKES

        facebook_url = 'https://graph.facebook.com/v2.8/'+fb_handle+'?fields=username,id,fan_count&access_token='+ access_token
        opener = urllib.urlopen(facebook_url)

        for data in opener:
            parsed_data = json.loads(data)
            page_likes = parsed_data['fan_count']
            print page_likes
            time.sleep(3)
