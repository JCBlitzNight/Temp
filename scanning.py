import collections
import math

# Initialize hash tables
Source = collections.defaultdict(lambda: [0, 0])
Candidate = collections.defaultdict(int)

# Set threshold values
c = 5 # minimum number of flows required to calculate FSD entropy
alpha = 0.5 # threshold for FSD entropy
eta0 = 0.5 # lower threshold for likelihood ratio
eta1 = 1.5 # upper threshold for likelihood ratio

def update(srcip, fsd):
    """
    Update likelihood ratio for srcip based on FSD entropy.
    """
    # Get current likelihood ratio for srcip
    ratio = Candidate[srcip]
    # If srcip has not been seen before, set ratio to 1
    if ratio == 0:
        ratio = 1

    # Check if srcip has enough flows to calculate FSD entropy
    if Source[srcip][0] < c:
        return

    # Check if FSD entropy is below threshold alpha
    if fsd < alpha:
        # Update ratio with successful event
        ratio *= (1/0.9) / (1/0.1) * (0.9/0.1) / (0.1/0.9)
    else:
        # Update ratio with unsuccessful event
        ratio *= 0.1 / 0.9

    # Check if updated ratio is above upper threshold eta1
    if ratio >= eta1:
        # Flag srcip as a scanner and remove from Candidate hash table
        del Candidate[srcip]
        print(f"{srcip} is a scanner!")
    # Check if updated ratio is below lower threshold eta0
    elif ratio <= eta0:
        # Remove srcip from Candidate hash table
        del Candidate[srcip]
    else:
        # Update likelihood ratio for srcip in Candidate hash table
        Candidate[srcip] = ratio

# Simulate flow data
flows = [
    ("192.168.1.1", 100),
    ("192.168.1.1", 200),
    ("192.168.1.1", 150),
    ("192.168.1.2", 50),
    ("192.168.1.2", 75),
    ("192.168.1.2", 80),
    ("192.168.1.3", 40),
    ("192.168.1.3", 60),
    ("192.168.1.4", 200),
    ("192.168.1.4", 150),
    ("192.168.1.5", 100),
    ("192.168.1.6", 100),
]

# Process flows
for srcip, size in flows:
    # Update flow count for srcip in Source hash table
    Source[srcip][0] += 1
    # Update flow size distribution for srcip in Source hash table
    if size in Source[srcip][1]:
        Source[srcip][1][size] += 1
    else:
        Source[srcip][1][size] = 1
    # Calculate FSD entropy for srcip
    counts = list(Source[srcip][1].values())
    total = sum(counts)
    ps = [c/total for c in counts]
    entropy = -sum([p * math.log2(p) for p in ps])
    Source[srcip][2] = entropy
    # Update likelihood ratio for srcip
    update(srcip, entropy)
