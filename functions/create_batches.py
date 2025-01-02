import shutil
import os
import json

# Configuration variables
BATCH_SUFFIX = "_batch_1"  # Change this to whatever you want, e.g., "_marius" or "_test_v2"

def copy_and_modify_file():
    # Define source and destination paths
    source_file = "example.txt"
    base_folder = "batches"
    # Create subfolder name by removing the leading underscore if it exists
    subfolder_name = BATCH_SUFFIX.lstrip('_')
    destination_folder = os.path.join(base_folder, subfolder_name)
    
    # List of video files to process
    video_files = [
        "Clip_1.mp4", 
        "Clip_2.mp4", 
        "Clip_4.mp4", 
        "Clip_5.mp4",
        "Clip_6.mp4",
        "Clip_8.mp4",
        "Clip_11.mp4", 
        "Clip_12.mp4", 
        "Clip_13.mp4", 
        "Clip_14.mp4",
        "Clip_15.mp4", 
        "Clip_16.mp4", 
        "Clip_17.mp4", 
        "Clip_18.mp4", 
        "Clip_19.mp4",
        "Clip_20.mp4", 
        "Clip_23.mp4", 
        "Clip_24.mp4", 
        "Clip_25.mp4",
    ]
    
    # Create directories if they don't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    try:
        # Check if source file exists
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Error: {source_file} not found")
        
        # Read the source file content
        with open(source_file, 'r') as f:
            config = json.load(f)
            
        # Create a copy for each video file
        for video_file in video_files:
            # Get clip number from filename
            clip_num = video_file.replace('Clip_', '').replace('.mp4', '')
            
            # Create a copy of the config for this iteration
            current_config = config.copy()
            
            # Update the batch_name using the configurable suffix
            current_config['batch_name'] = f"Clip_{clip_num}{BATCH_SUFFIX}"
            
            # Update init_images and cn_1_vid_path, replacing Clip_XXX with the correct clip number
            current_config['init_images'] = current_config['init_images'].replace('Clip_XXX', f'Clip_{clip_num}')
            current_config['cn_1_vid_path'] = current_config['cn_1_vid_path'].replace('Clip_XXX', f'Clip_{clip_num}')
            
            # Create destination filename with batch suffix
            dest_filename = f"Clip_{clip_num}{BATCH_SUFFIX}.txt"
            destination_file = os.path.join(destination_folder, dest_filename)
            
            # Write the modified config to the new file
            with open(destination_file, 'w') as f:
                json.dump(current_config, f, indent=4)
                
            print(f"Successfully created {dest_filename} in folder {subfolder_name}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    copy_and_modify_file()
