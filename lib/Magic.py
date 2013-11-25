import tornado.web

class Magic(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>Getting started! Please be patient!</h1>')
        




    
