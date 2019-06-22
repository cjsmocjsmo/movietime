#/usr/bin/python3
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
import configparser

class CfgParser:
    
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("./movietime.cfg")
        print(parser["Prog_Paths"]["NoArt"])
        os.environ["MT_THUMBNAILS"] = parser["Prog_Paths"]['Thumbnails']
        os.environ["MT_DBUSCONTROLPATH"] = parser["Prog_Paths"]["DBusControlPath"]
        os.environ["MT_NOART_PATH"] = parser["Prog_Paths"]["NoArt"]
        os.environ["MT_PICPATH"] = parser["Media_Paths"]["PicPath"]
        os.environ["MT_MEDIA_PATH_MOVIES"] = parser["Media_Paths"]["MediaPath_Movies"]
        os.environ["MT_MEDIA_PATH_TVSHOWS"] = parser["Media_Paths"]["MediaPath_TVshows"]
        os.environ["MT_USB_MEDIA_PATH"] = parser["Media_Paths"]["MediaPath_Usb"]
        os.environ["MT_MP4"] = parser["Extension_List"]["mp4"]
        os.environ["MT_M4V"] = parser["Extension_List"]["m4v"]
        os.environ["MT_MKV"] = parser["Extension_List"]["mkv"]
        os.environ["MT_AVI"] = parser["Extension_List"]["avi"]
        
    def create_media_list(self):
        return [os.environ["MT_MEDIA_PATH_MOVIES"], os.environ["MT_MEDIA_PATH_TVSHOWS"],
            os.environ["MT_USB_MEDIA_PATH"]]
            
    def create_extension_list(self):
        EXTLIST = []
        if os.environ["MT_MP4"]:
            EXTLIST.append(".mp4")
        if os.environ["MT_M4V"]:
            EXTLIST.append(".m4v")
        if os.environ["MT_MKV"]:
            EXTLIST.append(".mkv")
        if os.environ["MT_AVI"]:
            EXTLIST.append(".avi")
        return EXTLIST