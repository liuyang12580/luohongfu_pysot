# Copyright (c) SenseTime. All Rights Reserved.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from yacs.config import CfgNode as CN

__C = CN()

cfg = __C

__C.META_ARC = "siamrpn_r50_l234_dwxcorr"

__C.CUDA = True

# ------------------------------------------------------------------------ #
# Training options
# ------------------------------------------------------------------------ #
__C.TRAIN = CN()

# Anchor Target
# Positive anchor threshold
__C.TRAIN.THR_HIGH = 0.6

# Negative anchor threshold
__C.TRAIN.THR_LOW = 0.3

# Number of negative
__C.TRAIN.NEG_NUM = 16

# Number of positive
__C.TRAIN.POS_NUM = 16

# Number of anchors per images
__C.TRAIN.TOTAL_NUM = 64


__C.TRAIN.EXEMPLAR_SIZE = 127

__C.TRAIN.SEARCH_SIZE = 255

__C.TRAIN.BASE_SIZE = 8

__C.TRAIN.OUTPUT_SIZE = 25

__C.TRAIN.RESUME = ''

__C.TRAIN.PRETRAINED = ''

__C.TRAIN.LOG_DIR = './logs'

__C.TRAIN.SNAPSHOT_DIR = './snapshot'

__C.TRAIN.EPOCH = 20

__C.TRAIN.START_EPOCH = 0

__C.TRAIN.BATCH_SIZE = 32

__C.TRAIN.NUM_WORKERS = 1

__C.TRAIN.MOMENTUM = 0.9

__C.TRAIN.WEIGHT_DECAY = 0.0001

__C.TRAIN.CLS_WEIGHT = 1.0

__C.TRAIN.LOC_WEIGHT = 1.2

__C.TRAIN.MASK_WEIGHT = 1

__C.TRAIN.PRINT_FREQ = 20

__C.TRAIN.LOG_GRADS = False

__C.TRAIN.GRAD_CLIP = 10.0

__C.TRAIN.BASE_LR = 0.005

__C.TRAIN.LR = CN()

__C.TRAIN.LR.TYPE = 'log'

__C.TRAIN.LR.KWARGS = CN(new_allowed=True)

__C.TRAIN.LR_WARMUP = CN()

__C.TRAIN.LR_WARMUP.WARMUP = True

__C.TRAIN.LR_WARMUP.TYPE = 'step'

__C.TRAIN.LR_WARMUP.EPOCH = 5

__C.TRAIN.LR_WARMUP.KWARGS = CN(new_allowed=True)

# ------------------------------------------------------------------------ #
# Dataset options
# ------------------------------------------------------------------------ #
__C.DATASET = CN(new_allowed=True)

# Augmentation
# for template
__C.DATASET.TEMPLATE = CN()

# Random shift see [SiamPRN++](https://arxiv.org/pdf/1812.11703)
# for detail discussion
__C.DATASET.TEMPLATE.SHIFT = 4

__C.DATASET.TEMPLATE.SCALE = 0.05

__C.DATASET.TEMPLATE.BLUR = 0.0

__C.DATASET.TEMPLATE.FLIP = 0.0

__C.DATASET.TEMPLATE.COLOR = 1.0

__C.DATASET.SEARCH = CN()

__C.DATASET.SEARCH.SHIFT = 64

__C.DATASET.SEARCH.SCALE = 0.18

__C.DATASET.SEARCH.BLUR = 0.0

__C.DATASET.SEARCH.FLIP = 0.0

__C.DATASET.SEARCH.COLOR = 1.0

# Sample Negative pair see [DaSiamRPN](https://arxiv.org/pdf/1808.06048)
# for detail discussion
__C.DATASET.NEG = 0.2

# improve tracking performance for otb100
__C.DATASET.GRAY = 0.0


__C.DATASET.NAMES = ('Inspire', 'Matrice', 'Mavic', 'Phantom', 'Quadrotor', 'Quadrotor450', 'Quadrotor450LD')


__C.DATASET.Inspire = CN()
__C.DATASET.Inspire.ROOT = 'training_dataset/inspire/crop511'
__C.DATASET.Inspire.ANNO = 'training_dataset/inspire/train.json'
__C.DATASET.Inspire.FRAME_RANGE = 100  #100
__C.DATASET.Inspire.NUM_USE = 19 # all: 19 repeat until reach NUM_USE

__C.DATASET.Matrice = CN()
__C.DATASET.Matrice.ROOT = 'training_dataset/matrice/crop511'
__C.DATASET.Matrice.ANNO = 'training_dataset/matrice/train.json'
__C.DATASET.Matrice.FRAME_RANGE = 20
__C.DATASET.Matrice.NUM_USE = 103  # all: 103 repeat until reach NUM_USE

__C.DATASET.Mavic = CN()
__C.DATASET.Mavic.ROOT = 'training_dataset/mavic/crop511'
__C.DATASET.Mavic.ANNO = 'training_dataset/mavic/train.json'
__C.DATASET.Mavic.FRAME_RANGE = 100  #100  #100
__C.DATASET.Mavic.NUM_USE = 17  #17   #17/8/4  # all: 17  repeat until reach NUM_USE

__C.DATASET.Phantom = CN()
__C.DATASET.Phantom.ROOT = 'training_dataset/phantom/crop511'
__C.DATASET.Phantom.ANNO = 'training_dataset/phantom/train.json'
__C.DATASET.Phantom.FRAME_RANGE = 100  #100
__C.DATASET.Phantom.NUM_USE = 23  # all: 23 repeat until reach NUM_USE

__C.DATASET.Quadrotor = CN()
__C.DATASET.Quadrotor.ROOT = 'training_dataset/quadrotor/crop511'
__C.DATASET.Quadrotor.ANNO = 'training_dataset/quadrotor/train.json'
__C.DATASET.Quadrotor.FRAME_RANGE = 100
__C.DATASET.Quadrotor.NUM_USE = 25  # all: 25 repeat until reach NUM_USE

__C.DATASET.Quadrotor450 = CN()
__C.DATASET.Quadrotor450.ROOT = 'training_dataset/quadrotor450/crop511'
__C.DATASET.Quadrotor450.ANNO = 'training_dataset/quadrotor450/train.json'
__C.DATASET.Quadrotor450.FRAME_RANGE = 100
__C.DATASET.Quadrotor450.NUM_USE = 24  # all: 24 repeat until reach NUM_USE

__C.DATASET.Quadrotor450LD = CN()
__C.DATASET.Quadrotor450LD.ROOT = 'training_dataset/quadrotor450LD/crop511'
__C.DATASET.Quadrotor450LD.ANNO = 'training_dataset/quadrotor450LD/train.json'
__C.DATASET.Quadrotor450LD.FRAME_RANGE = 100
__C.DATASET.Quadrotor450LD.NUM_USE = 11  # all: 11 repeat until reach NUM_USE


__C.DATASET.VIDEOS_PER_EPOCH = 300000
# ------------------------------------------------------------------------ #
# Backbone options
# ------------------------------------------------------------------------ #
__C.BACKBONE = CN()

# Backbone type, current only support resnet18,34,50;alexnet;mobilenet
__C.BACKBONE.TYPE = 'res50'

__C.BACKBONE.KWARGS = CN(new_allowed=True)

# Pretrained backbone weights
__C.BACKBONE.PRETRAINED = ''

# Train layers
__C.BACKBONE.TRAIN_LAYERS = ['layer2', 'layer3', 'layer4']

# Layer LR
__C.BACKBONE.LAYERS_LR = 0.1

# Switch to train layer
__C.BACKBONE.TRAIN_EPOCH = 10

# ------------------------------------------------------------------------ #
# Adjust layer options
# ------------------------------------------------------------------------ #
__C.ADJUST = CN()

# Adjust layer
__C.ADJUST.ADJUST = True

__C.ADJUST.KWARGS = CN(new_allowed=True)

# Adjust layer type
__C.ADJUST.TYPE = "AdjustAllLayer"

# ------------------------------------------------------------------------ #
# RPN options
# ------------------------------------------------------------------------ #
__C.RPN = CN()

# RPN type
__C.RPN.TYPE = 'MultiRPN'

__C.RPN.KWARGS = CN(new_allowed=True)

__C.RPN.CLS = CN()

__C.RPN.CLS.TRAIN_LAYERS = ['conv_kernel', 'conv_search', 'head']

__C.RPN.LOC = CN()

__C.RPN.LOC.TRAIN_LAYERS = ['conv_kernel', 'conv_search', 'head']

__C.RPN.LAYERS_LR = 0.1

# ------------------------------------------------------------------------ #
# mask options
# ------------------------------------------------------------------------ #
__C.MASK = CN()

# Whether to use mask generate segmentation
__C.MASK.MASK = False

# Mask type
__C.MASK.TYPE = "MaskCorr"

__C.MASK.KWARGS = CN(new_allowed=True)

__C.REFINE = CN()

# Mask refine
__C.REFINE.REFINE = False

# Refine type
__C.REFINE.TYPE = "Refine"

# ------------------------------------------------------------------------ #
# Anchor options
# ------------------------------------------------------------------------ #
__C.ANCHOR = CN()

# Anchor stride
__C.ANCHOR.STRIDE = 8

# Anchor ratios
__C.ANCHOR.RATIOS = [0.33, 0.5, 1, 2, 3]

# Anchor scales
__C.ANCHOR.SCALES = [8]

# Anchor number
__C.ANCHOR.ANCHOR_NUM = len(__C.ANCHOR.RATIOS) * len(__C.ANCHOR.SCALES)


# ------------------------------------------------------------------------ #
# Tracker options
# ------------------------------------------------------------------------ #
__C.TRACK = CN()

__C.TRACK.TYPE = 'SiamRPNTracker'

# Scale penalty
__C.TRACK.PENALTY_K = 0.04

# Window influence
__C.TRACK.WINDOW_INFLUENCE = 0.44

# Interpolation learning rate
__C.TRACK.LR = 0.4

# Exemplar size
__C.TRACK.EXEMPLAR_SIZE = 127

# Instance size
__C.TRACK.INSTANCE_SIZE = 255

# Base size
__C.TRACK.BASE_SIZE = 8

# Context amount
__C.TRACK.CONTEXT_AMOUNT = 0.5

# Long term lost search size
__C.TRACK.LOST_INSTANCE_SIZE = 831

# Long term confidence low
__C.TRACK.CONFIDENCE_LOW = 0.85

# Long term confidence high
__C.TRACK.CONFIDENCE_HIGH = 0.998

# Mask threshold
__C.TRACK.MASK_THERSHOLD = 0.30

# Mask output size
__C.TRACK.MASK_OUTPUT_SIZE = 127
