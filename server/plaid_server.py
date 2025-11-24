from flask import Flask
from lib.serverConfigurationHelper import serverConfig
import plaid
from plaid.api import plaid_api

# create the configuration object for our plaid api connection
configuration = plaid.Configuration(
    host= serverConfig.getPlaidEnv(),
    api_key= {
        "client_id": serverConfig.getPlaidClientId(),
        "secret": serverConfig.getPlaidSecret()
    }
)

# use the client object to send future requests to the API, it will automatically
# include all of our configuration info
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def baseRequest():
    return "This endpoint is not configured for use, please use an intended API route", 400

@app.route("/request-link", methods=["GET"])
def requestLink():
    pass