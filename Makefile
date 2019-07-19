
output/raw-waveform.png: data/BBH_events_v3.json
	mkdir -p $(dir $@)
	python3 plot-raw.py $@ $^

# 准备数据，如果已经准备好请忽略。
data:
	mkdir $@
	cd $@
	wget http://hep.tsinghua.edu.cn/~orv/pd/data-LIGO.tar.gz
	tar xf data-LIGO.tar.gz
	rm data-LIGO.tar.gz
