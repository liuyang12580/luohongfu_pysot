### testing data set : OTBQuadrotor25 OTBInspire31 OTBPhantom17 OTBMavic62 OTBMavic62down

python -u ../../tools/test.py --snapshot ./VMPIQFD-VMPIQFD-VMPIQ45.pth --dataset OTBMavic62 --config ./config.yaml --vis
python ../../tools/eval.py --tracker_path ./results/ --dataset OTBMavic62 --num 1 --tracker_prefix '*'
    
python ../../tools/eval.py --tracker_path ./resultsMP/ --dataset OTBQuadrotor25 --num 1 --tracker_prefix 'checkpoint_e9'

python ../../tools/eval.py --tracker_path ./results/ --dataset OTBPhantom17 --num 1 --tracker_prefix 'checkpoint_e9'

python ../../tools/eval.py --tracker_path ./results/ --dataset OTBQuadrotor25 --num 1 --tracker_prefix 'checkpoint_e9'

python ../../tools/eval.py --tracker_path ./results/ --dataset OTBInspire31 --num 1 --tracker_prefix 'checkpoint_e9'

python ../../tools/eval.py --tracker_path ./results/ --dataset OTBMavic62down --num 1 --tracker_prefix 'checkpoint_e9'

python ../../tools/eval.py --tracker_path ./results/ --dataset VOT2016 --num 1 --tracker_prefix 'checkpoint_e9'
