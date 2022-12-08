#Importación de librerías
from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute
from qiskit.visualization import plot_histogram


# 01 CREAMOS NUESTRO PRIMER CIRCUITO
#Creamos un circuito cuántico de 4 Qbits y 3 bits
circ1=QuantumCircuit(4,3)
#En el último Qbit aplicamos una puerta X
circ1.x(3)
circ1.h((0,1,2,3))
circ1.draw(output='mpl')



# 02 CREAMOS NUESTRO SEGUNDO CIRCUITO
#Programamos la función, esta es la función que queremos saber si es constante o balanceada
#El comando barrier pone barreras imaginarias para que sea más entendible
circ2=QuantumCircuit(4,3)
circ2.barrier(range(4))
circ2.cx(0,3)
circ2.x(0)
circ2.cx(0,3)
circ2.cx(1,3)
circ2.x(1)
circ2.cx(1,3)
circ2.cx(2,3)
circ2.x(2)
circ2.cx(2,3)
circ2.barrier(range(4))
circ2.draw(output='mpl')

# 03 CREAMOS NUESTRO TERCER CIRCUITO
#Creamos un circuito de 4 qbits y tres bits
#Le aplicamos una puerta h a los tres primeros
circ3=QuantumCircuit(4,3)
circ3.h((0,1,2))
circ3.measure((0,1,2),(0,1,2))
circ3.draw(output='mpl')

# 04 UNIMOS TODOS LOS CIRCUITOS QUE CREAMOS PREVIAMENTE
#Una de las bondades de la librería Qiskit es que podemos sumar circuitos de una manera muy sencilla
circ=circ1+circ2+circ3
circ.draw(output='mpl')

#05 Una vez que tenemos el diseño, vamos a realizar la simulación
#Aquí se evalúa la función una única vez, por eso shots vale 1

backend=Aer.get_backend('qasm_simulator')
job=execute(circ,backend,shots=1)
result=job.result()
counts=result.get_counts(circ)
plot_histogram(counts)