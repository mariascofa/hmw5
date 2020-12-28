
from django.utils.deprecation import MiddlewareMixin
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

class LoggsMiddleware(MiddlewareMixin):

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     logging.info("proccess {}".format(view_func))

    def process_response(self, request, response):
        logging.info("response %s", response)
        return response

    # process = process_view
    # logging.info("proccess {}".format(process))
    # print ("proccess {}".format(process))
    #
    # response = process_response
    # logging.info("response {}".format(response))
    # print("response {}".format(response))

