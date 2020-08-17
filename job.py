import time
import logging
from kubernetes import config, client

import socket
from urllib3 import connection
# workaround for azure load balancer issue
connection.HTTPConnection.default_socket_options += [(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
                                            (socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60),
                                            (socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60),
                                            (socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3)]

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level = logging.DEBUG)

config.load_incluster_config()
v1 = client.CoreV1Api()

logging.info('Calling 1st time')
start_time = time.time()
v1.list_namespaced_pod('default')
logging.info("First Execution took --- %s seconds ---" % (time.time() - start_time))

logging.info('Sleeping 10 minutes')
time.sleep(600)

logging.info('Calling 2nd time')
start_time = time.time()
# this call will timeout after 15 minutes may be?
v1.list_namespaced_pod('default')
logging.info("Second Execution took --- %s seconds ---" % (time.time() - start_time))