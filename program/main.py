from constants import ABORT_ALL_POSITION, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices_test

if __name__ == "__main__":
    
    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ",e)
        exit(1)

    # Abort all open position
    if ABORT_ALL_POSITION:
        try:
            print("Closing all positions...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all positions: ",e)
            exit(1)
    
    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        #Contruct Market Prices
        try:
            print("Fething market prices, please allow 3 mins..")
            df_market_prices = construct_market_prices_test(client)
        except Exception as e:
            print("Error constructing market prices: ", e)
            exit(1)
    