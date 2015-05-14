# Trim Filename

[![Stories in Ready](https://badge.waffle.io/tanjot/trimfilename.svg?label=ready&title=Ready)](http://waffle.io/tanjot/trimfilename)

A script to trim a specific pattern from filenames.  
Files are recursively checked for a pattern match on the path user mentions.

####Usage

```sh

[03:12:09] [~/code/trim_filename/songs] [master *] $ ls                                                                                                                                      [3:12:09]
01_rihanna___rude_boy.mp3  05 Flo Rida - Whistle.mp3
David Archuleta - A Little Too Not Over You.mp3  Nelly - Just A Dream 2010.mp3

[03:12:14] [~/code/trim_filename] [master *] $ ./trimfilename_run.py songs                                                                                                             [3:12:14]
songs
Files renamed:
songs/01_rihanna___rude_boy.mp3 : rihanna___rude_boy.mp3
songs/05 Flo Rida - Whistle.mp3 : Flo Rida - Whistle.mp3
Successfully rename 2 file/s


[03:13:18] [~/code/trim_filename/songs/thumbs] [master *] $ ls                                                                                                                                      [3:13:18]
AlbumArt_Adele_Large.jpg  AlbumArt_hall_of_fame_Large.jpg  AlbumArt_lotavo_Large.jpg

[03:14:04] [~/code/trim_filename] [master *] $ ./trimfilename_run.py thumbs -pb AlbumArt_                                                                                        [3:14:04]
thumbs
Entered parseDirfnamesongs/thumbs
Files renamed:
songs/thumbs/AlbumArt_hall_of_fame_Large.jpg : hall_of_fame_Large.jpg
songs/thumbs/AlbumArt_Adele_Large.jpg : Adele_Large.jpg
songs/thumbs/AlbumArt_lotavo_Large.jpg : lotavo_Large.jpg
Successfully rename 3 file/s


[03:22:45] [~/code/trim_filename] [master *] $ ./trimfilename_run.py thumbs -p _Large                                                                                                             [3:22:45]
thumbs
Entered parseDirfnamesongs/thumbs
Files renamed:
songs/thumbs/lotavo_Large.jpg : lotavo.jpg
songs/thumbs/hall_of_fame_Large.jpg : hall_of_fame.jpg
songs/thumbs/Adele_Large.jpg : Adele.jpg
Successfully rename 3 file/s

```