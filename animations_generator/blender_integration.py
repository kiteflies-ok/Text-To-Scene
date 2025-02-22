import bpy
import subprocess
import os

def generate_blender_animation(scenes: list, output_dir: str = "media/animations") -> str:
    output_path = os.path.join(output_dir, "3d_animation.mp4")
    script_path = os.path.join("animation_generator", "blender_scripts", "text_to_3d.py")
    
    subprocess.run([
        "blender", "--background", "--python", script_path,
        "--", "--text", ";".join(scenes), "--output", output_path
    ])
    
    return output_path