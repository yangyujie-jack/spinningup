import datetime
from torch.utils.tensorboard import SummaryWriter
import os


class Logger:
    def __init__(self, port=6006):
        cur_path = os.path.abspath(__file__)
        project_path = cur_path[:cur_path.find('spinningup')] + 'spinningup/'
        log_path = project_path + 'log/'
        os.popen(f'tensorboard --logdir={log_path} --port {port}')
        t = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        self.writer = SummaryWriter(log_path + t)
        self.add_num = {}

    def add_scalar(self, **kwargs):
        tag = kwargs.pop('tag')
        for k, v in kwargs.items():
            if k not in self.add_num.keys():
                self.add_num[k] = 0
            else:
                self.add_num[k] += 1
            self.writer.add_scalar(tag + '/' + k, v, self.add_num[k])
