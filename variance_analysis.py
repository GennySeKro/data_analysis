import re

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import kstest, ks_2samp
from scipy.stats import spearmanr

import main

import seaborn as sns

from scipy import stats

def read(μ_path: str):  # 读取给定路径下的文件内容
    μ_data = []#txt文件名
    name_data = []#均值
    var_data = []#方差
    data = []#流量数据
    for line in open(μ_path, "r",encoding='utf-8'):
        name_data.append(line.split("  ")[0])
        μ_data.append(line.split("  ")[1])
        var_data.append(line.split("  ")[2])

        #读取的流量数据是字符串，需要转化为数字
        data.append(re.findall(r'[\'](.*?)[\']', line.split("  ")[3]))


    return name_data,μ_data,var_data,data


def add_path(alg_name: list):  # 合成out文件夹下的txt文件名称
    path = []
    for i in range(len(alg_name)):
        path.append(main.alg_name[i] + "_" + "out" + ".txt")
    return path


path = add_path(main.alg_name)

for i in range(len(path)):
    print(".out" + "\\" + path[i])

    #对应的txt文件名、均值、方差、流量数据
    name_data,μ_data,var_data,data = read("out" + "\\" + path[i])


    print(spearmanr(np.float_(data[0]), np.float_(data[1])))

    # for j in range(len(name_data)):
    #     r, p = spearmanr(np.float_(data[0]), np.float_(data[j]))
    #     print(name_data[j])
    #     if p > 0.05:
    #         print('no')
    #     else:
    #         print('yes')


    # print(stats.kruskal(np.float_(data[0]), np.float_(data[1]),np.float_(data[2]), np.float_(data[3])))




    # sns.heatmap(np.float_(data[:2]))
    # plt.show()

    break

