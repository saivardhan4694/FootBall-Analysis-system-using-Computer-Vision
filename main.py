# from ultralytics import YOLO

# model = YOLO("models/best.pt")
# results = model.predict(r"D:\repositories\foot_ball_analysis\Data\08fd33_4.mp4", save = True)
# print(results[0])
# print("================================")
# for box in results[0].boxes:
#     print(box)

from utils import read_vedio, save_video
from pathlib import Path
from trackers.tracker import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_distance_estimator import SpeedAndDistance_Estimator

def main():
    # Read video
    video_path = Path(r"D:\repositories\foot_ball_analysis\Data\test (1).mp4")
    video_frames = read_vedio(video_path)
    # Save video
    #save_vedio(video_frames, Path(r"output_videos/output_video.avi"))

    tracker = Tracker(model_path= Path(r"models/best.pt"))
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub= True,
                                       stub_path="stubs/track_stubs2.pkl")
    
    # get object postions
    tracker.add_position_to_tracks(tracks)
    # camaera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frames = camera_movement_estimator.get_camera_movement(video_frames, read_from_stub= True, 
                                                                               stub_path= "stubs/camaera_movement2.pkl")
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frames)


    # View Transformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    # Interpolate ball path
    tracks["ball"] = tracker.interpolate_ball_path(tracks["ball"])
    
    # speed and distance estimator
    speed_distance_estimator = SpeedAndDistance_Estimator()
    speed_distance_estimator.add_speed_and_distance_to_tracks(tracks)


    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0],
                                    tracks["players"][0])
    
    tracks, video_frames = team_assigner.assign_teams_to_players(tracks, video_frames)

    # Assign ball aquisiton
    player_ball_assigner = PlayerBallAssigner()
    
    tracks, team_ball_control = player_ball_assigner.assign_player_to_ball(tracks)

    # Draw Ouptut
    output_vedio_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control, team_assigner.team_colors)

    # Draw Camera Movement
    output_vedio_frames = camera_movement_estimator.draw_camera_movement(output_vedio_frames, camera_movement_per_frames)

    # Draw Speed and Distance
    speed_distance_estimator.draw_speed_and_distance(output_vedio_frames, tracks)

    save_video(output_vedio_frames, Path(r"D:\repositories\foot_ball_analysis\output_videos\output_video2.mp4"))

if __name__ == "__main__":
    main()