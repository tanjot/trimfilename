# Trim Filename

[![Stories in Ready](https://badge.waffle.io/tanjot/trimfilename.svg?label=ready&title=Ready)](http://waffle.io/tanjot/trimfilename)

A script to trim a specific pattern from filenames.

Files are recursively checked for a pattern match on the path mentioned or in current working directory.

####Usage

```sh

home $ ls songs
04_maroon5_she_will_be_loved.mp3        05 Flo Rida-Whistle.mp3
Nelly-Just A Dream 2010.mp3             David Archuleta - A Little Too Not Over You000.mp3


home $ trimfilename songs
parsing directory: songs
Files renamed:
songs/04_maroon5_she_will_be_loved.mp3    : maroon5_-_she_will_be_loved-tn.mp3
songs/05 Flo Rida-Whistle.mp3             : Flo Rida - Whistle.mp3

Successfully renamed 2 file/s


home $ ls thumbs
AlbumArt_Adele_Large.jpg  AlbumArt_hall_of_fame_Large.jpg  AlbumArt_lotavo_Large.jpg


home $ trimfilename thumbs -b AlbumArt_
parsing directory: thumbs
Files renamed:
thumbs/AlbumArt_Adele_Large.jpg        : Adele_Large.jpg
thumbs/AlbumArt_hall_of_fame_Large.jpg : hall_of_fame_Large.jpg
thumbs/AlbumArt_lotavo_Large.jpg       : lotavo_Large.jpg

Successfully renamed 3 file/s


home $ ls thumbs
Adele_Large.jpg  hall_of_fame_Large.jpg  lotavo_Large.jpg


home $ trimfilename thumbs -p _large -i
parsing directory: thumbs
Files renamed:
thumbs/lotavo_Large.jpg       : lotavo.jpg
thumbs/hall_of_fame_Large.jpg : hall_of_fame.jpg
thumbs/Adele_Large.jpg        : Adele.jpg

Successfully renamed 3 file/s

```