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
            return "https://jira.tiki.com.vn/projects/PS/queues/custom/27/" + qp(arg)
        else:
            return "https://jira.tiki.com.vn/projects/PS/queues/custom/27"

    def another_command(self, arg):
        """this example will send content to the browser rather than redirecting"""
        raise HTML("some <u>html</u> " + escape("with some <angle brackets>"))



    # in this class here

class MyBunny(bunny1.Bunny1):
    def __init__(self):
        bunny1.Bunny1.__init__(self, MyCommands(), bunny1.Bunny1Decorators())

if __name__ == "__main__":
    bunny1.main(MyBunny())


