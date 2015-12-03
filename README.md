# network-benchmark
**This piece of code is originanly forked from : https://github.com/matthieu-lapeyre/network-benchmark**

[![Build Status](https://travis-ci.org/Flukas88/network-benchmark.svg?branch=master)](https://travis-ci.org/Flukas88/network-benchmark)

You can quickly evaluate the latency of your network and obtain mean, std, percentile, timeout data. 
Usage is `python network_test.py -i <ip> -s <n_sample> -t <timeout>` for example you can run:
```console
python network_test.py -i 192.168.0.1 -s 50 -t 1300
```
and the output will be something like this:

``` console
mean latency: 19.0138426854 ms
std latency: 91.3184052069 ms
99% latency: 7.4905 ms
95% latency: 7.4905 ms
timeout: 0.2 %
```
