import glob
import os
import sys
import argparse


current_file_path = os.path.abspath(__file__)
parent_folder_path = os.path.dirname(current_file_path)
sys.path.append(f'{parent_folder_path}/landmark_extract_face_align')


from frame_extract import extract_frames
from landmark_extract_face_align.main import landmark_extract_and_align

def get_all_video_files(parent_data):
    return glob.glob(f"{parent_data}/**/*.mp4", recursive=True)

def extract_directory_from_filepath(filepath):
    return os.path.dirname(filepath)

def remove_original_data(directory):
    original_data_path = f"{directory}/original_data"
    if os.path.exists(original_data_path):
        for root, dirs, files in os.walk(original_data_path):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(original_data_path)
    print(f"Removed original data from {original_data_path}")

def main(parent_data):
    all_files = get_all_video_files(parent_data)

    for file in all_files:
        directory = extract_directory_from_filepath(file)

        # Frame extraction
        extract_frames(file, f"{directory}/original_frames")

        # Face extraction
        landmark_extract_and_align(f"{directory}/original_frames", f"{directory}/aligned_frames")

        # Remove original data
        remove_original_data(directory)

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser(description="Extract frames and align faces from video files.")
    parser.add_argument('parent_data', type=str, help="Path to the parent data directory containing the video files")
    
    args = parser.parse_args()
    
    main(args.parent_data)

