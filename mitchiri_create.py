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
# Note 1: you may resize image when edit. Anchor is bottom-left.
# Note 2: on Windows, file names are case insensitive, so you get
#         weird results if you use different cases of a single
#         letter (as it is now). You shall change that in the
#         'animations' variable.

size = {'x': 1280, 'y': 720}
bgcolor = '#fffff2'

# Here's the definition of exact march performers!
# They are divided into five bunches. You may have an idea
# what animation is to be used if you check the corresponding
# letter.

bunch1 = 'AURXFFFTGDL'

bunch2 = 'gxAFdt'

# Then a bass drum ('B') cat goes

bunch3top = 'XaFtUc'
bunch3mid = 'XAfTUC'
bunch3btm = 'xAFTuC'

bunch4 = 'IIiII'

# Then a harper ('H') cat goes

bunch5top = 'btAy'
bunch5mid = 'UjAF'
bunch5btm = 'Uthf'

# Then a bass drum ('B') cat goes

bunch6top = 'dwRXC'
bunch6mid = 'DgoXe'
bunch6btm = 'nGRxC'

# Then two singer ('S') cat go

import av
from PIL import Image, ImageDraw

source = av.open('source.mp4', mode = 'r').decode(video=0) # or None if no back is needed
container = av.open('mitchiri.mp4', mode = 'w')
stream = container.add_stream('mpeg4', rate = 30)
stream.width = size['x']
stream.height = size['y']
stream.pix_fmt = 'yuv420p'

files_cache = {}

def cached(animation, phase):
    global files_cache
    filename = animation + str(phase) + '.png'
    if not filename in files_cache:
        files_cache[filename] = Image.open('images/' + filename)
    return files_cache[filename]

#def flush_cache():
#    for img in files_cache.values():
#        img.destroy()

def decode_frame_num(frame):
    seq = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7]
    phase = seq[frame % 19]
    offset = 65 * (frame // 19)
    return phase, offset

def alpha_composite(bottom, top, dest):
    lbound = 0
    rbound = bottom.width
    linsert = dest[0]
    rinsert = dest[0] + top.width
    if rinsert < lbound or linsert > rbound:
        return bottom
    elif linsert < lbound:
        bottom.alpha_composite(top, (lbound, dest[1]), (lbound - linsert, 0, top.width, top.height))
    elif rinsert > rbound:
        bottom.alpha_composite(top, dest, (0, 0, rbound - linsert, top.height))
    else:
        bottom.alpha_composite(top, dest)
    return bottom

def mitchiri_march(img, frame, animation, position, level = 0):
    phase, offset = decode_frame_num(frame)
    overlay = cached(animation, phase)
    x = position + offset
    y = 260 + level * 250
    img = alpha_composite(img, overlay, dest = (x, y))
    return img

for frame in range(0, 1605):

    # Initialize frame image
    if source is None:
        img = Image.new('RGBA', (size['x'], size['y']), color = bgcolor)
    else:
        img = next(source).to_image().convert('RGBA')
    print('Processing frame', frame, end = '\r', flush = True)

    # First and second bunch of marching cats (frames 0-1604)
    if frame in range(0, 1605):
        if frame < 1200:
            for i in range(11):
              img = mitchiri_march(img, frame, bunch1[i], -188 - 246 * i);
        if frame > 1000:
            for i in range(6):
              img = mitchiri_march(img, frame, bunch2[i], -3910 - 246 * i);

    # Bass drum sequence ('B' and last four of second bunch) (1605-1681)
    #for frame in range(1605, 1681):

    # Last four of second bunch, 'B', and third bunch (1682-2499)
    #for frame in range(1682, 2500):

    # Lead cats and harp sequence (bunch 4) (2500-3041)
    #for frame in range(2500, 3042):

    # Bunch 4, 'H' cat, bunch 5, 'B' cat, bunch 6, and two 'S' cats (3042-4240)
    #for frame in range(3042, 4241):

    # Just a plain frame with nothing (4241-5399)
    #for frame in range(4241, 5400):

    # Pack frame to output stream
    frame = av.VideoFrame.from_image(img)
    for packet in stream.encode(frame):
        container.mux(packet)

#flush_cache()


for packet in stream.encode():
    container.mux(packet)

container.close()
print()

#animations = 'LDFGTXCRUABSIHdnfygwtjxceoubahi'
#from PIL import Image, ImageDraw, ImageFont, ImageFile
#for filename in list(animations):
#    for frame in range(8):
#        shift = frame * 8
#        canvas.rectangle([2 + shift, 2, 198 + shift, 198], fill = None, outline = 'black', width = 2)
#        canvas.text((10 + shift, 60), filename + str(frame), font = font, fill = 'black')
#        img.save(filename + str(frame) + '.png')
