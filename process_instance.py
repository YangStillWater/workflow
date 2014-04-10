__author__ = 'Peng'

from task_instance import Task_Instance


class ProcessInstance():
    '流程实例'

    class Permission():
        '动作许可'
        start = True
        stop = True
        send = True

    process_inst = None
    permission = Permission()
    operator = 'admin'
    task_instance_list = None

    def __init__(self, process_inst):
        self.process_inst = process_inst

    def start(self):
        node = self.process_inst[0]
        node.active()

    def suspend(self):
        pass

    def stop(self):
        pass

    def resume(self):
        pass

    def delete(self):
        pass

    def send(self):
        lenth = len(self.process_inst)
        for i in range(lenth):
            node = self.process_inst[i]
            if i < lenth - 1:
                node_next = self.process_inst[i + 1]
            else:
                node_next = Task_Instance()
            if node.is_active:
                node.inactive()
                node_next.active()
                break

