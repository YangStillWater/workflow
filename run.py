__author__ = 'Peng'

from process_instance import ProcessInstance
from task_instance import Task_Instance

node_start = Task_Instance('start')
node1 = Task_Instance(1)
node2 = Task_Instance(2)
node3 = Task_Instance(3)
node_end = Task_Instance('end')

process_inst = (node_start, node1, node2, node3, node_end)

p = ProcessInstance(process_inst)

p.start()

p.send()
p.send()
p.send()
