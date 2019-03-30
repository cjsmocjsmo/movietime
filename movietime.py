#!/usr/bin/python3

import os
import hashlib
import random
import string
import time
#import base64
from pymongo import MongoClient
from pprint import pprint
from PIL import Image
from pathlib import PurePath as PP

NOART = "/home/pi/MovieTime/static/images/animals.jpg"    
PICPATH = "/nfs/home/charlie/Pictures"
MEDIAPATHLIST = ["/nfs/home/charlie/Videos", "/nfs/usb"]
ExtList = [".mp4", ".m4v", ".mkv", ".avi"]

client = MongoClient()
db = client.movietime2DB

class MyFile:
    def __init__(self, media):
        self.media = media
        self.purepath = PP(self.media)
        self.parts = self.purepath.parts
        self.parent = self.purepath.parent
        
        
        self.name = ""
        self.movie_catagory = ""
        self.tvshow_catagory = ""
        self.season = ""
        self.episode = ""
        if "Movies" in self.parts:
            self.name = self.purepath.name[:-11]
            self.movie_catagory = list(self.purepath.parts)[6]
        elif "usb" in self.parts:
            self.name = self.purepath.name[:-11]
            self.movie_catagory = list(self.purepath.parts)[4]
        elif "TVShows" in self.parts:
            self.tvshow_catagory = list(self.purepath.parts)[6]
            if "Voyager" in self.parts:
                self.name = self.purepath.name[25:-4]
                self.season = self.purepath.name[19:21]
                self.episode = self.purepath.name[22:24]
               
            elif "STTV" in self.parts:
                self.name = self.purepath.name[22:-4]
                self.season = self.purepath.name[16:18]
                self.episode = self.purepath.name[19:21]
   
            elif "Enterprise" in self.parts:
                self.name = self.purepath.name[21:-4]
                self.season = self.purepath.name[15:17]
                self.episode = self.purepath.name[18:20]
                
            elif "TNG" in self.parts:
                self.name = self.purepath.name[21:-4]
                self.season = self.purepath.name[15:17]
                self.episode = self.purepath.name[18:20]
                
            elif "Discovery" in self.parts:
                self.name = self.purepath.name[27:-4]
                self.season = self.purepath.name[21:23]
                self.episode = self.purepath.name[24:26]
                
            elif "Orville" in self.parts:
                self.name = self.purepath.name[19:-4]
                self.season = self.purepath.name[13:15]
                self.episode = self.purepath.name[16:18]
                
            elif "TheLastShip" in self.parts:
                self.name = self.purepath.name[21:-4]
                self.season = self.purepath.name[15:17]
                self.episode = self.purepath.name[18:20]
 
        self.name_and_year = self.purepath.name[:-4]
        self.year = self.purepath.name[-9:-5]

        self.search_path = media[:-4]
        self.jpg_search_path = ".".join((self.search_path, "jpg"))
        self.png_search_path = ".".join((self.search_path, "png"))
        self.picfolder = "/".join((PICPATH, str(self.name_and_year)))
        self.picfolder_jpg_search_path = ".".join((self.picfolder, "jpg"))
        self.picfolder_png_search_path = ".".join((self.picfolder, "png"))

        self.save_location = "/".join(("/home/pi/MovieTime2/static/images/thumbnails", self.name_and_year))
        self.id = hashlib.md5(str(random.randrange(100000)).encode('utf-8')).hexdigest()
        
class Thumbnails(MyFile):		
##    def get_b64_image(self, location):	
##        with open(location, 'rb') as imagefile:
##            return ''.join(('data:image/png;base64,', base64.b64encode(imagefile.read()).decode('utf-8')))


    def movie_thumbnail(self, filename):
        sav_loc = "".join((self.save_location, ".jpg"))
        if os.path.exists(sav_loc):
            return sav_loc
        else:
            try:
                im = Image.open(filename)
                width, height = im.size
                aspect_ratio = width / height
                new_height = 300 * aspect_ratio
                new_size =(300, int(new_height))
                im.resize(new_size, Image.ANTIALIAS)
                im.save(sav_loc, "JPEG")
            except OSError:
                print(filename)
            return sav_loc
        
    def tvshow_thumbnail(self, filename):
        sav_loc = "".join((self.save_location, ".jpg"))
        if os.path.exists(sav_loc):
            return sav_loc
        else:
            try:
                im2 = Image.open(filename)
                width, height = im2.size
                aspect_ratio = width  /  height
                siz = (100, 100)
                im2.resize(siz, Image.ANTIALIAS)
                im2.save(sav_loc, "JPEG")
            except OSError:
                print(filename)
            return sav_loc
        
    def find_movie_art(self):
        if os.path.exists(self.jpg_search_path): return self.jpg_search_path
        elif os.path.exists(self.png_search_path): return self.png_search_path
        elif os.path.exists(self.picfolder_jpg_search_path): return self.picfolder_jpg_search_path
        elif os.path.exists(self.picfolder_png_search_path): return self.picfolder_png_search_path
        else: return NOART

    def find_tvshow_art(self):
        if os.path.exists(self.jpg_search_path): return self.jpg_search_path
        elif os.path.exists(self.png_search_path): return self.png_search_path
        elif os.path.exists(self.picfolder_jpg_search_path): return self.picfolder_jpg_search_path
        elif os.path.exists(self.picfolder_png_search_path): return self.picfolder_png_search_path
        else: return NOART

if __name__ == "__main__":
    start_time = time.clock()
    
    for media_path in MEDIAPATHLIST:
        for (paths, dirs, files) in os.walk(media_path, followlinks=True):
            for filename in files:
                my_file = os.path.join(paths, filename)
                if os.path.splitext(my_file)[1] in ExtList:
                    MF = MyFile(my_file)
                    x = {}
                    x['MediaId'] = str(MF.id)
                    x["Filename"] = str(MF.media)
                    if "Movies" in MF.parts or "usb" in MF.parts:
                        #movie = Movies(str(MF.media))
                        thumbnail_path = Thumbnails(str(MF.media)).find_movie_art()
                        thumbnail = Thumbnails(str(MF.media)).movie_thumbnail(thumbnail_path)
                        
                        x["Name"] = str(MF.name)
                        x['Catagory'] = MF.movie_catagory
                        x['Year'] = str(MF.year)
                        x["Thumbnailpath"] = thumbnail
                        x["Artwork"] = thumbnail[20:]
                        print("Processed: %s" % MF.name)              
                    elif "TVShows" in MF.parts:
                        print(MF.tvshow_catagory)
                        #tvshow = TVShows(str(MF.media))
                        thumbnail_path = Thumbnails(str(MF.media)).find_tvshow_art()
                        thumbnail = Thumbnails(str(MF.media)).tvshow_thumbnail(thumbnail_path)
                        x["Filename"] = str(MF.media)
                        x["Title"] = str(MF.name)
                        x['Catagory'] = MF.tvshow_catagory
                        x['Season'] = str(MF.season)
                        x['Episode'] = str(MF.episode)
                        x["Thumbnailpath"] = thumbnail
                        x["Artwork"] = thumbnail[20:]   
                    print("Processed: %s" % MF.name)
                    print("this is Catagory %s" % MF.movie_catagory)
                    print("this is Catagory %s" % MF.tvshow_catagory)
                    print(x)
                    db.movietime2DB.insert(x)
    print(time.clock() - start_time)