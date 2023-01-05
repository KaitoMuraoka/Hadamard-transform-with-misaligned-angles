## ライブラリのインポート
from qulacs import QuantumCircuit
from qulacs.gate import H

# アダマール演算子
def Hadamard(nqubits):
    Hadamard = QuantumCircuit(nqubits)
    for i in range(nqubits):
        Hadamard.add_gate(H(i))
    return Hadamard