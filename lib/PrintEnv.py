
import tornado.web
import os

class PrintEnv(tornado.web.RequestHandler):
    def get(self):
        env = os.environ
        line = "%s = %s<br>\n"
        output = ''
        for item in env.keys():
            output += line % (item, env[item])
        self.write(output)

