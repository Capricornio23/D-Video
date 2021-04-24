#!/usr/bin/python2

import youtube_dl
import pafy
import time
import sys
import os

def venom(s):
  for p in s + "\n":
    sys.stdout.write(p)
    sys.stdout.flush()
    time.sleep(1./70)

os.system("clear")
print ("\n")
venom ("""

\033[35m  _____                             _    _
 (_____)                           (_)  (_)
 (_)  (_) ______   __   __   ____  (_)__(_)_
 (_)  (_)(______) (__)_(__) (____) (________)
 (_)__(_)        (_) (_) (_)(_)_(_)     (_)
 (_____)         (_) (_) (_)(____)      (_)
                            (_)
                            (_)

\n""")
venom("\033[31m[\033[33m*\033[31m]\033[32m Create by Capricornio23 :v  \n")
url = input("\033[31m[\033[33m*\033[31m]\033[34m Ingrese la URL: ")
video = pafy.new(url)

videostrams = video.streams
for i in videostrams:
  print(i)

best = video.getbest()
if(best):
  venom("\033[32m Iniciando descarga")
  venom("\033[32m Descargando video...")
  print(best.resolution, best.extension)

best.download()
venom("\033[36m Vídeo descargado")

