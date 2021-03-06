from p2pool.bitcoin import networks

PARENT = networks.nets['usde']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 50 # blocks
IDENTIFIER = '1f28fcfe0d56a1a1'.decode('hex')
PREFIX = 'f163e0ac2fe68af2'.decode('hex')
P2P_PORT = 29948
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8860
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net p2pool-eu.gotgeeks.com:8448 p2pool-us.gotgeeks.com:8448 rav3n.dtdns.net:8448 p2pool.gotgeeks.com:8448 p2pool.dndns.net:8448 solidpool.org:8448'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
