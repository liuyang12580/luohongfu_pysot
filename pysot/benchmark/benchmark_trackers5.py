import os
import cv2

def benchmark():
    # trackers = ['SiamRPN', 'SiamFC', 'SiamDW', 'SiamRPN++', 'DaSiamRPN']
    # video_name = []
    # for i in range (len(path_list)):
    #     video_name.append(path_list[i].split('.')[0])
    file_path = '/home/dc/ly/benchmark/SiamRPN'
    path_list = os.listdir(file_path)
    # file_path = '/home/dc/volume1TB/ly/12.16/benchmark/checkpoint_e35/'
    # path_list = os.listdir(file_path)
    path_list.sort()

    # path_list1 = ['Mavic_Attr_nob_1.txt', 'Mavic_Attr_nob_2.txt', 'Mavic_BC_1.txt', 'Mavic_BC_2.txt', 'Mavic_BC_3.txt',
    #  'Mavic_BC_4.txt', 'Mavic_BC_5.txt', 'Mavic_BC_6.txt', 'Mavic_BC_7.txt', 'Mavic_BC_FM_1.txt', 'Mavic_BC_FM_10.txt',
    #  'Mavic_BC_FM_11.txt', 'Mavic_BC_FM_12.txt', 'Mavic_BC_FM_2.txt', 'Mavic_BC_FM_3.txt', 'Mavic_BC_FM_4.txt',
    #  'Mavic_BC_FM_5.txt', 'Mavic_BC_FM_6.txt', 'Mavic_BC_FM_7.txt', 'Mavic_BC_FM_8.txt', 'Mavic_BC_FM_9.txt',
    #  'Mavic_BC_FM_LR_1.txt', 'Mavic_BC_FM_MB_1.txt', 'Mavic_BC_FM_MB_2.txt', 'Mavic_BC_FM_MB_3.txt',
    #  'Mavic_BC_FM_MB_4.txt', 'Mavic_BC_FM_MB_OPR_1.txt', 'Mavic_BC_FM_MB_OV_1.txt', 'Mavic_BC_FM_MB_OV_2.txt',
    #  'Mavic_BC_FM_MB_SV_1.txt', 'Mavic_BC_FM_MB_SV_2.txt', 'Mavic_BC_FM_MB_SV_3.txt', 'Mavic_BC_FM_OPR_1.txt',
    #  'Mavic_BC_FM_OV_2.txt', 'Mavic_BC_FM_SV_1.txt', 'Mavic_BC_FM_SV_2.txt', 'Mavic_BC_FM_SV_3.txt',
    #  'Mavic_BC_FM_SV_4.txt', 'Mavic_BC_FM_SV_5.txt', 'Mavic_BC_FM_SV_6.txt', 'Mavic_BC_LR_1.txt', 'Mavic_BC_MB_1.txt',
    #  'Mavic_BC_MB_IPR_SV_1.txt', 'Mavic_BC_MB_OPR_1.txt', 'Mavic_BC_MB_OPR_2.txt', 'Mavic_BC_OV_part_1.txt',
    #  'Mavic_BC_SV_1.txt', 'Mavic_BC_SV_2.txt', 'Mavic_BC_SV_ROT_1.txt', 'Mavic_FM_1.txt', 'Mavic_FM_2.txt',
    #  'Mavic_FM_3.txt', 'Mavic_FM_4.txt', 'Mavic_FM_OPR_1.txt', 'Mavic_FM_OV_1.txt', 'Mavic_FM_OV_2.txt',
    #  'Mavic_FM_OV_part_1.txt', 'Mavic_IPR_1.txt', 'Mavic_MB__FM_OPR_1.txt', 'Mavic_OV_part_1.txt', 'Mavic_SV_1.txt',
    #  'Mavic_SV_IPR_1.txt']
    video_list = []
    # for i in trackers:
        # trackers_path = os.path.join('/home/dc/ly/benchmark/', '{}/{}/{}/{}_001.txt'.format(datasets, i, video_name, video_name))

    trackers_path = os.path.join('/home/dc/ly/benchmark/SiamRPN/', '{}'.format(path_list[i]))
    with open(trackers_path) as f:
        video_val = f.readlines()
        video_list.append(video_val)
# print(video_list)
    return video_list

def trackers_pred_bbox(benchmark_bbox, id):
    video_line = []
    for t in benchmark_bbox:
        t_bbox = t[id]
        t_bbox = t_bbox.strip('\n').split(',')
        t_bbox = [float(i) for i in t_bbox]
        video_line.append(t_bbox)
    return video_line

def plot_bbox(pre_bbox, image):
    # color_list = [(125, 255, 125), (0, 0, 255), (255, 0, 0), (255, 255, 0), (255, 0, 255), (255, 255, 255)]
    color_list = [(0, 0, 255),(255, 255, 255)]
    for i in pre_bbox:
        bb = list(map(int, i))
        cv2.rectangle(image, (bb[0], bb[1]), (bb[0] + bb[2], bb[1] + bb[3]), color_list[pre_bbox.index(i)], 3)
