check_if_util
=============

Nagios plugion to check network interface %utilization.

Takes _n_ readings over _n_ seconds and averages %utilization.

Usage Example
-------------

check_if_util.py -i eth1 -w 80 -c 95 -n 5

_takes 5 readings over 5 seconds on eth0_
