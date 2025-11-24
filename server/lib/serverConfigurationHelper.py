from dotenv import load_dotenv
import os

__all__ = ["serverConfig"]

class serverConfigurationHelper:
    """
    This class helps the developer load and access the plaid API environment variables. While in development it will load
    the variables from the .env file, otherwise it will just access them as normal.
    """
    required_keys = ["PLAID_CLIENT_ID","PLAID_SECRET", "PLAID_ENV", "PLAID_PRODUCTS", "PLAID_COUNTRY_CODES"]

    def __init__(self):
        # load from the .env file
        load_dotenv()

        # note any required keys that are missing
        missingRequiredKeys = [key for key in APIConfigurationHelper.required_keys if key not in os.environ]
        if( len(missingRequiredKeys) != 0 ):
            raise RuntimeError( f"Missing required environment variables {missingRequiredKeys}. If in development please ensure there is a root-level .env file " +
                               "with the required keys, if deploying, create the environment variables on your server host" )
        
        print("Required Environment variables loaded!", end="\n\n")

    def getPlaidClientId(self) -> str:
        """
        Get the plaid client ID for this server's connection to the API. Required for 
        authenticating this server with the PLAID API
        """
        return os.environ.get("PLAID_CLIENT_ID")

    def getPlaidSecret(self) -> str:
        """
        Get the plaid secret for this server's connection to the API. Required for 
        authenticating this server with the PLAID API
        """
        return os.environ.get("PLAID_SECRET")
    
    def getPlaidEnv(self) -> str:
        """
        Get the plaid environment that this server is using. Used to tell 
        the server if you arer going to use actual data or test data.
        """
        return os.environ.get("PLAID_ENV")
    
    def getPlaidProducts(self) -> list[str]:
        """
        Get the plaid products that this server can access. Used to tell the server
        what API services it wishes to use
        """
        return os.environ.get("PLAID_PRODUCTS").split(",")
    
    def getPlaidCountryCodes(self) -> list[str]:
        """
        Get the plaid country codes that this server can use. Used to determine which
        countries this server may be requesting data for.
        """
        return os.environ.get("PLAID_COUNTRY_CODES").split(",")
    
serverConfig = serverConfigurationHelper()