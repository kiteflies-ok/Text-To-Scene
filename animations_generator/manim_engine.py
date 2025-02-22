from manim import Scene, Text, Write
import subprocess
import os

def generate_manim_animation(scenes: list, output_dir: str = "media/animations") -> str:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "2d_animation.mp4")
    
    scene_code = generate_scene_code(scenes)
    with open("temp_scene.py", "w") as f:
        f.write(scene_code)
    
    subprocess.run([
        "manim", "-ql", 
        "--media_dir", output_dir,
        "temp_scene.py", "GeneratedScene"
    ])
    
    os.remove("temp_scene.py")
    return output_path

def generate_scene_code(scenes: list) -> str:
    scenes_str = "\n".join([f'        self.play(Write(Text("{scene}")))' 
                          for scene in scenes])
    return f"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
{scenes_str}
        self.wait(3)
"""