import os
import shutil
from pathlib import Path

def copy_videos():
    # Source and destination directories
    source_dir = r"E:\stable-diffusion\output\stable-diffusion-webui-qn\generated\default"
    dest_dir = r"G:\My Drive\marius-jopen\work\clients\art-camp\work\quantum-noise\output\selected-videos-2"

    # Ensure destination directory exists
    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    # Video file extensions to look for
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')

    # Get list of existing files in destination
    existing_files = {os.path.splitext(f)[0].split('_')[0] for f in os.listdir(dest_dir)}

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(source_dir):
        parent_folder = os.path.basename(root)
        
        # Skip if we already have files from this folder
        if parent_folder in existing_files:
            print(f"Skipping folder {parent_folder} - already processed")
            continue

        for file in files:
            # Check if the file is a video
            if file.lower().endswith(video_extensions):
                # Get full paths
                source_file = os.path.join(root, file)
                
                # Create new filename using parent folder name and original extension
                file_extension = os.path.splitext(file)[1]
                new_filename = f"{parent_folder}{file_extension}"
                
                # If a file with this name already exists, add a number
                counter = 1
                dest_file = os.path.join(dest_dir, new_filename)
                while os.path.exists(dest_file):
                    new_filename = f"{parent_folder}_{counter}{file_extension}"
                    dest_file = os.path.join(dest_dir, new_filename)
                    counter += 1
                
                # Copy the file
                print(f"Copying {source_file} to {dest_file}")
                shutil.copy2(source_file, dest_file)

if __name__ == "__main__":
    copy_videos()
    print("Video copying completed!")
