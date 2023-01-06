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
import math

## 自作ライブラリ
import made_graph as graph
import grover_algorithm as algorithm

# ユニットテスト
import unittest

class TestAlgorithm(unittest.TestCase):
    nqubit = 3
    times = 4
    result_theory, k_theory, p_kth = algorithm.grover(nqubit, times)
    revolution_result, revolution_maxk = algorithm.revolution_grover(nqubit, times)
    noisy_y_result, noisy_y_maxk, noisy_y_pk = algorithm.noisy_y_grover(nqubit, times, 0)
    noisy_z_result, noisy_z_maxk, noisy_z_pk = algorithm.noisy_z_grover(nqubit, times, 0)
    def test_theory_grover(self, p_kth = p_kth, k_theory = k_theory):
        ans = 0.9722718241315015
        k_ans = 2
        self.assertEqual(p_kth, ans)
        self.assertEqual(k_theory, k_ans)

    # revolution groverとtheory groverのテスト
    def test_revolution_theory(self):
        revolution_result = self.revolution_result
        theory_result = self.result_theory
        self.assertTrue(np.allclose(revolution_result, theory_result))

        revolution_k = self.revolution_maxk
        theory_k = self.k_theory
        self.assertTrue(np.allclose(revolution_k, theory_k))

    # noisy groverとtheory groverのテスト
    def test_noisy_theory(self):
        noisy_y_result = self.noisy_y_result
        theory_result = self.result_theory
        print(f'result theory: {noisy_y_result}')
        print(f'result noizy y: {theory_result}')
        self.assertTrue(np.allclose(noisy_y_result, theory_result))

        noisy_y_k = self.noisy_y_maxk
        theory_k = self.k_theory
        self.assertTrue(np.allclose(noisy_y_k, theory_k))

        noisy_pk = self.noisy_y_pk
        theory_pk = self.p_kth
        self.assertTrue(np.allclose(noisy_pk, theory_pk))


    # revolution_groverとnoisy_groverのテスト
    def test_y_grover(self, nqubits = 3, times = 4):
        revolution_result = self.revolution_result
        revolution_maxk = self.revolution_maxk
        noisy_result = self.noisy_y_result
        noisy_maxk = self.noisy_y_maxk

        self.assertEqual(revolution_result, noisy_result)
        self.assertEqual(revolution_maxk, noisy_maxk)

# 理想のグローバーとz回転のグローバのテスト
    def test_z_grover(self, nqubits = 3, times = 4):
        result_theory = self.result_theory
        k_theory = self.k_theory
        p_kth = self.p_kth

        result_noisy_z = self.noisy_z_result
        maxk_noisy_z = self.noisy_z_maxk
        pk_noisy_z = self.noisy_z_pk

        result = np.allclose(result_theory, result_noisy_z)
        print(f'result theory: {result_theory}')
        print(f'result noisy z: {result_noisy_z}')
        maxk = np.allclose(k_theory, maxk_noisy_z)
        pk = np.allclose(p_kth, pk_noisy_z)

        self.assertTrue(result)
        self.assertTrue(maxk)
        self.assertTrue(pk)

