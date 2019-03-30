#!/usr/bin/python3

import unittest
import movietime

class TestTVShowCatagory(unittest.TestCase):
    def runner(self, filename):
        MF = movietime.MyFile(filename)
        tvshow = movietime.TVShows(MF.media)
        tvshow_cat = tvshow.catagory()
        return tvshow_cat
        
    def test_tvshow_cat_tng(self):
        tng_test_path =  "/home/pi/taz/TVShows/TNG/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(tng_test_path) , "TNG")
        
    def test_tvshow_cat_sttv(self):
        sttv_test_path = "/home/pi/taz/TVShows/STTV/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(sttv_test_path), "STTV")
        
    def test_tvshow_cat_orville(self):
        orville_test_path = "/home/pi/taz/TVShows/Orville/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(orville_test_path), "Orville")
        
    def test_tvshow_cat_voyager(self):
        voyager_test_path = "/home/pi/taz/TVShows/Voyager/Some Made Up Movie (2018).mp4"
        tvshow_cat = self.runner(voyager_test_path)
        assert tvshow_cat == "Voyager"
        
    def test_tvshow_cat_discovery(self):
        discovery_test_path = "/home/pi/taz/TVShows/Discovery/Some Made Up Movie (2018).mp4"
        tvshow_cat = self.runner(discovery_test_path)
        assert tvshow_cat == "Discovery"
        
    def test_tvshow_cat_enterprise(self):
        enterprise_test_path = "/home/pi/taz/TVShows/Enterprise/Some Made Up Movie (2018).mp4"
        tvshow_cat = self.runner(enterprise_test_path)
        assert tvshow_cat == "Enterprise"
        
    def test_tvshow_cat_thelastship(self):
        thelastship_test_path = "/home/pi/taz/TVShows/TheLastShip/Some Made Up Movie (2018).mp4"
        tvshow_cat = self.runner(thelastship_test_path)
        assert tvshow_cat == "TheLastShip"