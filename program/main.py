from constants import ABORT_ALL_POSITION, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message

# MAIN FUNCTION
if __name__ == "__main__":

    # Message on start
    send_message("Bot launch successful..")
    
    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ",e)
        # Send Message
        send_message(f"Failed to connect to client {e}")
        exit(1)

    # Abort all open position
    if ABORT_ALL_POSITION:
        try:
            print("Closing all positions...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all positions: ",e)
            send_message(f"Error closing all positions {e}")
            exit(1)
    
    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        #Contruct Market Prices
        try:
            print("Fetching market prices, please allow 3 mins..")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error constructing market prices: ", e)
            send_message(f"Error constructing market prices {e}")
            exit(1)

        # Store Cointegrated Pairs
        try:
            print("Storing cointegrated pairs...")
            stores_result = store_cointegration_results(df_market_prices)
            if stores_result != "saved":
                print("Error saving cointegration results.")
        except Exception as e:
            print("Error saving cointegration results: ", e)
            send_message(f"Error saving cointegration results {e}")
            exit(1)
    
    # Run as always on
    while MANAGE_EXITS or PLACE_TRADES:

        # Place trades for open positions
        if MANAGE_EXITS:
            try:
                print("Managing exists..")
                manage_trade_exits(client)
            except Exception as e:
                print("Error managing exiting positions: ", e)
                send_message(f"Error managing exiting position {e}")
                exit(1)    

        # Place trades for open positions
        if PLACE_TRADES:
            try:
                print("Finding trading oportunities..")
                open_positions(client)
            except Exception as e:
                print("Error trading pairs: ", e)
                send_message(f"Error opening trades {e}")
                exit(1)
    