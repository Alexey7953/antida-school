import songdetails
song = songdetails.scan("blah.mp3")
if song is not None:
    print (song.artist)