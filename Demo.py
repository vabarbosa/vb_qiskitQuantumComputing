from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute
from qiskit.visualization import plot_histogram


circ=QuantumCircuit(2,2)
circ.h(0)
circ.x(1)
circ.z(1)
circ.measure((0,1),(0,1))

circ.draw()




from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute
circ.draw()
backend = Aer.get_backend("qasm_simulator")
job = execute(circ,backend,shots=1024)
result=job.result()
count=result.get_counts(circ)
plot_histogram(count)