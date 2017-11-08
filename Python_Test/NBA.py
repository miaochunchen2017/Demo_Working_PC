# coding=utf-8
import pandas as pd
import scipy
import sklearn
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score


# 当每支队伍没有elo等级分时，赋予其基础elo等级分
base_elo = 1600
team_elos = {}
team_stats = {}
x = []
y = []
folder = 'data'         # 存放数据的目录



