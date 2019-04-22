# -*- coding: utf-8 -*-
"""
log_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""

import logging

log_fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
log_file = 'blue_ox.log'
print('-'*30)
print('Setting logging.basicConfig(level=logging.DEBUG), \
      format=log_fmt, \
      filename=log_file):')
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG, format=log_fmt)
logging.basicConfig(level=logging.DEBUG, format=log_fmt, filename=log_file)
print('-'*30)

#%%
print('logging.debug():')
logging.debug("Looks like rain")
logging.debug("It's raining again")
print('-'*30)

print('logging.info():')
logging.info("And hail")
logging.info("With hail the size of hailstones")
print('-'*30)

print('logging.warning():')
logging.warning("Did I hear thunder?")
print('-'*30)

print('logging.error():')
logging.error("Was that lightning?")
print('-'*30)

print('logging.critical():')
logging.critical("Stop fencing and get inside!")
print('-'*30)
#%%

#%%
print('-'*30)
the_logger = 'bunyan'
print('logging.getLogger('+the_logger+'):')
logger = logging.getLogger(the_logger)
print('-'*30)

logging.info("Looks like rain")
logger.info('Timber!')
print('logging.info():','logger.info()')
print('-'*30)

logging.debug("And hail")
logger.debug("Where's my axe?")
print('logging.debug():','logger.debug()')
print('-'*30)

logging.warning("Did I hear thunder?")
logger.warning("I need my axe")
print('logging.warning():','logger.warning()')
print('-'*30)

#%%


