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


# アダマール演算子
def hadamard(nqubits):
    Hadamard = QuantumCircuit(nqubits)
    for i in range(nqubits):
        Hadamard.add_gate(H(i))
    return Hadamard


# オラクルU_wの作成
def make_U_w(nqubits):
    U_w = QuantumCircuit(nqubits)
    CnZ = to_matrix_gate(Z(nqubits - 1))
    # i-th qubitが全て1の場合だけゲートを作用
    for i in range(nqubits - 1):
        control_index = i
        control_with_value = 1
        CnZ.add_control_qubit(control_index, control_with_value)
    U_w.add_gate(CnZ)
    return U_w


# 反転U_sを作成
def make_U_s(nqubits):
    U_s = QuantumCircuit(nqubits)
    for i in range(nqubits):
        U_s.add_gate(H(i))

    # 2|0><0| - I の実装
    U_s.add_gate(to_matrix_gate(RZ(nqubits - 1, 2 * np.pi)))  # まず、位相(-1)を全ての状態に付与する。ゲート行列はarrary([[-1,0],[0,-1]])
    U_s.add_gate(X(nqubits - 1))
    # 全てのi-th qubitが0の場合だけZゲートを作用させる
    CnZ = to_matrix_gate(Z(nqubits - 1))
    for i in range(nqubits - 1):
        control_index = i
        control_with_value = 0
        CnZ.add_control_qubit(control_index, control_with_value)
    U_s.add_gate(CnZ)
    U_s.add_gate(X(nqubits - 1))

    for i in range(nqubits):
        U_s.add_gate(H(i))

    return U_s


# 任意の回転ゲートを利用してアダマールゲートを作成する
def make_revolution_Hadamard(nqubits):
    U_3 = QuantumCircuit(nqubits)
    THETA = np.pi / 2
    PHI = 0
    LAMBDA = np.pi
    # 全てのqubitにゲートを作用
    for i in range(nqubits):
        control_index = i
        U_3.add_gate(U3(control_index, THETA, PHI, LAMBDA))
    return U_3


def make_y_noisy_Hadamard(nqubits, delta):
    U_3 = QuantumCircuit(nqubits)
    THETA = np.pi / 2
    PHI = 0
    LAMBDA = np.pi
    # 全てのqubitにゲートを作用
    for i in range(nqubits):
        control_index = i
        U_3.add_gate(U3(control_index, THETA + delta, PHI, LAMBDA))
    return U_3

def make_z_noisy_Hadamard(nqubits, delta):
    U_3 = QuantumCircuit(nqubits)
    THETA = np.pi / 2
    PHI = 0
    LAMBDA = np.pi
    # 全てのqubitにゲートを作用
    for i in range(nqubits):
        control_index = i
        U_3.add_gate(U3(control_index, THETA, PHI, LAMBDA + delta))
    return U_3