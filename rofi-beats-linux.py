#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:54:58 2022

@author: GoodGuyPat

Created based on rofi-beats by Carbon-Bl4ck (https://github.com/Carbon-Bl4ck/Rofi-Beats/blob/main/rofi-beats-linux).
Added piping of mpv's ouptput to allow it to be captured by other programs. The last line will contain the title of
the currently played song, if any, with the prefix 'icy-title'. This can be useful to display the currently
played song in a status bar, for example (tested with Waybar). It is also automatically connected to a socket
so that it can be contolled externally (for example, by sending a play/pause command via 
`echo '{ "command": ["cycle", "pause"] }' | socat - /tmp/mpvsocket`
)
"""
# Import modules. There are all built-in in Python3

import subprocess as s
from pathlib import Path
import sys

# List all our radio stations

radios = {
"Lofi Girl":{
"notification": "Lofi Girl ☕️🎶",
"URL":"https://play.streamafrica.net/lofiradio"},
"Chillhop":{
"notification": "Chillhop ☕️🎶",
"URL":"http://stream.zeno.fm/fyn8eh3h5f8uv"},
"Box Lofi":{
"notification": "Box Lofi ☕️🎶",
"URL":"http://stream.zeno.fm/f3wvbbqmdg8uv"},
"The Bootleg Boy":{
"notification": "The Bootleg Boy ☕️🎶",
"URL":"http://stream.zeno.fm/0r0xa792kwzuv"},
"Radio Spinner":{
"notification": "Radio Spinner ☕️🎶",
"URL":"https://live.radiospinner.com/lofi-hip-hop-64"},
"SmoothChill":{
"notification": "SmoothChill ☕️🎶",
"URL":"https://media-ssl.musicradio.com/SmoothChill"},
"Black Metal":{
"notification": "Black Metal ☕️🎶",
"URL":"http://trueblackmetalradio.com:666/radio"},
"60s":{
"notification": "60s ☕️🎶",
"URL":"http://64.40.99.76:8000/stream/1/"},
"70s":{
"notification": "70s ☕️🎶",
"URL":"http://hydra.cdnstream.com/1823_128"},
"80s":{
"notification": "80s ☕️🎶",
"URL":"https://orf-live.ors-shoutcast.at/oe3-q2a"},
"90s":{
"notification": "90s ☕️🎶",
"URL":"https://orf-live.ors-shoutcast.at/oe3-q2a"},
"Acid_jazz":{
"notification": "acid_jazz ☕️🎶",
"URL":"http://138.201.83.14:8010/stream/1/"},
"African":{
"notification": "african ☕️🎶",
"URL":"http://192.95.18.39:5127/stream/1/"},
"Alternative":{
"notification": "alternative ☕️🎶",
"URL":"http://107.155.111.170:8440"},
"Ambient":{
"notification": "ambient ☕️🎶",
"URL":"http://starfrosch.ch:8000/stream"},
"Americana":{
"notification": "americana ☕️🎶",
"URL":"http://51.222.8.101:8000/stream/1/"},
"Anime":{
"notification": "anime ☕️🎶",
"URL":"http://hi5.streamingsoundtracks.com:80"},
"Arabic":{
"notification": "arabic ☕️🎶",
"URL":"http://radioshamfm.grtvstream.com:8400/stream/1/"},
"Asian":{
"notification": "asian ☕️🎶",
"URL":"http://desi.canstream.co.uk:8001/live.mp3"},
"Big_band":{
"notification": "big_band ☕️🎶",
"URL":"http://199.189.111.28:8012"},
"Bluegrass":{
"notification": "bluegrass ☕️🎶",
"URL":"http://streams.abidingradio.org:7840/1_autodj"},
"Blues":{
"notification": "blues ☕️🎶",
"URL":"http://87.118.126.101:19406/stream/1/"},
"Breakbeat":{
"notification": "breakbeat ☕️🎶",
"URL":"http://www.drums.ro:8000"},
"Chillout":{
"notification": "chillout ☕️🎶",
"URL":"http://hirschmilch.de:7000/stream/4/"},
"Christian":{
"notification": "christian ☕️🎶",
"URL":"http://ic2.christiannetcast.com/kxta-fm"},
"Classical":{
"notification": "classical ☕️🎶",
"URL":"http://uk2.streamingpulse.com:8010/stream/1/"},
"Club":{
"notification": "club ☕️🎶",
"URL":"http://stream2.dancewave.online:8080/dance.mp3"},
"College":{
"notification": "college ☕️🎶",
"URL":"http://ice1.somafm.com/indiepop-128-mp3"},
"Comedy":{
"notification": "comedy ☕️🎶",
"URL":"http://live.topfm.hu:8000/comedy.mp3"},
"Country":{
"notification": "country ☕️🎶",
"URL":"http://87.118.126.101:19406/stream/1/"},
"Dance":{
"notification": "dance ☕️🎶",
"URL":"http://online.kissfm.ua/KissFM"},
"Deutsch":{
"notification": "deutsch ☕️🎶",
"URL":"http://pool.radiopaloma.de/RADIOPALOMA.mp3"},
"Discofox":{
"notification": "discofox ☕️🎶",
"URL":"https://s37.derstream.net/afr128.mp3"},
"Disco":{
"notification": "disco ☕️🎶",
"URL":"http://kunc.streamguys1.com/kjac"},
"Drum_and_bass":{
"notification": "drum_and_bass ☕️🎶",
"URL":"http://193.0.98.66:8005/stream/1/"},
"Easy_listening":{
"notification": "easy_listening ☕️🎶",
"URL":"http://stream.soundstorm-radio.com:8000/stream/1/"},
"Ebm":{
"notification": "ebm ☕️🎶",
"URL":"http://www.ebm-radio.org:7000/stream/1/"},
"Electronic":{
"notification": "electronic ☕️🎶",
"URL":"http://stream2.dancewave.online:8080/dance.mp3"},
"Eurodance":{
"notification": "eurodance ☕️🎶",
"URL":"http://89.39.189.52:8000/stream/1/"},
"Film":{
"notification": "film ☕️🎶",
"URL":"http://94.23.51.96:8001"},
"Folk":{
"notification": "folk ☕️🎶",
"URL":"http://live.narodni.hr:8059/stream/1/"},
"France":{
"notification": "france ☕️🎶",
"URL":"http://stream.lazaradio.com:8100/live.mp3"},
"Funk":{
"notification": "funk ☕️🎶",
"URL":"http://91.121.104.123:8000/stream/1/"},
"Goa":{
"notification": "goa ☕️🎶",
"URL":"http://cast.magicstreams.gr:9111/stream/1/"},
"Gospel":{
"notification": "gospel ☕️🎶",
"URL":"http://ic2.christiannetcast.com/kxta-fm"},
"Gothic":{
"notification": "gothic ☕️🎶",
"URL":"http://162.213.197.52:80"},
"Greek":{
"notification": "greek ☕️🎶",
"URL":"http://sokfm.lalala.gr:8000/stream/1/"},
"Hardcore":{
"notification": "hardcore ☕️🎶",
"URL":"http://173.245.78.93:80"},
"Hardrock":{
"notification": "hardrock ☕️🎶",
"URL":"http://144.217.29.205:80/stream/1/"},
"Hip_hop":{
"notification": "hip_hop ☕️🎶",
"URL":"http://starfrosch.ch:8000/stream"},
"House":{
"notification": "house ☕️🎶",
"URL":"http://live.dancemusic.ro:7000/stream/1/"},
"India":{
"notification": "india ☕️🎶",
"URL":"http://cast2.asurahosting.com:8569/stream/1/"},
"Indie":{
"notification": "indie ☕️🎶",
"URL":"http://b.fmradiomanele.ro:8044/stream/1/"},
"Industrial":{
"notification": "industrial ☕️🎶",
"URL":"http://mp3.stream.tb-group.fm:80/ct.mp3"},
"Instrumental":{
"notification": "instrumental ☕️🎶",
"URL":"http://199.233.234.34:25373/stream/1/"},
"Italian":{
"notification": "italian ☕️🎶",
"URL":"http://uk2.streamingpulse.com:8010/stream/1/"},
"Jazz":{
"notification": "jazz ☕️🎶",
"URL":"http://64.95.243.43:8002/stream/1/"},
"Jpop":{
"notification": "jpop ☕️🎶",
"URL":"https://igor.torontocast.com:1025/stream/1/"},
"Jungle":{
"notification": "jungle ☕️🎶",
"URL":"http://andromeda.shoutca.st:8031/stream/1/"},
"Latin":{
"notification": "latin ☕️🎶",
"URL":"http://radiopetrecaretzu.zapto.org:8383/stream/1/"},
"Lounge":{
"notification": "lounge ☕️🎶",
"URL":"http://larry.torontocast.com:1820/stream/1/"},
"Metal":{
"notification": "metal ☕️🎶",
"URL":"http://173.245.78.93:80"},
"Mixed":{
"notification": "mixed ☕️🎶",
"URL":"http://centova16.ciclanohost.com.br:9627/stream/1/"},
"Musical":{
"notification": "musical ☕️🎶",
"URL":"http://67.212.179.138:7102/stream/1/"},
"Oldies":{
"notification": "oldies ☕️🎶",
"URL":"http://b.fmradiomanele.ro:8044/stream/1/"},
"Opera":{
"notification": "opera ☕️🎶",
"URL":"http://stream.klassikradio.de/opera/mp3-128"},
"Polish":{
"notification": "polish ☕️🎶",
"URL":"http://stream4.nadaje.com:15476/radiobialystok"},
"Polka":{
"notification": "polka ☕️🎶",
"URL":"http://server-67.stream-server.nl:8910/autodj"},
"Pop":{
"notification": "pop ☕️🎶",
"URL":"http://stream.radioaktual.si/Aktual"},
"Portugal":{
"notification": "portugal ☕️🎶",
"URL":"http://195.23.85.126:8401/stream/1/"},
"Progressive":{
"notification": "progressive ☕️🎶",
"URL":"http://cast.magicstreams.gr:9111/stream/1/"},
"Punk":{
"notification": "punk ☕️🎶",
"URL":"http://stream.laut.fm/tax_free_radio"},
"Quran":{
"notification": "quran ☕️🎶",
"URL":"http://162.244.81.30:8224"},
"Rap":{
"notification": "rap ☕️🎶",
"URL":"http://185.23.192.118:8000/stream/1/"},
"Reggae":{
"notification": "reggae ☕️🎶",
"URL":"http://s02.whooshserver.net:9091/live.mp3"},
"Retro":{
"notification": "retro ☕️🎶",
"URL":"http://46.28.49.164:7504/autodj"},
"Rnb":{
"notification": "rnb ☕️🎶",
"URL":"http://radiopetrecaretzu.zapto.org:8383/stream/1/"},
"Rock":{
"notification": "rock ☕️🎶",
"URL":"http://b.fmradiomanele.ro:8044/stream/1/"},
"Romanian":{
"notification": "romanian ☕️🎶",
"URL":"http://live.guerrillaradio.ro:8010/guerrilla.aac"},
"Russian":{
"notification": "russian ☕️🎶",
"URL":"http://listen.rusongs.ru/ru-mp3-128"},
"Salsa":{
"notification": "salsa ☕️🎶",
"URL":"http://51.222.8.101:8000/stream/1/"},
"Schlager":{
"notification": "schlager ☕️🎶",
"URL":"http://pool.radiopaloma.de/RADIOPALOMA.mp3"},
"Ska":{
"notification": "ska ☕️🎶",
"URL":"http://stream.m-1.fm/lietus/aacp64"},
"Smooth_jazz":{
"notification": "smooth_jazz ☕️🎶",
"URL":"http://64.95.243.43:8002/stream/1/"},
"Soul":{
"notification": "soul ☕️🎶",
"URL":"http://stream01.superfly.fm:8080/live"},
"Soundtrack":{
"notification": "soundtrack ☕️🎶",
"URL":"http://94.23.51.96:8001"},
"Spain":{
"notification": "spain ☕️🎶",
"URL":"http://live.radiovoz.es/mp3/stream_coruna.mp3"},
"Spiritual":{
"notification": "spiritual ☕️🎶",
"URL":"http://ic2.christiannetcast.com/kxta-fm"},
"Sport":{
"notification": "sport ☕️🎶",
"URL":"http://144.140.228.109:8220/stream/1/"},
"Swing":{
"notification": "swing ☕️🎶",
"URL":"http://s6.voscast.com:11312/stream/1/"},
"Symphonic":{
"notification": "symphonic ☕️🎶",
"URL":"http://hi5.adagio.fm"},
"Talk":{
"notification": "talk ☕️🎶",
"URL":"https://lb0-stream.radiox981.ca/choi.aac"},
"Techno":{
"notification": "techno ☕️🎶",
"URL":"http://51.89.148.171:8022/stream/1/"},
"Top_40":{
"notification": "top_40 ☕️🎶",
"URL":"http://listen.rusongs.ru/ru-mp3-128"},
"Trance":{
"notification": "trance ☕️🎶",
"URL":"http://stream2.dancewave.online:8080/dance.mp3"},
"Turk":{
"notification": "turk ☕️🎶",
"URL":"http://37.247.98.8/stream/22/"},
"Urban":{
"notification": "urban ☕️🎶",
"URL":"http://51.222.8.101:8011/stream/1/"},
"Usa":{
"notification": "usa ☕️🎶",
"URL":"http://stream2.joyhits.online:8880/joyhits.aac"},
"Various":{
"notification": "various ☕️🎶",
"URL":"http://live.guerrillaradio.ro:8010/guerrilla.aac"},
"Wave":{
"notification": "wave ☕️🎶",
"URL":"http://stream2.dancewave.online:8080/dance.mp3"},
"World":{
"notification": "world ☕️🎶",
"URL":"http://starfrosch.ch:8000/stream"}
}

# Declare where the output of the player will be written, and its name. 
# By default it will be stored in the current user's home directory. 
# This output is only relevant if it is captured by other programs. 

output_file_dir = Path.home()
output_file_name = 'rofi-beats_out.txt'


# Dinamically add a numerical prefix to the radio stations based on the order
# they appear in the dictionary above. This is done to respect Carbon-Bl4ck's
# original format, and to allow users to edit the radio dictionary without
# needing to maintain the numbers in the station names.

choices = []
index = 0
for i in radios:
    index = index+1
    choices.append(f"{str(index)}. {i}")

# Compile list to be passed to Rofi

choicelist = "\n".join(choices)

# Pass list to Rofi and capture user input

p1 = s.Popen(["echo", choicelist], stdout=s.PIPE)
p2 = s.Popen(["rofi", "-dmenu", "-i"], stdin=p1.stdout, stdout=s.PIPE)
p1.stdout.close()

output = p2.communicate()[0].decode()[:-1]

# Remove the number we just added

cleanoutput = " ".join(output.split()[1:])

# If there is an error, notify user and stop execution

if cleanoutput in radios:
    url = radios[cleanoutput]['URL']
else:
    s.run(["notify-send","Station not found"])
    sys.exit()

# Try to close any current instance of mpv

try:
    s.run(['pkill','-f','radio-mpv'])
except:
    pass

# Clear existing output file if found. This is done so that the file does not
# get huge after many executions
print('1')
s.run(['rm',f"{output_file_dir}/{output_file_name}"])
print('2')
# Open player with URL of selected station, send notification, write output to
# file

with open(f"{output_file_dir}/{output_file_name}",'w') as f:
    print('3')
    s.run(["notify-send",f"Playing now: \"{radios[cleanoutput]['notification']}\"","--icon=media-tape"])
    print('4')
    s.run(["mpv",f"{url}","--idle=yes", "--volume=60", "--title=\"radio-mpv\"","--input-ipc-server=/tmp/mpvsocket"],stdout=f)

