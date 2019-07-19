

# 准备数据
data:
	mkdir $@
	cd $@
	wget http://hep.tsinghua.edu.cn/~orv/pd/data-LIGO.tar.gz
	tar xf data-LIGO.tar.gz
	rm data-LIGO.tar.gz
