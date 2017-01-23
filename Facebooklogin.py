import sys
import os
import random
import socket
import urllib.request
import urllib.parse
import re


url = 'https://www.facebook.com'
values = {'style': 'lo',
          'jlou': 'AfepAeBoDZd1h19y-ekG5lQdrONQlZKyQx3t-i_sRn74lP_68o3HlsZOrzgU0K648rN9iAzNBiipqupYPOTLxNMc1fm9G7wGLUyoZm_l3TweqA',
          'smuh': '30038',
          'Ih': 'Ac_rRdhafRRKMQec'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<a href(.*?)</a>',str(respData))

print(paragraphs)


