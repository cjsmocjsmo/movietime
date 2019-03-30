#!/usr/bin/python3

import unittest
import movietime as MT

MovieTestPath = "/home/pi/taz/Videos/Movies/Action/Some Made Up Movie (2018).mp4"
DiscoveryTestPath ="/home/pi/taz/Videos/TVShows/Discovery/S1/Star Trek Discovery S01E01 The Volcan Hello.mkv"
EnterpriseTestPath = "/home/pi/taz/Videos/TVShows/Enterprise/S1/Star Trek ENT S01E01 Broken Bow.mkv"
OrvilleTestPath = "/home/pi/taz/Videos/TVShows/Orville/S1/The Orville S01E01 Old Wounds.mkv"
STTVTestPath = "/home/pi/taz/Videos/TVShows/STTV/S1/Star Trek STTV S01E01 The Cage.mp4"
TheLastShipTestPath = "/home/pi/taz/Videos/TVShows/TheLastShip/S1/The Last Ship S01E01 Phase Six.mp4"
VoyagerTestPath = "/home/pi/taz/Videos/TVShows/Voyager/S1/Star Trek Voyager S01E01 Caretaker.mkv"
TNGTestPath =  "/home/pi/taz/Videos/TVShows/TNG/S1/Star Trek TNG S01E01 Encounter at Farpoint.mkv"
PicPath = "/nfs/home/charlie/Pictures"

MF = MT.MyFile(MovieTestPath)

class TestMyFile(unittest.TestCase):
    def test_media(self):
        self.assertEqual(MF.media, "/home/pi/taz/Videos/Movies/Action/Some Made Up Movie (2018).mp4")
    
    def test_parts(self):
        self.assertEqual(len(MF.parts), 8)
    
    def test_parent(self):
        self.assertEqual(str(MF.parent), "/home/pi/taz/Videos/Movies/Action")
    
    def test_name(self):
        self.assertEqual(str(MF.name), "Some Made Up Movie")
    
    def test_name_and_year(self):
        self.assertEqual(str(MF.name_and_year), "Some Made Up Movie (2018)")
    
    def test_year(self):
        self.assertEqual(str(MF.year), "2018")
 
    def test_search_path(self):
        self.assertEqual(str(MF.search_path), "/home/pi/taz/Videos/Movies/Action/Some Made Up Movie (2018)")
    
    def test_jpg_search_path(self):
        self.assertEqual(str(MF.jpg_search_path), "/home/pi/taz/Videos/Movies/Action/Some Made Up Movie (2018).jpg")
    
    def test_png_search_path(self):
        self.assertEqual(str(MF.png_search_path), "/home/pi/taz/Videos/Movies/Action/Some Made Up Movie (2018).png")

    def test_picfolder(self):
        self.assertEqual(str(MF.picfolder), "/".join((MT.PICPATH, MF.name_and_year)))

    def test_picfolder_jpg_search_path(self):
        self.assertEqual(str(MF.picfolder_jpg_search_path), ".".join((MF.picfolder, "jpg")))
    
    def test_picfolder_png_search_path(self):
        self.assertEqual(str(MF.picfolder_png_search_path), ".".join((MF.picfolder, "png")))

    def test_save_location(self):
        path = "/".join(("/home/pi/MovieTime2/static/images/thumbnails", MF.name_and_year))
        self.assertEqual(str(MF.save_location), path)
    
    def test_id(self):
        self.assertEqual(len(MF.id), 32)

    def test_voyager(self):
        MyF = MT.MyFile(VoyagerTestPath)
        self.assertEqual(MyF.name, "Caretaker")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")
        
    def test_STTV(self):
        MyF = MT.MyFile(STTVTestPath)
        self.assertEqual(MyF.name, "The Cage")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")

    def test_Enterprise(self):
        MyF = MT.MyFile(EnterpriseTestPath)
        self.assertEqual(MyF.name, "Broken Bow")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")
        
    def test_TNG(self):
        MyF = MT.MyFile(TNGTestPath)
        self.assertEqual(MyF.name, "Encounter at Farpoint")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")
        
    def test_Discovery(self):
        MyF = MT.MyFile(DiscoveryTestPath)
        self.assertEqual(MyF.name, "The Volcan Hello")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")
        
    def test_Orville(self):
        MyF = MT.MyFile(OrvilleTestPath)
        self.assertEqual(MyF.name, "Old Wounds")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")
        
    def test_TheLastShip(self):
        MyF = MT.MyFile(TheLastShipTestPath)
        self.assertEqual(MyF.name, "Phase Six")
        self.assertEqual(MyF.season, "01")
        self.assertEqual(MyF.episode, "01")