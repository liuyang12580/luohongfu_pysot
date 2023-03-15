# import os
# import cv2
# def benchmark(datasets, video_name):
#     trackers = ['SiamRPN', 'SiamFC', 'SiamDW', 'SiamRPN++', 'DaSiamRPN']
#     video_list = []
#     for i in trackers:
#         trackers_path = os.path.join('/home/db/work/lhp/pysot_attn/benchmark', '{}/{}/{}/{}_001.txt'.format(datasets, i, video_name, video_name))
#         with open(trackers_path) as f:
#             video_val = f.readlines()
#             video_list.append(video_val)
#     return video_list
#
# def trackers_pred_bbox(benchmark_bbox, id):
#     video_line = []
#     for t in benchmark_bbox:
#         t_bbox = t[id]
#         t_bbox = t_bbox.strip('\n').split(',')
#         t_bbox = [float(i) for i in t_bbox]
#         video_line.append(t_bbox)
#     return video_line
#
# def plot_bbox(pre_bbox, image):
#     color_list = [(125, 255, 125), (0, 0, 255), (255, 0, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
#     for i in pre_bbox:
#         bb = list(map(int, i))
#         cv2.rectangle(image, (bb[0], bb[1]), (bb[0] + bb[2], bb[1] + bb[3]), color_list[pre_bbox.index(i)], 3)
import os
import cv2

def benchmark():
    trackers = ['base_OTBmavic62']
    path_list = [
     'Mavic_FM_OV_part_1.txt', 'Mavic_IPR_1.txt', 'Mavic_MB__FM_OPR_1.txt', 'Mavic_SV_1.txt']
    # video_names = ['Basketball', 'Biker', 'Bird1', 'Bird2', 'BlurBody', 'BlurCar1', 'BlurCar2', 'BlurCar3',
    #                'BlurCar4', 'BlurFace', 'BlurOwl', 'Board', 'Bolt', 'Bolt2', 'Box', 'Boy', 'Car1', 'Car2',
    #                'Car24', 'Car4', 'CarDark', 'CarScale', 'ClifBar', 'Coke', 'Couple', 'Coupon', 'Crossing',
    #                'Crowds', 'Dancer', 'Dancer2', 'David', 'David2', 'David3', 'Deer', 'Diving', 'Dog', 'Dog1',
    #                'Doll', 'DragonBaby', 'Dudek', 'FaceOcc1', 'FaceOcc2', 'Fish', 'FleetFace', 'Football',
    #                'Football1', 'Freeman1', 'Freeman3', 'Freeman4', 'Girl', 'Girl2', 'Gym', 'Human2', 'Human3',
    #                'Human4-2', 'Human5', 'Human6', 'Human7', 'Human8', 'Human9', 'Ironman',
    #                'Jogging-1', 'Jogging-2', 'Jump', 'Jumping', 'KiteSurf', 'Lemming', 'Liquor', 'Man', 'Matrix',
    #                'Mhyang', 'MotorRolling', 'MountainBike', 'Panda', 'RedTeam',
    #                'Rubik', 'Shaking', 'Singer1', 'Singer2', 'Skater', 'Skater2', 'Skating1',
    #                'Skating2-1', 'Skating2-2', 'Skiing', 'Soccer', 'Subway', 'Surfer', 'Suv', 'Sylvester',
    #                'Tiger1', 'Tiger2', 'Toy', 'Trans', 'Trellis', 'Twinnings', 'Vase', 'Walking', 'Walking2', 'Woman']
    # video_names = []
    # file_path = '/home/dc/luohongfu/pysot/testing_dataset/VOT2019'
    # video_names = os.listdir(file_path)
    # video_names.sort()
    # print(video_names)
    # video_names = [ 'agility', 'ants1', 'ball2', 'ball3', 'basketball', 'birds1', 'bolt1', 'book', 'butterfly',
    #                 'car1', 'conduction1', 'crabs1', 'dinosaur', 'dribble', 'drone1', 'drone_across',
    #                 'drone_flip', 'fernando', 'fish1', 'fish2', 'flamingo1', 'frisbee', 'girl', 'glove',
    #                 'godfather', 'graduate', 'gymnastics1', 'gymnastics2', 'gymnastics3', 'hand', 'hand2',
    #                 'handball1', 'handball2', 'helicopter', 'iceskater1', 'iceskater2', 'lamb', 'leaves',
    #                  'marathon', 'matrix', 'monkey', 'motocross1', 'nature', 'pedestrian1', 'polo',
    #                 'rabbit', 'rabbit2', 'road', 'rowing', 'shaking', 'singer2', 'singer3', 'soccer1',
    #                 'soccer2', 'soldier', 'surfing', 'tiger', 'wheel', 'wiper', 'zebrafish1']
    video_list = []
    # for video_name in video_names:
    trackers_path = os.path.join('/home/dc/ly/benchmark/base_OTBMavic62/Mavic_SV_1.txt')
        # trackers_path = os.path.join('/home/dc/ly/benchmark/base_VOT2019/', '{}/{}_001.txt'.format( video_name, video_name))
    with open(trackers_path) as f:
        video_val = f.readlines()
        video_list.append(video_val)
    return video_list
        # for count in path_list:
        #     trackers_path = os.path.join('/home/dc/ly/benchmark/SiamRPN/', '{}'.format(count))
        #     with open(trackers_path) as f:
        #         video_val = f.readlines()
        #         video_list.append(video_val)
        # return video_list[i]

def trackers_pred_bbox(benchmark_bbox, id):
    video_line = []
    for t in benchmark_bbox:
        t_bbox = t[id]
        t_bbox = t_bbox.strip('\n').split(',')
        t_bbox = [float(i) for i in t_bbox]
        video_line.append(t_bbox)
    return video_line

def plot_bbox(pre_bbox, image):
    color_list = [(0 , 0 , 255)]
    for i in pre_bbox:
        bb = list(map(int, i))
        cv2.rectangle(image, (bb[0], bb[1]), (bb[0] + bb[2], bb[1] + bb[3]), color_list[pre_bbox.index(i)], 3)
