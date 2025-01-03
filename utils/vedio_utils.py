import cv2

def read_vedio(vedio_path):
    cap = cv2.VideoCapture(vedio_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  

    frame_width = output_video_frames[0].shape[1]
    frame_height = output_video_frames[0].shape[0]

    out = cv2.VideoWriter(output_video_path, fourcc, 24, (frame_width, frame_height))
    
    for frame in output_video_frames:
        out.write(frame)
    out.release()