### testing data set : OTBQuadrotor25 OTBInspire31 OTBPhantom17 OTBMavic62 OTBMavic62down

for k in {1..50}
do
    python -u ../../tools/testhalfhalf.py --snapshot ./snapshothalfhalf/checkpoint_e$k.pth --dataset OTBMavic62 --config ./configcopyhalfhalf.yaml
done

for k in {1..50}
do
    python -u ../../tools/test3.py --snapshot  ./snapshot3/checkpoint_e$k.pth --dataset OTBPhantom17  --config  ./configcopy.yaml
done

for k in {1..50}
do
    python -u ../../tools/test3.py --snapshot  ./snapshot3/checkpoint_e$k.pth --dataset OTBInspire31 --config ./configcopy.yaml
done


for k in {1..50}
do
    python -u ../../tools/test3.py --snapshot ./snapshot3/checkpoint_e$k.pth --dataset OTBMavic62 --config ./configcopy.yaml
done


for k in {1..50}
do
    python -u ../../tools/test3.py --snapshot ./snapshot3/checkpoint_e$k.pth --dataset OTBMavic62down --config ./configcopy.yaml
done

for k in {1..50}
do
    python -u ../../tools/test3.py --snapshot ./snapshot3/checkpoint_e$k.pth --dataset OTBQuadrotor25 --config ./configcopy.yaml
done

for k in {1..50}
do
    python -u ../../tools/testMP.py --snapshot  ./snapshotMP/checkpoint_e$k.pth --dataset OTBMavic62  --config  ./configcopy.yaml
done
