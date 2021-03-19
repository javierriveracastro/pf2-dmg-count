# Pathfinder 2 damage count

A simple modules that shows the damage taken by a token with an overlay

It's mostly just a wild test to see if a module could be writen in Python

## Build Instructions

You will need to have Trasncrypt(https://transcrypt.org/) installed.

Just move to the root directory and run

`transcrypt main.py`

This will transpile the python code into javascipt into the py-src/__target__/ directory.

You should link this directory from pf2-dmg-count as script. In linux:

`ln -s py-src/__target__/ pdf2-dmg-count/scripts/`

Afterwards you only need to run transcrypt after each change or just setup your preferred IDE to do it automatically.