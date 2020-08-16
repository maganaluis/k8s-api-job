import time
import logging
from kubernetes import config, client

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level = logging.DEBUG)

config.load_incluster_config()
v1 = client.CoreV1Api()

logging.info('Calling 1st time')
v1.list_namespaced_pod('default')
logging.info('Sleeping 5 minutes')
time.sleep(300)
logging.info('Calling 2nd time')

# this call will timeout after 15 minutes
v1.list_namespaced_pod('default')
logging.info('OK')