import numpy
import pexpect
import sys
from optparse import OptionParser


class NetworkLatencyBenchmark(object):
    def __init__(self, ip, timeout=1200):
        object.__init__(self)

        self.ip = ip
        self.interval = 0.5

        ping_command = 'ping -i ' + str(self.interval) + ' ' + self.ip
        self.ping = pexpect.spawn(ping_command)

        self.ping.timeout = timeout
        self.ping.readline()  # init

        self.wifi_latency = []
        self.wifi_timeout = 0

    def run_test(self, n_sample=100):
        for n in xrange(n_sample):
            p = self.ping.readline()

            try:
                ping_time = float(p[p.find('time=') + 5:p.find(' ms')])
                self.wifi_latency.append(ping_time)

            except:
                self.wifi_timeout = self.wifi_timeout + 1
                print 'timeout'

        self.wifi_timeout = self.wifi_timeout / float(n_sample)
        self.wifi_latency = numpy.array(self.wifi_latency)

    def get_results(self):
        print 'mean latency:', numpy.mean(self.wifi_latency), 'ms'
        print 'std latency:', numpy.std(self.wifi_latency), 'ms'
        print '99% latency:', numpy.percentile(self.wifi_latency, 50), 'ms'
        print '95% latency:', numpy.percentile(self.wifi_latency, 50), 'ms'
        print 'timeout:', self.wifi_timeout * 100, '%'


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "usage: python network_latency_test.py <ip> <n_sample> <timeout>"
        sys.exit(1)
        
    parser = OptionParser(usage="usage: %prog -h arg1 -s arg2 -t arg3 ")
    parser.add_option('-h', help='host used to verify the latency', nargs=1, dest='host', type='string', default=False, action='store')
    parser.add_option('-s', help='Number of sample [default=5]', nargs=1, dest='sample', type='int', default=5, action='store')
    parser.add_option('-t', help='Timeout in milleseconds for network checking [default={}]'.format(100), nargs=1, dest='timeout', type='string', default=100, action='store')
    (options, args) = parser.parse_args()
    
    ip = options.host
    n_sample = int(options.sample) 
    timeout = int(options.timeout) 
    

    network = NetworkLatencyBenchmark(ip,timeout)

    network.run_test(n_sample)
    network.get_results()
