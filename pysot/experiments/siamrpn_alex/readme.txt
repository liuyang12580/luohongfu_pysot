####################################################################################################################
############## training CNN: cd /path/to/pysot/experiments/siamrpn_alex

source activate pysot

export PYTHONPATH=/home/dc/luohongfu/pysot:$PYTHONPATH

CUDA_VISIBLE_DEVICES=0
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

python -m torch.distributed.launch --nproc_per_node=1 --master_port=2333 ../../tools/train.py --cfg config.yaml


#####################################################################################################################
##############  test tracker: cd /path/to/pysot/experiments/siamrpn_alex

python -u ../../tools/test.py --snapshot ./snapshot/checkpoint_exx.pth --dataset OTBxxx --config config.yaml --vis


#####################################################################################################################
##############  eval tracker: cd /path/to/pysot/experiments/siamrpn_alex

python ../../tools/eval.py --tracker_path ./results --dataset OTBxxx --num 1 --tracker_prefix 'checkpoint_exx'


#####################################################################################################################
#############  hp_search: cd /path/to/pysot/experiments/siamrpn_alex

python -u ../../tools/hp_search.py --snapshot checkpoint_exx.pth --dataset OTBxxx --config config.yaml


######################################################################################################################
#############  demo: cd /path/to/pysot/experiments/siamrpn_alex

python ../../tools/demo.py --config experiments/siamrpn_alex/config.yaml --snapshot experiments/siamrpn_alex/snapshot/checkpoint_exx.pth --video demo/xx.mp4

#######################################################################################################################


