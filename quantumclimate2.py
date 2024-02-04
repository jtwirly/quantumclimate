from qiskit_ibm_runtime import QiskitRuntimeService
 
service = QiskitRuntimeService(channel="ibm_quantum", token="e062aab97300178da0436050a37d4c5c29605b267944a42789682dba6f4e4b6cfec94acf0659ccb130697dff52418b935e5316a62d416968275b8ba30d3266a9")
 
from qiskit import QuantumCircuit, Aer, execute
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.visualization import plot_histogram

#Create a Quantum Circuit: Define a quantum circuit with one qubit and one classical bit for measurement:
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate to create superposition
qc.measure(0, 0)  # Measure the qubit

# Visualize the Circuit (Optional): To visualize your circuit, you can use:

qc.draw(output='mpl')

#Execute the Circuit: Run the circuit on a quantum simulator:
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)