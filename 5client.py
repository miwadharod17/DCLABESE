# arithmetic_client_with_marshalling.py
import xmlrpc.client
import http.client

class VerboseTransport(xmlrpc.client.Transport):
    """ Custom transport to force new connection + print marshalled XML. """
    
    def make_connection(self, host):
        # Force new HTTP connection on every RPC call
        return http.client.HTTPConnection(host)

    def send_content(self, connection, request_body):
        print("\n---- MARSHALLED XML SENT TO SERVER ----")
        print(request_body.decode())   # print the raw marshalled XML request
        print("\n")
        super().send_content(connection, request_body)


proxy = xmlrpc.client.ServerProxy(
    "http://localhost:8000/",
    transport=VerboseTransport()
)

print("Calling add(12, 4)...")
result = proxy.add(12, 4)
print("Returned from server:", result)

print("\nCalling subtract(12, 4)...")
result_sub = proxy.subtract(12, 4)
print("Result from server:", result_sub)

print("\nCalling multiply(12, 4)...")
result_mul = proxy.multiply(12, 4)
print("Result from server:", result_mul)
