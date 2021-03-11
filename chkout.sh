checkout=${1}
git reset --hard ${checkout}
dvc pull
dvc run -n new1  --force python3 src/catname.py
git add dvc.yaml
dvc add csvdata/name.csv
git add csvdata/name.csv.dvc
hdfs dfs -copyFromLocal -f csvdata/name.csv /user/hive/data/

