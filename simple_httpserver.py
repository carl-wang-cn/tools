import web

urls = (
    '/index', 'index',
    '/test', 'test',
)

class index:
    def GET(self, name):
        render = web.template.render('templates/')
        #name = 'Bob'
        print render.index(name)
#        i = web.input(times=1)
#        if not name: name = 'world'
#        for c in xrange(int(i.times)): print 'Hello,', name+'!'

class test:
    def GET(self):
        print "this is a GET response for /test"
        return 200, "ok"

    def POST(self):
        cookie = web.cookies()
        print cookie.get("name")
        print cookie.get("age")
        print cookie.get("gendor")
        print "this is a POST response for /test"
        print web.data()
        print web.input().get("name")
        print web.input().get("age")
        return 200, "ok"

    def HEAD(self):
        print "this is a HEAD response for /test"
        return 200, "ok"

if __name__ == "__main__": web.run(urls, globals())
