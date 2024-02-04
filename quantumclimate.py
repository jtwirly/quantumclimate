from qiskit_ibm_runtime import QiskitRuntimeService
 
service = QiskitRuntimeService(channel="ibm_quantum", token="e062aab97300178da0436050a37d4c5c29605b267944a42789682dba6f4e4b6cfec94acf0659ccb130697dff52418b935e5316a62d416968275b8ba30d3266a9")
 

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
 
 # Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
 # You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(example_circuit)
print(f"job id: {job.job_id()}")
result = job.result()
print(result)