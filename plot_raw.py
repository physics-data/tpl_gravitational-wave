import json

def load(index, evt_name="GW150914"):
    '''

    从 .json 目录中读取引力波事件的信息，从里面记载的文件名中
    进一步读取拉伸 (strain) 数据。

    - index: .json 目录的文件名
    - evt_name: 想要读取的引力波事例名
    - 返回：H 地信号，L 地信号，时间，事例信息
    '''
    events = json.load(open(index, "r"))
    event = events[evt_name]

    import readligo as rl

    ## FIXME!! data 路径写死了，应当可变
    fn_H1 = "data/" + event['fn_H1']
    strain_H1, time, chan_dict_H1 = rl.loaddata(fn_H1)
    fn_L1 = "data/" + event['fn_L1']
    strain_L1, time, chan_dict_L1 = rl.loaddata(fn_L1)

    event['tevent'] = event['tevent'] - time[0]
    time = time - time[0]

    return strain_H1, strain_L1, time, event

if __name__=='__main__':
    import sys
    
    strain_H1, strain_L1, time, event = load(sys.argv[2], "GW150914")
    import matplotlib as mpl
    mpl.use("Agg")

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,8))
    plt.plot(time, strain_H1, label="H1")
    plt.plot(time, strain_L1, label="L1")
    plt.vlines((16,), ymin=-2e-18, ymax=1e-18)
    plt.title("Strains of 2 detectors")
    plt.xlabel('time since Sep 14 9:50:29 GMT 2015 [s]');
    plt.ylabel('strain')
    plt.grid('on')
    plt.legend()
    plt.savefig(sys.argv[1])
