import os
import pandas as pd

models = ['CT250MX500SSD1', 'DELLBOSS VD', 'MTFDDAV240TCB', 'ZA250CM10003',
		  'ZA500CM10003', 'ZA2000CM10002', 'ZA250CM10002', 'ZA500CM10002',
		  'ZA500GM10001', 'ZA250NM1002', 'SSD', 'WD Blue SA510 2.5WDS250G2B0A']

dir_path = '/Users/haifengni/Downloads/data_Q1_2023'
des_dir_path = dir_path + '_SSD'
os.system('rm -rf ' + des_dir_path)
os.system('mkdir ' + des_dir_path)

files = os.listdir(dir_path)
for fl in files:
	if fl == '.DS_Store':  # .DS_Store 是 MAC 系统自带的隐藏文件
		continue

	file = dir_path + '/' + fl
	resource_df = pd.read_csv(file)

	ls = []
	for i in range(len(resource_df)):
		md = resource_df.at[i, 'model']
		for t in models:
			if t in md:
				ls.append(i)
				break
	
	resource_df = resource_df.drop(list(set([i for i in range(len(resource_df))]) - set(ls)))
	resource_df.to_csv(des_dir_path + '/' + fl)
