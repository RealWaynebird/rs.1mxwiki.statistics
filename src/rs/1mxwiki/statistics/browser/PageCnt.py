from plone import api
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
import logging

class PageCnt(BrowserView):
	def pagecnt(self):
		context = self.context
		catalog = getToolByName(self.context, 'portal_catalog')
		results = catalog.searchResults({'portal_type': 'Document'})
		logger = logging.getLogger('statistics')		
		lhdlr = logging.FileHandler('/opt/plone/zeocluster/var/zeoserver/statistics.log')
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		lhdlr.setFormatter(formatter)
 		logger.addHandler(lhdlr)
		logger.setLevel(logging.INFO)
		logger.info(str(len(results)) + " Pages in the Plone")

