from collections import namedtuple
from queue import PriorityQueue
import random

event = namedtuple("event", "time proc action")
DEPARTURE_INTERVAL = 4
MINI_TRIPS = 2
SEARCH_DURATION = 3
TRIP_DURATION = 5


def main():
    taxi_number = 3
    event_dict = {i: taxi_process(i, (i + 1) * MINI_TRIPS, i * DEPARTURE_INTERVAL) for i in range(taxi_number)}
    sim = Simulator(event_dict)
    sim.run(end_time=100)


# 根据action的行为返回持续的时间
def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['离开车库', '送下乘客']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == '接到乘客':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == '回家':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1 / interval)) + 1


# 仿真器
class Simulator:
    def __init__(self, event_dict):
        self.proc_dict = dict(event_dict)
        self.event_queue = PriorityQueue()

    def run(self, end_time):
        sim_time = 0
        for key in self.proc_dict.values():
            self.event_queue.put(next(key))
        while sim_time < end_time:
            if self.event_queue.empty():
                print('finished')
                break
            current_event = self.event_queue.get()
            sim_time, proc, action = current_event
            print('编号为 {} 的出租车 {} {}'.format(proc, sim_time, action))
            time = sim_time + compute_duration(action)
            next_proc = self.proc_dict[proc]
            try:
                next_event = next_proc.send(time)
            except StopIteration:
                del self.proc_dict[proc]
            else:
                self.event_queue.put(next_event)


# 出租车运行进程 add start_time 每执行一个事件，就让步出去，将主线程交给下一个出租车
def taxi_process(ident, trips, start_time=0):
    time = yield event(time=start_time, proc=ident, action='离开车库')

    for i in range(trips):
        time = yield event(time, ident, '接到乘客')
        time = yield event(time, ident, '送下乘客')
    yield event(time, ident, '回家')


if __name__ == '__main__':
    main()
