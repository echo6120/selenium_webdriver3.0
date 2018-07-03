# -*- coding: utf-8 -*-
import web
from web import form

import cgi

render = web.template.render('templates/')

urls = (
     '/', 'index',
     '/interface', 'interface'

)
app = web.application(urls, globals())



class index: 
    def GET(self): 
		#return "Hello, world!"
		#print "hello world"
        #form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
         #print(form.render())
        return render.formtest()


class interface:
    def GET(self): return "hi"
    def POST(self):
         i = web.input()
         return 'form value:',i.title

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
