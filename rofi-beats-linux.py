#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:54:58 2022

@author: GoodGuyPat

Created based on rofi-beats by Carbon-Bl4ck (https://github.com/Carbon-Bl4ck/Rofi-Beats/blob/main/rofi-beats-linux)
"""

60s.m3u
70s.m3u
80s.m3u
90s.m3u
acid_jazz.m3u
african.m3u
alternative.m3u
ambient.m3u
americana.m3u
anime.m3u
arabic.m3u
asian.m3u
big_band.m3u
blackmetal.m3u
bluegrass.m3u
blues.m3u
breakbeat.m3u
chillout.m3u
christian.m3u
classical.m3u
club.m3u
college.m3u
comedy.m3u
country.m3u
dance.m3u
deutsch.m3u
discofox.m3u
disco.m3u
downtempo.m3u
drum_and_bass.m3u
easy_listening.m3u
ebm.m3u
electronic.m3u
eurodance.m3u
film.m3u
folk.m3u
france.m3u
funk.m3u
goa.m3u
gospel.m3u
gothic.m3u
greek.m3u
hardcore.m3u
hardrock.m3u
hip_hop.m3u
house.m3u
india.m3u
indie.m3u
industrial.m3u
instrumental.m3u
italian.m3u
jazz.m3u
jpop.m3u
jungle.m3u
latin.m3u
lounge.m3u
metal.m3u
mixed.m3u
musical.m3u
oldies.m3u
opera.m3u
polish.m3u
polka.m3u
pop.m3u
portugal.m3u
progressive.m3u
punk.m3u
quran.m3u
rap.m3u
reggae.m3u
retro.m3u
rnb.m3u
rock.m3u
romanian.m3u
russian.m3u
salsa.m3u
schlager.m3u
ska.m3u
smooth_jazz.m3u
soul.m3u
soundtrack.m3u
spain.m3u
spiritual.m3u
sport.m3u
swing.m3u
symphonic.m3u
talk.m3u
techno.m3u
top_40.m3u
trance.m3u
turk.m3u
urban.m3u
usa.m3u
various.m3u
wave.m3u
w

import os
import subprocess as s

radios = {
"1. Lofi Girl":{
"notification": "Lofi Girl ☕️🎶",
"URL":"https://play.streamafrica.net/lofiradio"},
"2. Chillhop":{
"notification": "Chillhop ☕️🎶",
"URL":"http://stream.zeno.fm/fyn8eh3h5f8uv"},
"3. Box Lofi":{
"notification": "Box Lofi ☕️🎶",
"URL":"http://stream.zeno.fm/f3wvbbqmdg8uv"},
"4. The Bootleg Boy":{
"notification": "The Bootleg Boy ☕️🎶",
"URL":"http://stream.zeno.fm/0r0xa792kwzuv"},
"5. Radio Spinner":{
"notification": "Radio Spinner ☕️🎶",
"URL":"https://live.radiospinner.com/lofi-hip-hop-64"},
"6. SmoothChill":{
"notification": "SmoothChill ☕️🎶",
"URL":"https://media-ssl.musicradio.com/SmoothChill"},
"7. Smooth Jazz":{
"notification": "Smooth Jazz ☕️🎶",
"URL":"$MUSIC_PATHsmoothjazz.mp3"},
"8. Black Metal":{
"notification": "Black Metal ☕️🎶",
"URL":"$MUSIC_PATH/blackmetal.m3u"},
"9. 60s":{
"notification": "60s ☕️🎶",
"URL":"$MUSIC_PATH/60s.m3u"},
"10. 70s":{
"notification": "70s ☕️🎶",
"URL":"$MUSIC_PATH/70s.m3u"},
"11. 80s":{
"notification": "80s ☕️🎶",
"URL":"$MUSIC_PATH/80s.m3u"},
"12. 90s":{
"notification": "90s ☕️🎶",
"URL":"$MUSIC_PATH/90s.m3u"},
"13. Acid_jazz":{
"notification": "acid_jazz ☕️🎶",
"URL":"$MUSIC_PATH/acid_jazz.m3u"},
"14. African":{
"notification": "african ☕️🎶",
"URL":"$MUSIC_PATH/african.m3u"},
"15. Alternative":{
"notification": "alternative ☕️🎶",
"URL":"$MUSIC_PATH/alternative.m3u"},
"16. Ambient":{
"notification": "ambient ☕️🎶",
"URL":"$MUSIC_PATH/ambient.m3u"},
"17. Americana":{
"notification": "americana ☕️🎶",
"URL":"$MUSIC_PATH/.mamericana3u"},
"18. Anime":{
"notification": "anime ☕️🎶",
"URL":"$MUSIC_PATH/anime.m3u"},
"19. Arabic":{
"notification": "arabic ☕️🎶",
"URL":"$MUSIC_PATH/arabic.m3u"},
"20. Asian":{
"notification": "asian ☕️🎶",
"URL":"$MUSIC_PATH/asian.m3u"},
"21. Big_band":{
"notification": "big_band ☕️🎶",
"URL":"$MUSIC_PATH/big_band.m3u"},
"22. Blackmetal":{
"notification": "blackmetal ☕️🎶",
"URL":"$MUSIC_PATH/blackmetal.m3u"},
"23. Bluegrass":{
"notification": "bluegrass ☕️🎶",
"URL":"$MUSIC_PATH/bluegrass.m3u"},
"24. Blues":{
"notification": "blues ☕️🎶",
"URL":"$MUSIC_PATH/blues.m3u"},
"25. Breakbeat":{
"notification": "breakbeat ☕️🎶",
"URL":"$MUSIC_PATH/breakbeat.m3u"},
"26. Chillout":{
"notification": "chillout ☕️🎶",
"URL":"$MUSIC_PATH/chillout.m3u"},
"27. Christian":{
"notification": "christian ☕️🎶",
"URL":"$MUSIC_PATH/christian.m3u"},
"28. Classical":{
"notification": "classical ☕️🎶",
"URL":"$MUSIC_PATH/classical.m3u"},
"29. Club":{
"notification": "club ☕️🎶",
"URL":"$MUSIC_PATH/club.m3u"},
"30. College":{
"notification": "college ☕️🎶",
"URL":"$MUSIC_PATH/college.m3u"},
"31. Comedy":{
"notification": "comedy ☕️🎶",
"URL":"$MUSIC_PATH/comedy.m3u"},
"32. Country":{
"notification": "country ☕️🎶",
"URL":"$MUSIC_PATH/country.m3u"},
"33. Dance":{
"notification": "dance ☕️🎶",
"URL":"$MUSIC_PATH/dance.m3u"},
"34. Deutsch":{
"notification": "deutsch ☕️🎶",
"URL":"$MUSIC_PATH/deutsch.m3u"},
"35. Discofox":{
"notification": "discofox ☕️🎶",
"URL":"$MUSIC_PATH/discofox.m3u"},
"36. Disco":{
"notification": "disco ☕️🎶",
"URL":"$MUSIC_PATH/disco.m3u"},
"37. Downtempo":{
"notification": "downtempo ☕️🎶",
"URL":"$MUSIC_PATH/.mdowntempo3u"},
"38. Drum_and_bass":{
"notification": "drum_and_bass ☕️🎶",
"URL":"$MUSIC_PATH/drum_and_bass.m3u"},
"39. Easy_listening":{
"notification": "easy_listening ☕️🎶",
"URL":"$MUSIC_PATH/easy_listening.m3u"},
"40. Ebm":{
"notification": "ebm ☕️🎶",
"URL":"$MUSIC_PATHMebmusic/PlaylistFiles/ebm.m3u"},
"41. Electronic":{
"notification": "electronic ☕️🎶",
"URL":"$MUSIC_PATH/electronic.m3u"},
"42. Eurodance":{
"notification": "eurodance ☕️🎶",
"URL":"$MUSIC_PATH/eurodance.m3u"},
"43. Film":{
"notification": "film ☕️🎶",
"URL":"$MUSIC_PATH/film.m3u"},
"44. Folk":{
"notification": "folk ☕️🎶",
"URL":"$MUSIC_PATH/folk.m3u"},
"45. France":{
"notification": "france ☕️🎶",
"URL":"$MUSIC_PATH/france.m3u"},
"46. Funk":{
"notification": "funk ☕️🎶",
"URL":"$MUSIC_PATH/funk.m3u"},
"47. Goa":{
"notification": "goa ☕️🎶",
"URL":"$MUSIC_PATH/goa.m3u"},
"48. Gospel":{
"notification": "gospel ☕️🎶",
"URL":"$MUSIC_PATH/gospel.m3u"},
"49. Gothic":{
"notification": "gothic ☕️🎶",
"URL":"$MUSIC_PATH/gothic.m3u"},
"50. Greek":{
"notification": "greek ☕️🎶",
"URL":"$MUSIC_PATH/greek.m3u"},
"51. Hardcore":{
"notification": "hardcore ☕️🎶",
"URL":"$MUSIC_PATH/hardcore.m3u"},
"52. Hardrock":{
"notification": "hardrock ☕️🎶",
"URL":"$MUSIC_PATH/hardrock.m3u"},
"53. Hip_hop":{
"notification": "hip_hop ☕️🎶",
"URL":"$MUSIC_PATH/hip_hop.m3u"},
"54. House":{
"notification": "house ☕️🎶",
"URL":"$MUSIC_PATH/house.m3u"},
"55. Index":{
"notification": "index ☕️🎶",
"URL":"$MUSIC_PATH/index.m3u"},
"56. India":{
"notification": "india ☕️🎶",
"URL":"$MUSIC_PATH/india.m3u"},
"57. Indie":{
"notification": "indie ☕️🎶",
"URL":"$MUSIC_PATH/indie.m3u"},
"58. Industrial":{
"notification": "industrial ☕️🎶",
"URL":"$MUSIC_PATH/.mindustrial3u"},
"59. Instrumental":{
"notification": "instrumental ☕️🎶",
"URL":"$MUSIC_PATH/instrumental.m3u"},
"60. Italian":{
"notification": "italian ☕️🎶",
"URL":"$MUSIC_PATH/italian.m3u"},
"61. Jazz":{
"notification": "jazz ☕️🎶",
"URL":"$MUSIC_PATH/jazz.m3u"},
"62. Jpop":{
"notification": "jpop ☕️🎶",
"URL":"$MUSIC_PATH/jpop.m3u"},
"63. Jungle":{
"notification": "jungle ☕️🎶",
"URL":"$MUSIC_PATH/jungle.m3u"},
"64. Latin":{
"notification": "latin ☕️🎶",
"URL":"$MUSIC_PATH/latin.m3u"},
"65. Lounge":{
"notification": "lounge ☕️🎶",
"URL":"$MUSIC_PATH/lounge.m3u"},
"66. Metal":{
"notification": "metal ☕️🎶",
"URL":"$MUSIC_PATH/metal.m3u"},
"67. Mixed":{
"notification": "mixed ☕️🎶",
"URL":"$MUSIC_PATH/mixed.m3u"},
"68. Musical":{
"notification": "musical ☕️🎶",
"URL":"$MUSIC_PATH/musical.m3u"},
"69. Oldies":{
"notification": "oldies ☕️🎶",
"URL":"$MUSIC_PATH/oldies.m3u"},
"70. Opera":{
"notification": "opera ☕️🎶",
"URL":"$MUSIC_PATH/opera.m3u"},
"71. Polish":{
"notification": "polish ☕️🎶",
"URL":"$MUSIC_PATH/polish.m3u"},
"72. Polka":{
"notification": "polka ☕️🎶",
"URL":"$MUSIC_PATH/polka.m3u"},
"73. Pop":{
"notification": "pop ☕️🎶",
"URL":"$MUSIC_PATH/pop.m3u"},
"74. Portugal":{
"notification": "portugal ☕️🎶",
"URL":"$MUSIC_PATH/portugal.m3u"},
"75. Progressive":{
"notification": "progressive ☕️🎶",
"URL":"$MUSIC_PATH/progressive.m3u"},
"76. Punk":{
"notification": "punk ☕️🎶",
"URL":"$MUSIC_PATH/punk.m3u"},
"77. Quran":{
"notification": "quran ☕️🎶",
"URL":"$MUSIC_PATH/quran.m3u"},
"78. Rap":{
"notification": "rap ☕️🎶",
"URL":"$MUSIC_PATH/rap.m3u"},
"79. README":{
"notification": "README ☕️🎶",
"URL":"$MUSIC_PATH/README.m3u"},
"80. Reggae":{
"notification": "reggae ☕️🎶",
"URL":"$MUSIC_PATH/reggae.m3u"},
"81. Retro":{
"notification": "retro ☕️🎶",
"URL":"$MUSIC_PATH/retro.m3u"},
"82. Rnb":{
"notification": "rnb ☕️🎶",
"URL":"$MUSIC_PATH/rnb.m3u"},
"83. Rock":{
"notification": "rock ☕️🎶",
"URL":"$MUSIC_PATH/rock.m3u"},
"84. Romanian":{
"notification": "romanian ☕️🎶",
"URL":"$MUSIC_PATH/romanian.m3u"},
"85. Russian":{
"notification": "russian ☕️🎶",
"URL":"$MUSIC_PATH/russian.m3u"},
"86. Salsa":{
"notification": "salsa ☕️🎶",
"URL":"$MUSIC_PATH/salsa.m3u"},
"87. Schlager":{
"notification": "schlager ☕️🎶",
"URL":"$MUSIC_PATH/schlager.m3u"},
"88. Ska":{
"notification": "ska ☕️🎶",
"URL":"$MUSIC_PATH/ska.m3u"},
"89. Smooth_jazz":{
"notification": "smooth_jazz ☕️🎶",
"URL":"$MUSIC_PATH/smooth_jazz.m3u"},
"90. Soul":{
"notification": "soul ☕️🎶",
"URL":"$MUSIC_PATH/soul.m3u"},
"91. Soundtrack":{
"notification": "soundtrack ☕️🎶",
"URL":"$MUSIC_PATH/soundtrack.m3u"},
"92. Spain":{
"notification": "spain ☕️🎶",
"URL":"$MUSIC_PATH/spain.m3u"},
"93. Spiritual":{
"notification": "spiritual ☕️🎶",
"URL":"$MUSIC_PATH/spiritual.m3u"},
"94. Sport":{
"notification": "sport ☕️🎶",
"URL":"$MUSIC_PATH/sport.m3u"},
"95. Swing":{
"notification": "swing ☕️🎶",
"URL":"$MUSIC_PATH/swing.m3u"},
"96. Symphonic":{
"notification": "symphonic ☕️🎶",
"URL":"$MUSIC_PATH/symphonic.m3u"},
"97. Talk":{
"notification": "talk ☕️🎶",
"URL":"$MUSIC_PATH/talk.m3u"},
"98. Techno":{
"notification": "techno ☕️🎶",
"URL":"$MUSIC_PATH/techno.m3u"},
"99. Top_40":{
"notification": "top_40 ☕️🎶",
"URL":"$MUSIC_PATH/top_40.m3u"},
"100. Trance":{
"notification": "trance ☕️🎶",
"URL":"$MUSIC_PATH/trance.m3u"},
"101. Turk":{
"notification": "turk ☕️🎶",
"URL":"$MUSIC_PATH/turk.m3u"},
"102. Urban":{
"notification": "urban ☕️🎶",
"URL":"$MUSIC_PATH/urban.m3u"},
"103. Usa":{
"notification": "usa ☕️🎶",
"URL":"$MUSIC_PATH/usa.m3u"},
"104. Various":{
"notification": "various ☕️🎶",
"URL":"$MUSIC_PATH/various.m3u"},
"105. Wave":{
"notification": "wave ☕️🎶",
"URL":"$MUSIC_PATH/wave.m3u"},
"106. World":{
"notification": "world ☕️🎶",
"URL":"$MUSIC_PATH/world.m3u"}
}

choices = []

for i in radios:
    choices.append(i)

choicelist = "\n".join(choices)
  
p1 = s.Popen(["echo", choicelist], stdout=s.PIPE)
p2 = s.Popen(["rofi", "-dmenu", "-i"], stdin=p1.stdout, stdout=s.PIPE)
p1.stdout.close()

output = p2.communicate()[0].decode()[:-1]

if output in radios:
    url = radios[output]['URL']

try:
    s.run(['pkill, mpv'])
except:
    pass

s.run(["mpv",f"{url}"])

s.run(["notify-send","Playing now: \"{radios[output]['notification']}\"","--icon=media-tape"])

