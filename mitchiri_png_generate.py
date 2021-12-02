#!/usr/bin/env python3

# Original Mitchiri Neko March has the following animation sequences:
#
# L = Lead
# D = Drum ['d' with stick rotation, 'n' with fans]
# F = Flute ['f' with two flutes, 'y' with yoyo]
# G = Guitar ['g' for guitar backwards, 'w' for a witch broom]
# T = Tambourine ['t' with thrombone, 'j' with joggling]
# X = Xylo ['x' with rotation]
# C = Cymbal ['c' with eating, 'e' with eating another thing]
# R = Triangle ['o' with phone]
# U = Tuba ['u' with a cat inside, 'b' with a bird]
# A = Accordion ['a' with a bird, 'h' with a hat]
# B = Bass drum
# S = Singer
# I = Lead in the interlude ['i' with different animation]
# H = Harp
#
# This script will generate all of these animations.
# If you need more, just add it to the 'animations' string.
#
# Note 1: you may resize image when edit. Anchor is top-left.
# Note 2: on Windows, file names are case insensitive, so you get
#         weird results if you use different cases of a single
#         letter (as it is now). You shall change that in the
#         'animations' variable.

animations = 'LDFGTXCRUABSIHdnfygwtjxceoubahi'

from PIL import Image, ImageDraw, ImageFont, ImageFile

def try_load_any_font(fonts):
    for fontname in fonts:
        try:
            font = ImageFont.truetype(fontname, 80)
            font.set_variation_by_name('Bold')
            break
        except OSError:
            continue
    try:
        return font
    except NameError:
        raise ValueError('No applicable fonts found.') from None

font = try_load_any_font(['Linux Biolinum', 'Helvetica', 'Arial', 'Sans Serif'])
for filename in list(animations):
    for frame in range(8):
        shift = frame * 8
        img = Image.new('RGBA', (265, 200))
        canvas = ImageDraw.Draw(img)
        canvas.rectangle([2 + shift, 2, 198 + shift, 198], fill = None, outline = 'black', width = 2)
        canvas.text((10 + shift, 60), filename + str(frame), font = font, fill = 'black')
        img.save(filename + str(frame) + '.png')
