import os
import cv2
from pathlib import Path

# Define paths
input_dir = Path('input-videos/v1')
output_dir = Path('video-frames')

# Create output directory if it doesn't exist
output_dir.mkdir(exist_ok=True)

# Process each video in the input directory
for video_file in input_dir.glob('*.mp4'):
    # Create folder for this video's frames
    video_name = video_file.stem  # Get filename without extension
    frame_dir = output_dir / video_name
    frame_dir.mkdir(exist_ok=True)
    
    # Open video
    video = cv2.VideoCapture(str(video_file))
    
    # Read frames
    frame_count = 0
    while True:
        success, frame = video.read()
        if not success:
            break
            
        # Save frame as image
        frame_path = frame_dir / f'frame_{frame_count:04d}.jpg'
        cv2.imwrite(str(frame_path), frame)
        frame_count += 1
    
    # Release video
    video.release()
    print(f'Processed {video_name}: extracted {frame_count} frames')

print('All videos processed!') 