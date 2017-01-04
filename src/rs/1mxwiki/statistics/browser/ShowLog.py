from plone import api
from Products.Five import BrowserView

class ShowLog(BrowserView):
        def __init__(self,context,request):
                return
         
        def __call__(self):
                with open('/opt/plone/zeocluster/var/zeoserver/statistics.log','r') as log:
                        return log.read()
