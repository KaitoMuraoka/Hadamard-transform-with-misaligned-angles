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

## 自作ライブラリ
import operation

# ユニットテスト
import unittest

class TestOperation(unittest.TestCase):
    # y軸を中心とした回転にノイズがあるアダマールと、
    # ノイズのないアダマールゲートのテスト
    def test_y_Hadamard(self, nqubits = 3):
        target_state = QuantumState(nqubits)
        target_state.set_computational_basis(2 ** nqubits - 1)

        state1 = QuantumState(nqubits)
        state1.set_zero_state()
        revolution_Hadamard = operation.hadamard(nqubits)
        revolution_Hadamard.update_quantum_state(state1)
        hoge = np.linalg.norm(inner_product(state1, target_state))

        state2 = QuantumState(nqubits)
        state2.set_zero_state()
        noisy_Hadamard = operation.make_y_noisy_Hadamard(nqubits, 0)
        noisy_Hadamard.update_quantum_state(state2)
        fuga = np.linalg.norm(inner_product(state2, target_state))
        self.assertEqual(hoge, fuga)

    # z軸を中心とした回転にノイズがあるアダマールと、
    # ノイズのないアダマールゲートのテスト
    def test_z_Hadamard(self, nqubits = 3):
        target_state = QuantumState(nqubits)
        target_state.set_computational_basis(2 ** nqubits - 1)

        state1 = QuantumState(nqubits)
        state1.set_zero_state()
        revolution_Hadamard = operation.hadamard(nqubits)
        revolution_Hadamard.update_quantum_state(state1)
        hoge = np.linalg.norm(inner_product(state1, target_state))

        state2 = QuantumState(nqubits)
        state2.set_zero_state()
        noisy_Hadamard = operation.make_z_noisy_Hadamard(nqubits, 0)
        noisy_Hadamard.update_quantum_state(state2)
        fuga = np.linalg.norm(inner_product(state2, target_state))
        self.assertEqual(hoge, fuga)

    # yとzを中心とした回転にノイズがあるアダマールと、
    # ノイズのないアダマールゲートのテスト
    def test_yz_Hadamard(self, nqubits = 3):
        target_state = QuantumState(nqubits)
        target_state.set_computational_basis(2 ** nqubits - 1)

        state1 = QuantumState(nqubits)
        state1.set_zero_state()
        revolution_Hadamard = operation.hadamard(nqubits)
        revolution_Hadamard.update_quantum_state(state1)
        hoge = np.linalg.norm(inner_product(state1, target_state))

        state2 = QuantumState(nqubits)
        state2.set_zero_state()
        noisy_Hadamard = operation.make_yz_noisy_Hadamard(nqubits, 0)
        noisy_Hadamard.update_quantum_state(state2)
        fuga = np.linalg.norm(inner_product(state2, target_state))
        self.assertEqual(hoge, fuga)


