# Simple Bully Algorithm Simulation

nodes = [1, 2, 3, 4, 5]      # priorities (5 is highest)
alive = {n: True for n in nodes}
coordinator = max(nodes)     # highest priority initially


def print_state():
    print("\nAlive Nodes:", [n for n in nodes if alive[n]])
    print("Current Coordinator:", coordinator)


def fail_node(n):
    global coordinator
    alive[n] = False
    print(f"\n*** Node {n} FAILED ***")
    if n == coordinator:
        print("Coordinator failed!")


def start_election(starter):
    global coordinator

    print(f"\nNode {starter} starts an ELECTION")

    higher = [n for n in nodes if n > starter and alive[n]]

    if not higher:
        # this node becomes coordinator
        coordinator = starter
        print(f"Node {starter} becomes the NEW COORDINATOR")
        return

    for h in higher:
        print(f"Node {starter} -> ELECTION -> Node {h}")
        print(f"Node {h} -> OK -> Node {starter}")

    # highest alive node wins
    new_coord = max(higher)
    coordinator = new_coord
    print(f"\nNode {new_coord} becomes the NEW COORDINATOR")


print_state()

# Coordinator fails
fail_node(5)

# Node 2 starts election
start_election(2)
print_state()

# Another failure
fail_node(4)

# Node 3 starts election
start_election(3)
print_state()
