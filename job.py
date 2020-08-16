import time
import logging
from kubernetes import config, client

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