# 爱的引力波 （gravitational-wave）

## 问题背景

两周过去了，芃芃终于上完了万恶的英语小学期！暑假是个出游的好时间，芃芃来到了著名的 LIGO 天文台。在这里，他了解到了著名的 GW150914 事件，这是人类历史上第一次观测到引力波的存在，又一次有力地印证了广义相对论。GW150914 来自于一次遥远的双黑洞合并事件，它们互相旋转、吸引，最后终于融为一体，释放出了巨大的能量。芃芃不禁回忆起了自己和女朋友相恋的过程：他们不也像这两个黑洞一样慢慢地走进了对方的生活，最后成为彼此不可取代的一部分，并从爱情中获得了巨大的能量吗！

想到这里，芃芃陷入了沉思……

## Git 协作

添加远程的 Git 仓库。

`git remote add upstream git@github.com:physics-data/tpl_gravitational-wave.git`

`upstream` 也可以是你取的任何名字。

`git fetch upstream`

从 `upstream` 取得最新的 `commit`。

`git log upstream/master`

查看 `upstream/master` 上的 `commit`。

`git merge upstream/master`

将 `upstream/master` 合并到本地。

## 问题描述

参照 LIGO 公开数据的 Jupyter Notebook，建造 LIGO 的数据流水线。
