#!/usr/bin/python3

import unittest
import movietime

class TestMovieCatagory(unittest.TestCase):
    def runner(self, filename):
        MF = movietime.MyFile(filename)
        movie = movietime.Movies(MF.media)
        movie_cat = movie.catagory()
        return movie_cat
        
    def test_mov_cat_tremors(self):
        tremors_test_path = "/home/pi/taz/Movies/Tremors/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(tremors_test_path), "Tremors")
        
    def test_mov_cat_johnwick(self):
        johnwick_test_path = "/home/pi/taz/Movies/John Wick/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(johnwick_test_path), "John Wick")
        
    def test_mov_cat_johnwayne(self):
        johnwayne_test_path = "/home/pi/taz/Movies/John Wayne/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(johnwayne_test_path), "John Wayne")
        
    def test_mov_cat_harrypotter(self):
        harrypotter_test_path = "/home/pi/taz/Movies/Harry Potter/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(harrypotter_test_path), "Harry Potter")
        
    def test_mov_cat_jurassicpark(self):
        jurassicpark_test_path =  "/home/pi/taz/Movies/Jurassic Park/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(jurassicpark_test_path), "Jurassic Park")
        
    def test_mov_cat_meninblack(self):
        meninblack_test_path =  "/home/pi/taz/Movies/Men In Black/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(meninblack_test_path), "Men In Black")
        
    def test_mov_cat_scifi(self):
        scifi_test_path = "/home/pi/taz/Movies/SciFi/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(scifi_test_path), "SciFi")
        
    def test_mov_cat_action(self):
        action_test_path = "/home/pi/taz/Movies/Action/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(action_test_path), "Action")
            
    def test_mov_cat_comedy(self):
        comedy_test_path = "/home/pi/taz/Movies/Comedy/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(comedy_test_path), "Comedy")
    
    def test_mov_cat_drama(self):
        drama_test_path = "/home/pi/taz/Movies/Drama/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(drama_test_path), "Drama")
        
    def test_mov_cat_cartoons(self):
        cartoons_test_path = "/home/pi/taz/Movies/Cartoons/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(cartoons_test_path), "Cartoons")
        
    def test_mov_cat_godzilla(self):
        godzilla_test_path = "/home/pi/taz/Movies/Godzilla/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(godzilla_test_path), "Godzilla")
        
    def test_mov_cat_kingsman(self):
        kingsman_test_path = "/home/pi/taz/Movies/Kingsman/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(kingsman_test_path), "Kingsman")
        
    def test_mov_cat_startrek(self):
        startrek_test_path = "/home/pi/taz/Movies/StarTrek/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(startrek_test_path), "StarTrek")
        
    def test_mov_cat_starwars(self):
        starwars_test_path = "/home/pi/taz/Movies/StarWars/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(starwars_test_path), "StarWars")
        
    def test_mov_cat_superheros(self):
        superheros_test_path = "/home/pi/taz/Movies/SuperHeros/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(superheros_test_path), "SuperHeros")
        
    def test_mov_cat_indianajones(self):
        indianajones_test_path = "/home/pi/taz/Movies/IndianaJones/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(indianajones_test_path), "IndianaJones")
        
    def test_mov_cat_misc(self):
        misc_test_path = "/home/pi/taz/Movies/Misc/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(misc_test_path), "Misc")
        
    def test_mov_cat_none(self):
        none_test_path = "/home/pi/taz/Movies/Voodoo/Some Made Up Movie (2018).mp4"
        self.assertEqual(self.runner(none_test_path), "Misc")
    
