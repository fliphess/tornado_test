import tornado.web
import os

class PrintIp(tornado.web.RequestHandler):
    def initialize(self, *args, **kwargs):
        self.remote_ip = self.request.headers.get('X-Forwarded-For', self.request.headers.get('X-Real-Ip', self.request.remote_ip))
        self.using_ssl = (self.request.headers.get('X-Scheme', 'http') == 'https')
    def get(self):
        self.write("Client IP is %s" % self.remote_ip)
