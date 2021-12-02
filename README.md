# Mitchiri Neko March generator

This script will generate (when it is finished) a modified version
of [Mitchiri Neko March](https://www.youtube.com/watch?v=lAIGb1lfpBw) video,
like [this one](https://www.youtube.com/watch?v=8VIllAilTnE)
with My Little Pony: Friendship is Magic characters.

Anything you need beyond this (except obvious things like fonts and drawing app)
is a massive amount of time to draw animation frames to let script animate it,
as original Mitchiri Neko March consists of totally 72 characters of 8 frames each.

# Workflow

1. Run `mitchiri_png_generate` to generate `images/` subdirectory and PNG files there.
2. Download `mitchiri.mp4` (video only, single track container) and possibly convert it to 1280x720@30FPS.
3. Run `mitchiri_create` to test if images fit into correct positions.
4. Edit everything in `images/` to your own animation frames (stubs are useful to place sprites correctly).
5. Delete `mitchiri.mp4` and run `mitchiri_create` to compile final file.

# Notice

Everything is WIP. Not sure I ever finish it someday.
