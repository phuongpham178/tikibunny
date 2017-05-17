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
import os


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

    @dont_expose
    def _help_html(self, examples=None, name="tikibunny"):
        """the help page that gets shown if no command or 'help' is entered"""

        import random

        def bookmarklet(name):
            return """<a href="javascript:bunny1_url='""" + self._base_url() + """?';cmd=prompt('bunny1.  type &quot;help&quot; to get help or &quot;list&quot; to see commands you can use.',window.location);if(cmd){window.location=bunny1_url+escape(cmd);}else{void(0);}">""" + name + """</a>"""

        if not examples:
            examples = [
                    "ps",
                    "jira",
                    "docs",
                    "debug",
                    "ya what is the meaning of life?",
                    "list Facebook",
                    "fbs john",
                    "php array_merge",
                    "wp FBML",
                    "fb mark zuckerberg",
                    "gmaps 285 Hamilton Ave, Palo Alto, CA 94301",
                    "gimg bisu",
                    "rickroll",
                    "yt i'm cool sushi654 yeah",
                    "y osteria palo alto",
                    "live james harrison",
                    ]

        return """
<html>
<head>
<title>bunny1</title>
""" + self._opensearch_link() + """
<style>
BODY {
    font-family: Sans-serif;
    width: 800px;
}

code {
    color: darkgreen;
}

A {
    color: #3B5998;
}

small {
    width: 800px;
    text-align: center;
}

.header {
    position: absolute;
    top: 0px;
    left: 0px;
}

.test-query-input {
    width: 487px;
    font-size: 20px;
}

.header-placeholder {
    height: 45px;
}

</style>
</head>
<body>
<h1 class="header-placeholder"><img class="header" src="tiki_header.gif" /></h1>

<p>""" + name + """ is a tool that lets you write smart bookmarks in python and then share them across all your browsers and with a group of people or the whole world.  It was developed at <a href="http://www.facebook.com/">Facebook</a> and is widely used there.</p>

<form method="GET">
<p style="width: 820px; text-align: center;"><input class="test-query-input" id="b1cmd" type="text" name="___" value=""" + '"' + escape(random.choice(examples)) + '"' + """/> <input type="submit" value=" try me "/></p>

<p>Type something like """ + " or ".join(["""<a href="#" onclick="return false;"><code onclick="document.getElementById('b1cmd').value = this.innerHTML; return true;">""" + x + "</code></a>" for x in examples]) + """.</p>

<p>Or you can see <a href="?list">a list of shortcuts you can use</a> with this example server.</p>

<h3>Running Your Own bunny1 Server</h3>
<ul>Download the <a href="https://github.com/phuongpham178/tikibunny">source code</a> for the project.  Or if you use setuptools, you can just <code>easy_install bunny1</code>.</ul>

<ul>To run an example server, just run <code>b1_example.py --port=8080</code>.</ul>

<ul>More detailed instructions for configuring and running your own server can be found in the <a href=""" + '"' + self._base_url() + """?readme">README</a>.  You can add your own commands with just a few lines of python.</ul>

<h3>Installing on Firefox</h3>
<ul>Type <code>about:config</code> into your location bar in Firefox.</ul>
<ul>Set the value of keyword.URL to be <code>""" + self._base_url() + """?</code></ul>
<ul>Make sure you include the <code>http://</code> at the beginning and the <code>?</code> at the end.</ul>
<ul>Now, type <code>list</code> or <code>wp FBML</code> into your location bar and hit enter.</ul>
<ul>Also, if you are a Firefox user and find bunny1 useful, you should check out <a href="http://labs.mozilla.com/projects/ubiquity/">Ubiquity</a>.</ul>

<h3>Installing on Safari</h3>
<ul>Drag this bookmarklet [""" + bookmarklet(name) + """] to your bookmarks bar.</ul>
<ul>Now, visit the bookmarklet, and in the box that pops up, type <code>list</code> or <code>g facebook comments widget video</code> and hit enter.</ul>
<ul>In Safari, one thing you can do is make the bookmarklet the leftmost bookmark in your bookmarks bar, and then use <code>Command-1</code> to get to it.</ul>
<ul>Alternatively, you can get the location bar behavior of Firefox in Safari 3 by using the <a href="http://purefiction.net/keywurl/">keywurl</a> extension.</ul>

<h3>Installing on Google Chrome</h3>
<ul>Choose <code>Options</code> from the wrench menu to the right of the location bar in Chrome, then under the section <code>Default Search</code>, click the <code>Manage</code> button.  Click the <code>Add</code> button and then fill in the fields name, keyword, and URL with <code>""" + name + """</code>, <code>b1</code>, and <code>""" + self._base_url() + """?</code>.  Hit <code>OK</code> and then select """ + name + """ from the list of search engines and hit the <code>Make Default</code> button to make """ + name + """ your default search engine.  Type <code>list</code> into your location bar to see a list of commands you can use.</ul>

<h3>Installing on Internet Explorer</h3>
<ul>There aren't any great solutions for installing """ + name + """ on IE, but two OK solutions are:</ul>
<ul>You can use this bookmarklet [""" + bookmarklet(name) + """] by dragging into your bookmarks bar and then clicking on it when you want to use """ + name + """.</ul>
<ul>Or, in IE7+, you can click the down arrow on the search bar to the right of your location bar and choose the starred """ + name + """ option there.  This will install the bunny OpenSearch plugin in your search bar.</ul>

<hr />
<small>bunny1 was originally written by <a href="http://www.facebook.com/people/Charlie-Cheever/1160">Charlie Cheever</a> at <a href="http://developers.facebook.com/opensource.php">Facebook</a> and is maintained by him, <a href="http://www.facebook.com/people/David-Reiss/626221207">David Reiss</a>, Eugene Letuchy, and <a href="http://www.facebook.com/people/Daniel-Corson/708561">Dan Corson</a>.  Julie Zhuo drew the bunny logo.</small>


</body>
</html>
        """


class MyBunny(bunny1.Bunny1):
    def __init__(self):
        bunny1.Bunny1.__init__(self, MyCommands(), bunny1.Bunny1Decorators())

    @cherrypy.expose
    def tiki_header_gif(self):
        """the banner GIF for the bunny1 homepage 123"""
        cherrypy.response.headers["Content-Type"] = "image/gif"
        return file("header_tiki.gif").read()
        # return bunny1.bunny1_file("header_tiki.gif")
if __name__ == "__main__":
    bunny1.main(MyBunny())


