#!/usr/bin/env python
import sys
import os
import yaml
import signal


import tornado.escape
import tornado.ioloop
import tornado.web

from lib import IndexHandler
from lib import PrintIp
from lib import PrintEnv
from lib import Magic

def signal_handler(signal, frame):
    print "\nHa! You pressed Ctrl+C! Quitting Joyfully :)"
    sys.exit(0)

def read_yaml_file(config):
    if not os.path.isfile(config):
        raise Exception("%s file %s not found! Exiting script!" % config)
    try:
        config = yaml.load(file(config))
    except Exception as e:
        raise Exception("Failed to read config file %s. Output: %s" % (config, e)) 
    return config

def get_dir(config, item):
    if item in config.keys():
        return "%s/%s" % (config['basedir'], config[item])

def main():
    config = {}
    try:
        config = read_yaml_file('%s/settings.yaml' % os.getcwd())
    except Exception as e:
        raise Exception("Failed to read config file ./settings.yaml. Error was %s" % e)

    print "Starting Restfull Application on %s:%s" % (config['address'], config['port'])
    application = tornado.web.Application([
        (r'/', IndexHandler.IndexHandler),
        (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": get_dir(config, 'content')}),
        (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': get_dir(config, 'images')}),
        (r'/ip', PrintIp.PrintIp),
        (r'/env', PrintEnv.PrintEnv),
        (r'/plop', Magic.Magic)
    ])

    try:
        application.listen(config['port'], config['address'])
    except Exception as e:
        raise Exception('Error: %s' % e)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        raise Exception('Error: %s' % e)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)    # catch ctrl+c 
    sys.exit(main())
