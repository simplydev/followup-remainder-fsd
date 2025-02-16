import http.client
from src.config import settings
from src.application.app_utils import get_http_connn
from auth0.authentication import GetToken
from urllib.parse import quote


def get_mgmt_access_token()->str:
    print("inside the mgmt token call")
    get_token = GetToken(settings.auth0_domain, settings.auth0_client_id, client_secret=settings.auth0_client_secret)
    token = get_token.client_credentials('https://{}/api/v2/'.format(settings.auth0_domain))
    mgmt_api_token = token['access_token']
    return mgmt_api_token

def get_user_by_id(user_id:str, access_token:str):
    print("inside the get_user_by_id call the access token is "+access_token)
    #access_token_mgmt = get_mgmt_access_token()
    #print("access_token_mgmt is "+access_token_mgmt)
    conn = get_http_connn(settings.auth0_domain)
    headers = { 'authorization': "Bearer "+access_token }
    print("headers is "+str(headers))
    print("conn  is "+str(conn))
    print("auth0_domain  is "+settings.auth0_domain)
    print("user_id  is "+user_id)
    print(f"/{settings.auth0_domain}/api/v2/users/{user_id}")
    user_id = quote(user_id)
    conn.request("GET", f"/api/v2/users/{user_id}", headers=headers)
    res = conn.getresponse()
    print("res is "+str(res))
    data = res.read()
    print(data.decode("utf-8"))
    data = data.decode("utf-8")
    return data

