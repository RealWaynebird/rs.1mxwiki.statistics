from plone import api
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
import logging

class PageCnt(BrowserView):
	def pagecnt(self):
                catalog = getToolByName(self.context, 'portal_catalog')
                results = catalog.searchResults({'portal_type': 'Document'})
                logger = logging.getLogger('statistics')
                if not len(logger.handlers):
                        lhdlr = logging.FileHandler('/opt/plone/zeocluster/var/zeoserver/statistics.log')
                        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                        lhdlr.setFormatter(formatter)
                        logger.addHandler(lhdlr)
                        logging.basicConfig(mode='w')
                logger.info(str(len(results)) + " Pages in the Plone")



