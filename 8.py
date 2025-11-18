# Simple Ring Election Algorithm

processes = [1, 2, 3, 4, 5]      # arranged in a ring
alive = {p: True for p in processes}
coordinator = max(processes)     # highest ID = leader


def fail(p):
    global coordinator
    alive[p] = False
    print(f"\n*** Process {p} FAILED ***")
    if p == coordinator:
        print("Leader failed!")


def ring_election(starter):
    global coordinator

    print(f"\nProcess {starter} STARTS ELECTION")
    msg = []
    idx = processes.index(starter)

    # pass message clockwise in the ring
    for _ in processes:
        p = processes[idx]
        if alive[p]:
            msg.append(p)
            print(f"Election message at Process {p}: {msg}")
        idx = (idx + 1) % len(processes)
        if processes[idx] == starter:
            break

    # highest alive becomes leader
    coordinator = max(msg)
    print(f"\nNEW LEADER ELECTED: Process {coordinator}")


def show_state():
    print("\nAlive:", [p for p in processes if alive[p]])
    print("Leader:", coordinator)


# ---------------- DEMO ----------------

show_state()

fail(5)            # leader fails
ring_election(2)   # process 2 starts election
show_state()

fail(4)
ring_election(1)
show_state()
