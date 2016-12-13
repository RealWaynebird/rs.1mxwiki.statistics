from plone import api
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
import logging

class PageCnt(BrowserView):
	def pagecnt(self):
		context = self.context
		catalog = getToolByName(self.context, 'portal_catalog')
		results = catalog.searchResults({'portal_type': 'Document'})
		logging.basicConfig(filename='/opt/plone/zeocluster/var/zeoserver/statistics.log', filemode='w', level=logging.INFO)
		logging.info('%(asctime)s %(levelname)s' + str(len(results)) + " Pages in the Plone")

