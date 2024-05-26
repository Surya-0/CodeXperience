# import requests
# import logging
#
# # Set up logging
# logging.basicConfig(level=logging.INFO)
#
#
# # Outbound Gateway class
# class OutboundGateway:
#     def __init__(self, allowlist):
#         self.allowlist = allowlist
#
#     def validate_url(self, request_url):
#         # Validate request URL to prevent SSRF
#         if any(domain in request_url for domain in self.allowlist):
#             return True
#         else:
#             return False
#
#     def make_request(self, request_url, request_method='GET', headers=None, data=None):
#         try:
#             # Make request to external service
#             response = requests.request(request_method, request_url, headers=headers, data=data)
#             response.raise_for_status()
#             return response.text
#         except Exception as e:
#             logging.error(f"Error making request to {request_url}: {str(e)}")
#             return None
#
#
# # Main application
# def main():
#     # Initialize Outbound Gateway with allowlist
#     gateway = OutboundGateway(['google.com', 'api.github.com'])
#
#     # Example request from main application
#     # request_url = 'https://example.com/api/data'
#     request_url = 'https://google.com/api/data'
#     request_method = 'POST'
#     headers = {'Content-Type': 'application/json'}
#     data = '{"key": "value"}'
#
#     # Validate request URL
#     if gateway.validate_url(request_url):
#         # Make request through Outbound Gateway
#         response = gateway.make_request(request_url, request_method, headers, data)
#         if response is not None:
#             print(response)
#     else:
#         logging.error("Invalid request URL")
#
#
# if __name__ == "__main__":
#     main()

import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


# Outbound Gateway class
class OutboundGateway:
    def __init__(self, allowlist):
        self.allowlist = allowlist

    def validate_url(self, request_url):
        # Validate request URL to prevent SSRF
        if any(domain in request_url for domain in self.allowlist):
            return True
        else:
            return False

    def make_request(self, request_url, request_method='GET', headers=None, data=None):
        try:
            # Make request to external service
            response = requests.request(request_method, request_url, headers=headers, data=data)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"Error making request to {request_url}: {str(e)}")
            return None


# Main application
def main():
    # Initialize Outbound Gateway with allowlist
    gateway = OutboundGateway(['api.github.com'])

    # Example request from main application
    request_url = 'https://httpbin.org/post'
    request_method = 'POST'
    headers = {'Content-Type': 'application/json'}
    data = '{"key": "value"}'

    # Validate request URL
    if gateway.validate_url(request_url):
        # Make request through Outbound Gateway
        response = gateway.make_request(request_url, request_method, headers, data)
        if response is not None:
            print(response)
    else:
        logging.error("Invalid request URL")


if __name__ == "__main__":
    main()