from dydx3.constants import API_HOST_SEPOLIA, API_HOST_MAINNET
from decouple import config

# !!! SELECT MODE !!!
MODE =  "DEVELOPMENT"

# Close all open positions and orders
ABORT_ALL_POSITION = True

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place Trades
PLACE_TRADES = True

# Place Trades
MANAGE_EXITS = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE  = 15 #ori 24
ZSCORE_THRESH = 1.75 #ori 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 500

# Thresholds - CLosing
CLOSE_AT_ZSCORE_CROSS = True

ETHEREUM_ADDRESS = "0xC0223736cCC86B3F7Ebe447014B497E952B756AD"

#KEYS - Production
# Must be on Mainnet
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

#KEYS - Development
# Must be on Testnet
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_SEPOLIA

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/DupZtQHZVveSaBBVCp6OryVFS1x_cT_K"
HTTP_PROVIDER_TESTNET = "https://eth-sepolia.g.alchemy.com/v2/psFcJCHUIyvUPQmu67oOrNViV0fT4uDy"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET