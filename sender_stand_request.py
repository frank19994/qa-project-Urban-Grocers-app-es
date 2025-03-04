import requests
import configuration
import data
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                         headers=data.headers)

def post_new_kit(kit_body, auth_token):
    curren_headers = data.headers.copy()
    curren_headers['Authorization'] = "Bearer " + auth_token
    return  requests.post(configuration.URL_SERVICE +configuration.KITS_PATH,
                          json=kit_body,
                          headers=curren_headers)
