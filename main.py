import os
import numpy as np
import matplotlib.pyplot as plt


dir_path = 'D:\桌面\传输组\\algos_iperf\\algos_iperf'
alg_name = os.listdir(dir_path) # ['bbr', 'bic', 'cubic', 'htcp', 'reno', 'vegas', 'westwood']


def read_data(alg:str,txt:str):#提取txt文件中的流量数据,并返回一个列表
    data = []
    for line in open(dir_path + '\\' + alg + '\\' + txt, "r"):
        data.append(line)
    Bytes = []
    if len(data) > 7:
        for y in range(7, len(data) - 1):
            Bytes.append(float(data[y].split(" ")[6]))
        return Bytes
    return []



if __name__ == '__main__':

    for m in range(len(alg_name)):
        txt_name = os.listdir(dir_path + '\\' + alg_name[m])

        print(dir_path +'\\'+ alg_name[m])

        txt_name.sort(key=lambda x: int(x.split("_")[1][:-1]))
        for i in range(len(txt_name)):
            print(txt_name[i])

            Bytes = read_data(alg_name[m],txt_name[i])
            print(Bytes)

            time = np.arange(300)
            print('均值=',np.mean(np.float_(Bytes)),'方差=',np.var(np.float_(Bytes)))
            print(str(alg_name[m] + '_out1.txt'))
            f_out = open("out" + "\\" + alg_name[m]+'_out.txt','a',encoding='utf-8')
            string = '均值='+ str(np.mean(np.float_(Bytes))) +'  ' + '方差=' + str(np.var(np.float_(Bytes)))
            f_out.write(txt_name[i]+'  ')
            f_out.write(str(string)+'  ')
            f_out.write(str(Bytes))
            f_out.write('\n')



