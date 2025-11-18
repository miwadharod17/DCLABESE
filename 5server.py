# arithmetic_server.py
from xmlrpc.server import SimpleXMLRPCServer

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Arithmetic RPC Server started on port 8000...")

# Define arithmetic functions
def add(a, b):
    print(f"Server: add({a}, {b}) called")
    return a + b

def subtract(a, b):
    print(f"Server: subtract({a}, {b}) called")
    return a - b

def multiply(a, b):
    print(f"Server: multiply({a}, {b}) called")
    return a * b

# Register functions so client can call them remotely
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")

# Keep server running
server.serve_forever()
