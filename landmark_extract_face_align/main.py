import multiprocessing
import sys
from core.leras import nn
from pathlib import Path
from mainscripts import Extractor


def landmark_extract_and_align(input_path, output_path):
    # Fix for linux
    multiprocessing.set_start_method("spawn")
    nn.initialize_main_env()

    Extractor.main(detector="s3fd",
                   input_path=Path(input_path),
                   output_path=Path(output_path),
                   output_debug=False,
                   manual_fix=None,
                   manual_output_debug_fix=False,
                   manual_window_size=1368,
                   face_type="whole_face",  #"full_face",
                   max_faces_from_image=1,
                   image_size=512,
                   jpeg_quality=100,
                   cpu_only=False,
                   force_gpu_idxs=[0])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input_path output_path")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        landmark_extract_and_align(input_path, output_path)








