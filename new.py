import os
import pandas as pd

lst = [1,2,3,4]
df = pd.DataFrame(lst)
df.to_csv('output.csv')

versioned_table = "v1"

def checkpoint(
	addfile: str,
	ignfile: str,
	addconf: str,
	gitcommit: str,
	dvcpush: str
):
	return versioned_table


checkpoint(
	os.system("dvc add output.csv"),
	os.system("git add output.csv.dvc"),
	os.system("git add dvc.yaml"),
	os.system("git commit -m 'new version'{versioned_table}"),
	os.system("dvc push"),
)






