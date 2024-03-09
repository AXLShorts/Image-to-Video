import cv2
import numpy as np

def create_video(image_path, output_video_path, duration_sec=120, fps=60):
    # Load the image
    img = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = img.shape

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Calculate number of frames
    total_frames = duration_sec * fps

    # Shift image downwards for each frame
    for i in range(total_frames):
        shifted_img = np.roll(img, -i, axis=0)
        out.write(shifted_img)

    # Release video writer
    out.release()

    print("Video created successfully!")

# Example usage
create_video("test.jpg", "output_video.mp4")
