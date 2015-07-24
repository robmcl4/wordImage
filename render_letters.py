import bpy
import sys
argv = sys.argv

if ("--fonts" in argv) and ("--chars" in argv):
    fonts = argv[argv.index("--fonts")+1:argv.index("--chars")]
if "--chars" in argv:
    chars = argv[argv.index("--chars")+1:]

def add_font(fontpath):
    bpy.ops.font.open(filepath=fontpath)

def set_font(font):
    bpy.data.curves["Text"].font = font

def scale_text(string_replace):
    bpy.context.scene.objects['Text'].data.body = string_replace
    textObj = bpy.data.objects['Text']
    textObj.scale.xyz = 1
    bpy.context.scene.update()
    textObj.scale.xyz = 7.25 / max(textObj.dimensions.x, textObj.dimensions.y)
    bpy.context.scene.update()
    textObj.location.y = 0 - (textObj.dimensions.y / 2)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.context.object.location = [0,0,0]

def render_scene(filepath, anti_aliasing=True):
    bpy.context.scene.render.use_antialiasing = anti_aliasing
    bpy.context.scene.render.filepath = "//images/" + filepath
    bpy.ops.render.render(write_still=True)


# main code
for fontIndex in range(len(fonts)):
    add_font(fonts[fontIndex])

for font in bpy.data.fonts.values():
    set_font(font)
    for charIndex in range(len(chars)):
        scale_text(chars[charIndex])
        render_scene(font.name + "_" + chars[charIndex])
