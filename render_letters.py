import bpy
override = {'snap_selected_to_cursor': list(bpy.ops.view3d)}
bpy.ops.object.delete(override)

def set_text_font(fontpath):
    bpy.ops.font.open(filepath=fontpath)

def scale_text(string_replace):
    # print(dir(bpy.context))
    bpy.context.scene.objects['Text'].data.body = string_replace
    textObj = bpy.data.objects['Text']
    textObj.scale.xyz = 1
    bpy.context.scene.update()
    textObj.scale.xyz = 7.25 / max(textObj.dimensions.x, textObj.dimensions.y)
    bpy.context.scene.update()
    textObj.location.y = 0 - (textObj.dimensions.y / 2)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    # bpy.context.area.type = "VIEW_3D"
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    # bpy.context.area.type = "TEXT_EDITOR"

def render_scene(filepath, anti_aliasing=True):
    render.use_antialiasing = anti_aliasing
    bpy.context.scene.render.filepath = "//" + filepath
    bpy.ops.render.render( write_still=True )

scale_text("A")
render_scene("A")
