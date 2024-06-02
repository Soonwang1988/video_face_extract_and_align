import cv2
import os
import argparse


def extract_frames(video_path, output_folder):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Create a filename for each frame
        frame_filename = os.path.join(output_folder, f"{frame_count:05d}.png")

        # Save the frame as an image file
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")


def main():
    parser = argparse.ArgumentParser(description="Extract frames from a video file and save them to a directory.")
    parser.add_argument("video_file", help="Path to the video file")
    parser.add_argument("output_folder", help="Path to the folder where frames will be saved")

    args = parser.parse_args()

    extract_frames(args.video_file, args.output_folder)


if __name__ == "__main__":
    main()
