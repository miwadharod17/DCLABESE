import time

# 3 replicas
replica_A = {"x": 10}
replica_B = {"x": 10}
replica_C = {"x": 10}

replicas = [replica_A, replica_B, replica_C]


def show_state(label):
    print(f"\n--- {label} ---")
    print("Replica A:", replica_A)
    print("Replica B:", replica_B)
    print("Replica C:", replica_C)


def eventual_update(key, value):
    print("\nReplica A UPDATED first (others not updated yet)")
    replica_A[key] = value


def propagate():
    print("\nPropagating update to other replicas (after delay)...")
    time.sleep(1)   # simulate network delay
    replica_B["x"] = replica_A["x"]
    replica_C["x"] = replica_A["x"]


# ---------------- DEMONSTRATION ----------------

show_state("Initial State (Strongly Consistent)")

eventual_update("x", 99)
show_state("AFTER UPDATE (Not consistent → Eventual Consistency)")

propagate()
show_state("AFTER PROPAGATION (Consistency Achieved Eventually)")
