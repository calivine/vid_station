===========
vid_station
===========

vid_station is a command line video editing package.
----------------------------------------------------

Installation:

``pip install vidstation``

Usage:

``vedit FILENAME OPTIONS``

Options:

``-g, --gif     Save file as GIF``

``-w, --webm    Save file as webm``

``-a, -auto     Auto-edit file down to summary clip.``

``-f, --file   Perform actions on a batch file. Usage: vedit -b FILE.txt OPTIONS``

``-c, --clips   Include custom timestamps to edit video on. Usage: vedit FILENAME -c [ts1start, ts1end, ...]``
