# QMK_KeymapToAsciiTable
Python script, that get input from keymap.c and returns "comments.txt." "comments.txt" contains searched layers, and commented ascii table for each layer(s).


# How to use?
1. put script in the same path where your keymap.c file is.
2. execute the script (python2 not tested)
3. check generated "comments.txt" file

# What layout is supported?
Basically, any layouts! 
However, all keys will apear as 1u key, so it’s optimized for ortholinears, keep that in mind.

# Referenced Codes
Keycodes Dictionary by Rionlion100, https://github.com/Rionlion100/qmk-comment-gen/blob/master/qmk_kc.py
