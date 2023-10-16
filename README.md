# timestampsplitter
Program that vertically splits a *.musicxml file by the timestamp added by mpvplaytime.

## Input
Receives a path of a MusicXML file as a command line argument and it splits the score based on the <words> tag with text in format PT:X where X is the elapsed time in seconds.

## Note
The program should keep tempo, staff, and clef information on each cut.
The program should create a new MusicXML file for each cut.
The name of each new partial file should be the same as the original file with the addition of the cut number. For example, if the original file is named "song.musicxml", the new files should be named "song_1.musicxml", "song_2.musicxml", etc.
