#!/usr/bin/env python
# -*- coding:utf-8 -*-

import utils
from pathlib import Path

def run(string, entities):
	"""Leon lists skills and modules"""
    
	packages = ''
	d = Path('./packages')
	for child in d.iterdir():
		if child.is_dir(): 
			packages = packages + child.name + '\n'

	return utils.output('inter', 'done', packages)