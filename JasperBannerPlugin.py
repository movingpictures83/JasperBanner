# coding: utf-8
# ---------------------------------------------------------------------------------------------------------------------
#
#                                       Florida International University
#
#   This software is a "Camilo Valdes Work" under the terms of the United States Copyright Act.
#   Please cite the author(s) in any work or product based on this material.
#
#   OBJECTIVE:
#	The purpose of this file is to implement helper functions and miscellaneous utility methods that are used by Flint.
#
#
#   NOTES:
#   Please see the dependencies section below for the required libraries (if any).
#
#   DEPENDENCIES:
#
#       • Python & the modules listed below
#
#   You can check the python modules currently installed in your system by running: python -c "help('modules')"
#
#   USAGE:
#       Run the program with the "--help" flag to see usage instructions.
#
#	AUTHOR:
#           Camilo Valdes (camilo@castflyer.com)
#			Florida International University (FIU)
#
#
# ---------------------------------------------------------------------------------------------------------------------

# 	Python Modules
import os, sys
import time
import multiprocessing
import plugins.Banner.BannerPlugin as BannerPlugin

class JasperBannerPlugin(BannerPlugin.BannerPlugin):
   def input(self, infile):
        self.__VERSION__ = 'B1'
        self.__BUILD_NUMBER__ = '2023021075'

   def printPrettyHeader(self):
    print(" ───────────────────────────────────────────────────────────────────────────────")
    print("   _____ _______ _______  _____  _______  ______        Version " + self.getVersion() +
          "." + self.getBuildNumber() + "")
    print("     |   |_____| |______ |_____] |______ |_____/                Jasper")
    print("   __|   |     | ______| |       |______ |    \_         ______(BETA)_______")
    print("                                                                              ")
    print("   https://github.com/camilo-v/jasper                               ")
    print(" ───────────────────────────────────────────────────────────────────────────────")




