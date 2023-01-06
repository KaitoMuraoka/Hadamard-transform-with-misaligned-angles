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
from qulacs.gate import Identity, X, Y, Z  # パウリ演算子
from qulacs.gate import H
from qulacs.gate import RX, RY, RZ  # パウリ演算子についての回転演算
from qulacs.gate import U1, U2, U3  # IBMQの基底ゲート

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


# ここからノイズ本題
noises_title = ['0', '(π/4)', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4', '2π']
noises_title_int = [0, (np.pi / 4), np.pi / 2, 3 * np.pi / 4, np.pi, 5 * np.pi / 4, 3 * np.pi / 2, 7 * np.pi / 4,
                    2 * np.pi]


# K - K_throryのグラフ化
def different_of_k_graph(x, y, yticks_start, yticks_end):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(noises_title_int, noises_title)
    ax.set_yticks(np.arange(yticks_start, yticks_end, 1))
    ax.grid(axis='both')
    ax.set_xlabel("与えたノイズδ", size=14, weight="light")
    ax.set_ylabel('(k) - (k_theory)', size=14, weight="light")
    ax.plot(x, y, "-o")


# P(k)のグラフ化
def P_k_graph(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(noises_title_int, noises_title)
    ax.set_ylim(0, 1)
    ax.grid(axis='both')
    ax.set_xlabel("与えたノイズδ", size=14, weight="light")
    ax.set_ylabel("解の確率振幅", size=14, weight="light")
    ax.plot(x, y, "-o")


# P(K_throry)のグラフ化
def P_k_throry_graph(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(noises_title_int, noises_title)
    ax.set_ylim(0, 1)
    ax.grid(axis='both')
    ax.set_xlabel("与えたノイズδ", size=14, weight="light")
    ax.set_ylabel("理想値k_{theory}時の解の確率振幅", size=14, weight="light")
    ax.plot(x, y, "-o")
