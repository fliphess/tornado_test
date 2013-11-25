
import tornado.web
import random

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        quotes = 'htdocs/quotes.txt'
        line = random.choice(list(open(quotes)))
        (quote, author) = line.strip().split('-')

        response = """ 
        <title>flapperdeflipper.com</title><center><a href=/><img width="128" height="128" title="" alt="" src="/images/flip.jpg" /></a>
        <br><br><br><br><br>
        <center><h2>%s</h2><br></center>
        <center><h3><i>%s</i></h3><br></center>
        <br><br><br><br><br><br>
        <center>
        <a href=http://flipper.flapperdeflipper.com><img src="/images/wep.png" border="0" width="20" height="20"/></a>
        <a href=http://flapperdeflipper.com/foto><img src="/images/foto.ico" border="0" width="20" height="20"/></a>
        <a href=https://www.facebook.com/FlipHessPhotography target=_blank ><img src="images/fb.ico" border="0" width="20" height="20"/></a> 
        <a href=https://secure.flickr.com/photos/fliphess target=_blank ><img src="images/flickr.ico" border="0" width="20" height="20"/></a></center>
        <center><script src="http://thestartuplegitimizer.com/js/legitimizeme.min.js?pubs=bu-ma-tc-hu-wi-be-tn-bf-te-cn-fo-fc-nm-wa-ny-ec-ha-bb"></script></center>""" % (quote, author)
        self.write(response)
