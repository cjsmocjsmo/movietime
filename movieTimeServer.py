#!/usr/bin/python

import os, json, hashlib, re, time, uuid, shutil, glob, pymongo, subprocess
from urllib.parse import urlparse, parse_qs
from PIL import Image
from pymongo import MongoClient
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
try:
	from omxplayer.player import OMXPlayer
except ImportError:
	from movmods.omxplayer.player import OMXPlayer
import movietime as MT


client = MongoClient()
db = client.movietime2DB
define('port', default=8080, help='run on the given port', type=int)

class Application(tornado.web.Application):
	def __init__(self):
		Movies = '/nfs/home/charlie/Videos/Movies'
		TVShows = '/nfs/home/charlie/Videos/TVShows'
		Pictures = "/home/pi/MovieTime2/static/images/thumbnails"
#		Pictures = '/nfs/home/charlie/Pictures'
        
		handlers = [
			(r"/Movies/(.*)", tornado.web.StaticFileHandler, {'path': Movies}),
			(r"/TVShows/(.*)", tornado.web.StaticFileHandler, {'path': TVShows}),
			(r"/Pictures/(.*)", tornado.web.StaticFileHandler, {'path': Pictures}),
			(r"/movietime", MainHandler),
			(r"/IntSciFi", IntSciFiHandler),
			(r"/IntAction", InitActionHandler),
			(r"/IntComedy", InitComedyHandler),
			(r"/IntDrama", InitDramaHandler),
			(r"/IntCartoons", IntCartoonsHandler),
			(r"/IntGodzilla", IntGodzillaHandler),
			(r"/IntKingsMan", IntKingsManHandler),
			(r"/IntStarTrek", IntStarTrekHandler),
			(r"/IntStarWars", IntStarWarsHandler),
			(r"/IntSuperHeros", IntSuperHerosHandler),
			(r"/IntIndianaJones", IntIndianaJonesHandler),
			(r"/IntHarryPotter", IntHarryPotterHandler),
			(r"/IntTremors", IntTremorsHandler),
			(r"/IntJohnWayne", IntJohnWayne),
			(r"/IntJurassicPark", IntJurasicParkHandler),
			(r"/IntMenInBlack", IntMenInBlackHandler),
			(r"/IntMisc", IntMiscHandler),
			(r"/STTVs1", STTVS1Handler),
			(r"/STTVs2", STTVS2Handler),
			(r"/STTVs3", STTVS3Handler),
			(r"/TNGs1", TNGS1Handler),
			(r"/TNGs2", TNGS2Handler),
			(r"/TNGs3", TNGS3Handler),
			(r"/TNGs4", TNGS4Handler),
			(r"/TNGs5", TNGS5Handler),
			(r"/TNGs6", TNGS6Handler),
			(r"/TNGs7", TNGS7Handler),
			(r"/VOYs1", VOYS1Handler),
			(r"/VOYs2", VOYS2Handler),
			(r"/VOYs3", VOYS3Handler),
			(r"/VOYs4", VOYS4Handler),
			(r"/VOYs5", VOYS5Handler),
			(r"/VOYs6", VOYS6Handler),
			(r"/VOYs7", VOYS7Handler),
			(r"/ENTs1", ENTS1Handler),
			(r"/ENTs2", ENTS2Handler),
			(r"/ENTs3", ENTS3Handler),
			(r"/ENTs4", ENTS4Handler),
			(r"/DISs1", DISS1Handler),
			(r"/ORVs1", ORVS1Handler),
			(r"/TLSs1", TLSS1Handler),
			(r"/TLSs2", TLSS2Handler),
			(r"/TLSs3", TLSS3Handler),
			(r"/TLSs4", TLSS4Handler),
			(r"/PlayMedia", PlayMediaHandler),
			(r"/Play", PlayHandler),
			(r"/Pause", PauseHandler),
			(r"/Stop", StopHandler),
			(r"/Next", NextHandler),
			(r"/Previous", PreviousHandler),
			(r"/Update", UpdateHandler),
		]
		settings = dict(
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			debug = True,
		)
		tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('movietime.html')

class IntSciFiHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [s for s in db.movietime2DB.find({"Catagory":"SciFi"}, {"_id":0})]
		print(l)
#		n = 2
#		if n < 1:
#			n = 1
#		chuncks = [l[i:i + n] for i in range(0, len(l), n)]
#		self.write(dict(IntSciFi=chuncks))
		self.write(dict(IntSciFi=l))
	
class InitActionHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [s for s in db.movietime2DB.find({"Catagory":"Action"}, {"_id":0})]
		self.write(dict(IntAction=l))

class InitComedyHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [s for s in db.movietime2DB.find({"Catagory":"Comedy"}, {"_id":0})]
		self.write(dict(IntComedy=l))

class InitDramaHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [s for s in db.movietime2DB.find({"Catagory":"Drama"}, {"_id":0})]
		self.write(dict(IntDrama=l))

class IntCartoonsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [c for c in db.movietime2DB.find({"Catagory":"Cartoons"}, {"_id":0})]
		self.write(dict(IntCartoons=l))

class IntKingsManHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		klist = [k for k in db.movietime2DB.find({"Catagory":"Kingsman"}, {"_id":0})]
		self.write(dict(IntKingsMan=klist))

class IntGodzillaHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [g for g in db.movietime2DB.find({"Catagory":"Godzilla"}, {"_id":0})]
		self.write(dict(IntGodzilla=l))

class IntStarTrekHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [st for st in db.movietime2DB.find({"Catagory":"StarTrek"}, {"_id":0})]
		self.write(dict(IntStarTrek=l))
	
class IntStarWarsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [sw for sw in db.movietime2DB.find({"Catagory":"StarWars"}, {"_id":0})]

		self.write(dict(IntStarWars=l))

class IntSuperHerosHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [sh for sh in db.movietime2DB.find({"Catagory":"SuperHeros"}, {"_id":0})]
		self.write(dict(IntSuperHeros=l))

class IntJurasicParkHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [sh for sh in db.movietime2DB.find({"Catagory":"Jurasic Park"}, {"_id":0})]
		self.write(dict(IntJurasicPark=l))

class IntIndianaJonesHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [ij for ij in db.movietime2DB.find({"Catagory":"IndianaJones"}, {"_id":0})]
		self.write(dict(IntIndianaJones=l))

class IntHarryPotterHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [ij for ij in db.movietime2DB.find({"Catagory":"Harry Potter"}, {"_id":0})]
		self.write(dict(IntHarryPotter=l))

class IntTremorsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [ij for ij in db.movietime2DB.find({"Catagory":"Tremors"}, {"_id":0})]
		self.write(dict(IntTremors=l))

class IntJohnWayne(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [ij for ij in db.movietime2DB.find({"Catagory":"John Wayne"}, {"_id":0})]
		self.write(dict(IntJohnWayne=l))

class IntMenInBlackHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [sh for sh in db.movietime2DB.find({"Catagory":"Men In Black"}, {"_id":0})]
		self.write(dict(IntMenInBlack=l))

class IntMiscHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		l = [ij for ij in db.movietime2DB.find({"Catagory":"Misc"}, {"_id":0})]
		self.write(dict(IntMisc=l))

class STTVS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"STTV", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(STTVS1=epi))
		
class STTVS2Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"STTV", "Season":"02"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(STTVS2=epi))
		
class STTVS3Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"STTV", "Season":"03"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(STTVS3=epi))

class TNGS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS1=epi))

class TNGS2Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"02"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS2=epi))

class TNGS3Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"03"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS3=epi))

class TNGS4Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"04"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS4=epi))

class TNGS5Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"05"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS5=epi))

class TNGS6Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"06"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS6=epi))

class TNGS7Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TNG", "Season":"07"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TNGS7=epi))

class VOYS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS1=epi))

class VOYS2Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"02"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS2=epi))

class VOYS3Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"03"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS3=epi))

class VOYS4Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"04"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS4=epi))

class VOYS5Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"05"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS5=epi))

class VOYS6Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"06"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS6=epi))

class VOYS7Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Voyager", "Season":"07"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(VOYS7=epi))

class ENTS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Enterprise", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(ENTS1=epi))

class ENTS2Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Enterprise", "Season":"02"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(ENTS2=epi))

class ENTS3Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Enterprise", "Season":"03"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(ENTS3=epi))

class ENTS4Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Enterprise", "Season":"04"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(ENTS4=epi))

class DISS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Discovery", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(DISS1=epi))

class ORVS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"Orville", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(ORVS1=epi))

class TLSS1Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TheLastShip", "Season":"01"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TLSS1=epi))

class TLSS2Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TheLastShip", "Season":"02"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TLSS2=epi))

class TLSS3Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TheLastShip", "Season":"03"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TLSS3=epi))

class TLSS4Handler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		epi = [e for e in db.movietime2DB.find({"Catagory":"TheLastShip", "Season":"04"}, {"_id":0, "Title":1, "MediaId":1, "Episode":1}).sort([("Episode", 1)])]
		self.write(dict(TLSS4=epi))

class PlayMediaHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def check_status(self):
		status = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "status", "|", "grep", "Paused"])
		
		print('this is statussssssssTwo')
		print(status)
		return status
#		if status == "Paused: false":
#			#0 means player is playing
#			return 0
#		else:
#			return 1
		
	@tornado.gen.coroutine
	def get(self):
		status =  yield self.check_status()
		if status == 1:
			p = parse_qs(urlparse(self.request.full_url()).query)
			mediaid = p['mid'][0]
			mediainfo = db.movietime2DB.find_one({"MediaId": mediaid}, {"_id":0})
			player = OMXPlayer(mediainfo["Filename"])
			self.write(dict(PM=mediainfo))
		else:
			print("Press the Stop Button A movie is already playing")
			pass

class PlayHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		pmm = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "play"])
		
class PauseHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		pm = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "pause"])
		
class StopHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		mp = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "stop"])
		
class NextHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		nt = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "seek", "60000000"])

class PreviousHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		nt = subprocess.call(["bash", "/home/pi/MovieTime/mydbuscontrol.sh", "seek", "-30000000"])

class UpdateHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		update = MT.MovieTimeSetUp().main()
		if update == 0:
			ex = {"exit":"0"}
			self.write(dict(EX=ex))

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()