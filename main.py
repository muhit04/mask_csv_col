import os
import csv
from itertools import islice
import hashlib

class MaskCsvCol:
	def __init__(self, source_dir, dest_dir, skip_rows=0):
		self.src = source_dir
		self.dst = dest_dir
		self.skip_rows = skip_rows

	def get_file_names(self):
		return os.listdir(self.src)

	def process_files(self):
		file_list = self.get_file_names()
		for f in file_list:
			src_file_path = self.src + "/" + f
			dst_file_path = self.dst + "/" + f
			with open(src_file_path, 'r') as f, open(dst_file_path, "w") as out:
				rows = csv.reader(islice(f, self.skip_rows, None))
				lines = list(rows)
				for idx, l in enumerate(lines):
					if idx == 0:
						continue
					new_username = hashlib.md5(l[0].encode('utf-8')).hexdigest()
					l[0] = new_username 
				wr = csv.writer(out)
				wr.writerows(lines)
 

m = MaskCsvCol('sample_data', 'output', skip_rows=7)
m.process_files()