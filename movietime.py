# /usr/bin/python3
#    MovieGo
#    Copyright (C) 2017  Charlie J Smotherman
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import hashlib
import random
import string
import time
from pymongo import MongoClient
from PIL import Image
from pathlib import PurePath

NOART = "/".join((os.getcwd(), "static/images/animals.jpg"))
PICPATH = "/home/teresa/Pictures"
MEDIAPATHLIST = ["/home/teresa/Videos", "/nfs/usb"]
EXTLIST = [".mp4", ".m4v", ".mkv", ".avi"]

client = MongoClient()
db = client.movietime2DB


class MyFile:
    def __init__(self, media):
        self.media = media
        self.purepath = PurePath(self.media)
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

        self.save_location = "/".join((
            os.getcwd(), "static/images/thumbnails", self.name_and_year))
        self.id = hashlib.md5(
            str(random.randrange(100000)).encode('utf-8')).hexdigest()


class Thumbnails(MyFile):
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
                new_size = (300, int(new_height))
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
                # width, height = im2.size
                # aspect_ratio = width  /  height
                siz = (100, 100)
                im2.resize(siz, Image.ANTIALIAS)
                im2.save(sav_loc, "JPEG")
            except OSError:
                print(filename)
            return sav_loc

    def find_movie_art(self):
        if os.path.exists(self.jpg_search_path):
            return self.jpg_search_path
        elif os.path.exists(self.png_search_path):
            return self.png_search_path
        elif os.path.exists(self.picfolder_jpg_search_path):
            return self.picfolder_jpg_search_path
        elif os.path.exists(self.picfolder_png_search_path):
            return self.picfolder_png_search_path
        else:
            return NOART

    def find_tvshow_art(self):
        if os.path.exists(self.jpg_search_path):
            return self.jpg_search_path
        elif os.path.exists(self.png_search_path):
            return self.png_search_path
        elif os.path.exists(self.picfolder_jpg_search_path):
            return self.picfolder_jpg_search_path
        elif os.path.exists(self.picfolder_png_search_path):
            return self.picfolder_png_search_path
        else:
            return NOART

if __name__ == "__main__":
    start_time = time.clock()
    for media_path in MEDIAPATHLIST:
        for (paths, dirs, files) in os.walk(media_path, followlinks=True):
            for filename in files:
                my_file = os.path.join(paths, filename)
                print(my_file)
                if os.path.splitext(my_file)[1] in EXTLIST:
                    MF = MyFile(my_file)
                    x = {}
                    if "Movies" in MF.parts or "usb" in MF.parts:
                        thumbnail_path = Thumbnails(
                            str(MF.media)).find_movie_art()
                        thumbnail = Thumbnails(
                            str(MF.media)).movie_thumbnail(thumbnail_path)
                        x['MediaId'] = str(MF.id)
                        x["Filename"] = str(MF.media)
                        x["Name"] = str(MF.name)
                        x['Catagory'] = MF.movie_catagory
                        x['Year'] = str(MF.year)
                        x["Thumbnailpath"] = thumbnail
                        x["Artwork"] = thumbnail[20:]
                        db.movietime2DB.insert(x)
                    elif "TVShows" in MF.parts:
                        thumbnail_path = Thumbnails(
                            str(MF.media)).find_tvshow_art()
                        thumbnail = Thumbnails(
                            str(MF.media)).tvshow_thumbnail(thumbnail_path)
                        x['MediaId'] = str(MF.id)
                        x["Filename"] = str(MF.media)
                        x["Title"] = str(MF.name)
                        x['Catagory'] = MF.tvshow_catagory
                        x['Season'] = str(MF.season)
                        x['Episode'] = str(MF.episode)
                        x["Thumbnailpath"] = thumbnail
                        x["Artwork"] = thumbnail[20:]
                        db.movietime2DB.insert(x)
                    print("Processed: %s" % MF.name)
    print(time.clock() - start_time)
