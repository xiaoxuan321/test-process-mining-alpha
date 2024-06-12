import os
import pm4py
import time

if __name__ == "__main__":
    # 构建XES文件的相对路径
    log_BPIC13cp = pm4py.read_xes('BPIC13cp.xes')
    BPI_Challenge_2012 = pm4py.read_xes('BPI_Challenge_2012.xes')

    start = time.perf_counter()
    # Alpha Miner
    net, im, fm = pm4py.discover_petri_net_alpha(log_BPIC13cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
    net, im, fm = pm4py.discover_petri_net_alpha(BPI_Challenge_2012, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
    end = time.perf_counter()
    print("Alpha Miner耗时: " + str(end - start) + "秒")