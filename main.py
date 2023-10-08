
# 复现 https://blog.51cto.com/luoqingchao/6140701 中的 柏松模型

import math
import time


def Year2hour(year:int):

    return year * 24 * 365


def Possion(Lambda, n, t):
    """
    计算柏松概率
    """
    return math.pow(Lambda * t, n) * math.exp(-Lambda * t) / math.factorial(n)

    
def Model(N, n, t, AFR):
    """
    利用柏松分布计算 N个磁盘, 在 年度故障率为AFR 下, t小时, 损坏n个磁盘 的概率.
    :param N: 服务器硬盘数, int
           n: 坏盘数量, int
           t: 小时数, int
           AFR: 年度故障率, float
    """

    # 计算lambda
    lbda = AFR / (24 * 365) * N

    # 计算 P(N(t) = n)
    P = Possion(lbda, n, t)

    return P


def Pro1():
    """
    度量时间 t 增加影响P1概率
    """
    print("N\t\tt\tAFR\t\tP1(any)\tAFR * N")

    N, AFR = 36, 0.005
    T = [1, 12, 24, 168, 720, 2160, 4320, 8760, 26280, 43800, 61320]

    for t in T:
        P1_any = 1 - Model(N, 0, t, AFR)
        print("{0}\t{1:5.0f}\t{2}\t{3:.4f}\t{4}".format(N, t, AFR, P1_any, AFR * N))


def Pro2():
    """
    磁盘 N 增加影响P1概率
    """
    print("\tN\tt\t\tAFR\t\tP1(any)\tAFR * N")

    t, AFR, = Year2hour(1), 0.005
    N = [6, 12, 24, 36, 108, 180, 360, 720, 1080, 3000, 180000]

    for n in N:
        P1_any = 1 - Model(n, 0, t, AFR)
        print("{0:6.0f}\t{1}\t{2}\t{3:.4f}\t{4}".format(n, t, AFR, P1_any, AFR * n))


def Pro3():
    """
    AFR 增加影响P1故障率
    """
    print("N\t  t\t\tAFR\t\tP1(any)\tAFR * N")

    N, t = 36, Year2hour(1)
    AFR = [0.004, 0.005, 0.006, 0.008, 0.01, 0.02, 0.04, 0.08]

    for afr in AFR:
        P1_any = 1 - Model(N, 0, t, afr)
        print("{0}\t{1}\t{2}\t{3:.4f}\t{4:.3f}".format(N, t, afr, P1_any, afr * N))


if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    Pro3() 
    