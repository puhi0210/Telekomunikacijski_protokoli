
#   Program je namenjen izdelavi testne log datoteke

import logging

logging.basicConfig(filename='Projekt\pozivnikLog.log', level=logging.DEBUG,  format='%(asctime)s : %(message)s')

logging.warning('RECO BR: VAJA OB 18.00 URI V GASILSKEM DOMU')