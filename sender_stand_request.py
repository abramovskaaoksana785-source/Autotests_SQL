import requests
import configuration


def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                          json = order_body)

def get_order(track):
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + f"{track}")