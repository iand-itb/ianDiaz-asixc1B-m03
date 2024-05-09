"""
Ian Díaz
09/05/2024
ASIXc1 UF3 A1
Descripció: Examen Pp1
"""
import os
import logging
import time

logFile = os.path.join(os.path.join('.', 'log'), 'paraules.log')
logFormat = '%(asctime)s - %(levelname)s - %(message)s'
logLevel = logging.DEBUG
logMode = 'at'
color_code = 0
if not os.path.exists(os.path.join('.', 'log')):
    os.mkdir(os.path.join('.', 'log'))
logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)

start = time.time()

def logger(type, message):
    match type:
        case 'error': logging.error(message)
        case 'info': logging.info(message)
        case 'warning': logging.warning(message)
        case 'debug': logging.debug(message)
        case 'critical': logging.critical(message)

def timeElapsed():
    end = time.time()
    lapse = end-start
    return lapse
