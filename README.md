# wordImage
makes a word or letter into a 16x16 PNG image. Throws all images into a images folder.
Should be run from the command line

`<blender executable> -b fontRender.blend -P render_letters.py -- --fonts <fonts...> --chars <strings...>`

### example
on windows:

`blender.exe -b fontRender.blend -P render_letters.py -- --fonts fonts/impact.ttf fonts/georgia.ttf --chars A B C`

Gives you characters A, B, and C in fonts impact and georgia (and Bfont which comes default with blender)
