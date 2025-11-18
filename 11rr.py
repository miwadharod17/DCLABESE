servers = ["S1", "S2", "S3"]
pointer = 0   # round robin pointer

def load_balancer(request):
    global pointer
    server = servers[pointer]
    pointer = (pointer + 1) % len(servers)
    print(f"Request {request} → {server}")

print("Round Robin Load Distribution:\n")
for r in range(1, 10):
    load_balancer(r)
