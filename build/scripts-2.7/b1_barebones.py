#!/usr/local/opt/python/bin/python2.7

__author__ = "ccheever"

import urlparse

import bunny1
from bunny1 import cherrypy
from bunny1 import Content
from bunny1 import q
from bunny1 import qp
from bunny1 import expose
from bunny1 import dont_expose
from bunny1 import escape
from bunny1 import HTML


class MyCommands(bunny1.Bunny1Commands):

    def ps(self, arg):
        """go to PS service desk"""
        return "https://jira.tiki.com.vn/servicedesk/customer/portal/5" 

    def jira(self, arg):
        """go to description and details of a JIRA ticket"""
        if arg:
            return "https://jira.tiki.com.vn/projects/PS/queues/custom/27/%s" % qp(arg)
        else:
            return "https://jira.tiki.com.vn/projects/PS/queues/custom/27"

    def data(self, arg):
        """go to channel to request DA tasks"""
        return "https://jira.tiki.com.vn/servicedesk/customer/portal/5/group/67"

    def docs(self, arg):
        """go to Tiki Docs (Confluence)"""
        return "https://docs.tiki.com.vn/"

    def debug(self, arg):
        """go to debugger tool"""
        if arg:
            return "http://backend.tiki.vn/tool/product_debugger?q=%s" % qp(arg)
        else:
            return "http://backend.tiki.vn/tool/product_debugger"

    def couponr(self, arg):
        """reset coupon of a cancelled order"""
        if arg: 
            return "http://backend.tiki.vn/tool/product_support?order-code=%s" % qp(arg)
        else:
            return "http://backend.tiki.vn/tool/product_support"

    def pck(self, arg):
        if arg:
            return "http://erp.tiki.vn/#id=%s&view_type=form&model=stock.picking&action=318" % qp(arg)
        else: 
            return "http://erp.tiki.vn/#page=0&limit=80&view_type=list&model=stock.picking&menu_id=274&action=318"

    def rma(self, arg):
        if arg:
            return "http://admin.tiki.vn/index.php/rmaadmin/adminhtml_rma/edit/id/%s" % qp(arg)
        else: 
            return "http://admin.tiki.vn/index.php/rmaadmin/adminhtml_rma/edit/id/"



    def another_command(self, arg):
        """this example will send content to the browser rather than redirecting"""
        raise HTML("some <u>html</u> " + escape("with some <angle brackets>"))



class MyBunny(bunny1.Bunny1):
    def __init__(self):
        bunny1.Bunny1.__init__(self, MyCommands(), bunny1.Bunny1Decorators())

if __name__ == "__main__":
    bunny1.main(MyBunny())


