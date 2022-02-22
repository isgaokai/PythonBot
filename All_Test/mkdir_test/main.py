# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import os

path = '/All_Test/mkdir_test'
path = os.path.join(path,'test_out','test_in')
os.makedirs(path)