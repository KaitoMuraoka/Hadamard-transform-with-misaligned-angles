## ライブラリのインポート
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import time
import random
from qulacs import QuantumState
from qulacs.state import inner_product
from qulacs import QuantumCircuit
from qulacs.gate import to_matrix_gate
from qulacs import QuantumState
from qulacs.gate import Identity, X,Y,Z #パウリ演算子
from qulacs.gate import H
from qulacs.gate import RX,RY,RZ #パウリ演算子についての回転演算
from qulacs.gate import U1,U2,U3 #IBMQの基底ゲート

from fractions import Fraction

# # 係数の絶対値の分布をプロットする関数
def show_distribution(state, nqubits):
    plt.bar([i for i in range(pow(2, nqubits))], abs(state.get_vector()))
    plt.xlabel(f'$2^{nqubits}$個のデータ')
    plt.ylabel('各状態の確率振幅')
    plt.ylim(0, 1)
    plt.show()

# 解の確率振幅と試行回数kに関するグラフ
def line_graph(result, title):
    plt.title(title)
    plt.plot(result, "o-")
    plt.xlabel('試行回数k')
    plt.ylabel('解の確率振幅')
    plt.ylim(0, 1)
    plt.xticks(np.arange(0, len(result), step=1))
    plt.grid()
    plt.show()