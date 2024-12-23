import sys 
sys.path.append('../')
from utils.bbox_utils import get_centre_of_bbox, measure_distance
import numpy as np

class PlayerBallAssigner():
    def __init__(self):
        self.max_player_ball_distance = 70
    
    def get_assinged_player(self,players,ball_bbox):
        ball_position = get_centre_of_bbox(ball_bbox)

        miniumum_distance = 99999
        assigned_player=-1

        for player_id, player in players.items():
            player_bbox = player['bbox']

            distance_left = measure_distance((player_bbox[0],player_bbox[-1]),ball_position)
            distance_right = measure_distance((player_bbox[2],player_bbox[-1]),ball_position)
            distance = min(distance_left,distance_right)

            if distance < self.max_player_ball_distance:
                if distance < miniumum_distance:
                    miniumum_distance = distance
                    assigned_player = player_id

        return assigned_player
    
    def assign_player_to_ball(self, tracks):
        team_ball_control = []
        for frame_num, player_track in enumerate(tracks["players"]):
            ball_box = tracks["ball"][frame_num][1]["bbox"]
            assigned_player = self.get_assinged_player(player_track, ball_box)

            if assigned_player != -1:
                tracks["players"][frame_num][assigned_player]["has_ball"] = True
                team_ball_control.append(tracks["players"][frame_num][assigned_player]["team"])
            else:
                team_ball_control.append(team_ball_control[-1])
        
        team_ball_control = np.array(team_ball_control)
        
        return tracks, team_ball_control