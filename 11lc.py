servers = {"S1": 0, "S2": 3, "S3": 0}  # server : active_connections

def load_balancer(request):
    # pick server with minimum active connections
    server = min(servers, key=servers.get)
    servers[server] += 1
    print(f"Request {request} → {server} (load = {servers[server]})")

print("\nLeast Connections Load Distribution:\n")
for r in range(1, 10):
    load_balancer(r)

