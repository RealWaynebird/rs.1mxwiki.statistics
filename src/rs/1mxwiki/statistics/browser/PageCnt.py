from plone import api
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
import logging
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

class PageCnt(BrowserView):
	def pagecnt(self, context, request):
		alsoProvides(request, IDisableCSRFProtection)
 		catalog = getToolByName(self.context, 'portal_catalog')
 		results = catalog.searchResults({'portal_type': 'Document'})
 		logger = logging.getLogger('statistics')		
		lhdlr = logging.FileHandler('/opt/plone/zeocluster/var/zeoserver/statistics.log', filemode='w')
 		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
 		lhdlr.setFormatter(formatter)
  		logger.addHandler(lhdlr)
		logger.info(str(len(results)) + " Pages in the Plone")


