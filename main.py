import time
import random
import datetime
from dataclasses import dataclass
from queue import Queue


@dataclass
class Order:
    timestamp: datetime.datetime

    def __str__(self):
        return f'<order make at {self.timestamp}>'


class OrderController(object):

    def __init__(self, window=datetime.timedelta(minutes=5), limit=10):
        self.Q = list()  # use list as a queue
        self.M = window
        self.N = limit

    def allow(self, order):
        while 1:
            if len(self.Q) >= self.N:
                order_first = self.Q[0]
                if datetime.datetime.now() - order_first.timestamp > self.M:
                    self.Q.pop(0)
                else:  # full but all in M
                    return False
            else:  # not full
                # put into Q
                self.Q.append(order)
                return True


if __name__ == '__main__':
    controllor = OrderController()
    orders = []
    for i in range(15):
        time.sleep(random.uniform(0.01, 0.1))
        orders.append(Order(datetime.datetime.now()))
    print(orders)
    for order in orders:
        if controllor.allow(order):
            print('allow {}'.format(order))
        else:
            print('deny  {}'.format(order))
