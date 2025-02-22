import bpy
import os

def text_to_3d_animation(summary: str, output_path: str):
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Create text object
    bpy.ops.object.text_add()
    text_obj = bpy.context.object
    text_obj.data.body = summary
    
    # Animate
    text_obj.location.z = -10
    text_obj.keyframe_insert(data_path="location", frame=1)
    
    text_obj.location.z = 0
    text_obj.keyframe_insert(data_path="location", frame=60)
    
    # Render settings
    bpy.context.scene.render.filepath = os.path.abspath(output_path)
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.ops.render.render(animation=True)