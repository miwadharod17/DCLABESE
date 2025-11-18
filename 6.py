# Number of processes
N = 3

# Initialize vector clocks
VC = [[0]*N for _ in range(N)]   # VC[i] is clock of process i

events = []

def internal(pid):
    VC[pid][pid] += 1
    events.append((f"P{pid} internal", VC[pid][:]))

def send(pid, dest):
    VC[pid][pid] += 1
    msg = VC[pid][:]
    events.append((f"P{pid} send->P{dest}", msg))
    return msg

def receive(pid, msg, src):
    for i in range(N):
        VC[pid][i] = max(VC[pid][i], msg[i])
    VC[pid][pid] += 1
    events.append((f"P{pid} recv<-P{src}", VC[pid][:]))


internal(0)              # P0 internal
internal(1)              # P1 internal

m1 = send(0, 1)          # P0 -> P1
receive(1, m1, 0)        # P1 receives

m2 = send(1, 2)          # P1 -> P2
receive(2, m2, 1)        # P2 receives

internal(2)              # P2 internal

# print results
print("\nVECTOR CLOCK EVENTS\n")
for desc, clock in events:
    print(f"{desc:20}  -->  {clock}")
