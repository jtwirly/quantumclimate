# expand your Quantum Random Number Generator (QRNG) to generate sequences of random bits
# Loop for Multiple Series - if you prefer to collect multiple series of random bits (each series from a separate execution of the circuit)

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

# Loop for Multiple Series - if you prefer to collect multiple series of random bits (each series from a separate execution of the circuit)
# Example: Collect 10 series of random bits
num_series = 10
all_counts = []

for _ in range(num_series):
    job = execute(qc, simulator, shots=1)  # Single shot for each series
    result = job.result()
    counts = result.get_counts(qc)
    all_counts.append(counts)

# Print all collected series
print(all_counts)
