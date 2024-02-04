# expand your Quantum Random Number Generator (QRNG) to generate sequences of random bits

from qiskit_ibm_runtime import QiskitRuntimeService
 
service = QiskitRuntimeService(channel="ibm_quantum", token="<IBM_QUANTUM_TOKEN>")
 
from qiskit import QuantumCircuit, Aer, execute
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.visualization import plot_histogram

# Define the number of qubits and bits
num_qubits = 4
qc = QuantumCircuit(num_qubits, num_qubits)

# Apply Hadamard gates to each qubit to create superposition states
for qubit in range(num_qubits):
    qc.h(qubit)

# Measure each qubit and store the result in the corresponding classical bit
qc.measure(range(num_qubits), range(num_qubits))

# Visualize the circuit (optional)
qc.draw(output='mpl')

#Execute the Circuit: Run the circuit on a quantum simulator:
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit with a higher number of shots
num_shots = 1024  # For example, 1024 executions of the circuit
job = execute(qc, simulator, shots=num_shots)
result = job.result()

# Get the counts of each bit sequence
counts = result.get_counts(qc)
print(counts)
