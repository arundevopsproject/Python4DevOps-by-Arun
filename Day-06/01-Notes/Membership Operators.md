# Membership Operations in Python

## Introduction

Membership operators in Python are used to check whether a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators are "in" and "not in."

## List of Membership Operators

1. **in:** Returns `True` if the left operand is found in the sequence on the right.
2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### Examples

#### in Operator

```python
fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
# result will be True
```

#### not in Operator

```python
colors = ["red", "green", "blue"]
result = "yellow" not in colors
# result will be True
```

====================================================================================================

 

# Membership Operators Recap

| Operator | Meaning                                     |
| -------- | ------------------------------------------- |
| `in`     | True if value exists in sequence/collection |
| `not in` | True if value does NOT exist                |

Works with:

✅ strings
✅ lists
✅ tuples
✅ sets
✅ dictionaries
✅ custom objects

 

# 1. Membership in Nested Lists (Harder)

```python
matrix = [[1, 2], [3, 4], [5, 6]]

print([3, 4] in matrix)
print(3 in matrix)
```

### Output:

```
True
False
```

### Explanation:

* Checks full element `[3,4]`
* Does NOT search inside inner lists automatically
 



# 2. Membership Inside Nested Elements

```python
matrix = [[1, 2], [3, 4], [5, 6]]

print(any(3 in row for row in matrix))
```

### Output:

```
True
```

Used for deep searching.

 



# 3. Dictionary Membership Checks Keys Only

```python
data = {"name": "Arun", "role": "DevOps"}

print("role" in data)
print("DevOps" in data)
```

### Output:

```
True
False
```

### Explanation:

* `in` checks keys, not values

 



# 4. Check Membership in Dictionary Values

```python
data = {"name": "Arun", "role": "DevOps"}

print("DevOps" in data.values())
```

### Output:

```
True
```

 



# 5. Membership in Sets (Fast Lookup)

```python
blocked_ips = {"192.168.1.10", "10.0.0.5"}

print("10.0.0.5" in blocked_ips)
```

### Output:

```
True
```

Sets are O(1) lookup → best for large datasets.

---

---

# 6. Substring Membership in Strings (Tricky)

```python
log = "ERROR: Disk space low on node-1"

print("Disk" in log)
print("disk" in log)
```

### Output:

```
True
False
```

### Explanation:

Membership is case-sensitive.

 



# 7. Membership with `not in` (Validation Use Case)

```python
allowed_envs = ["dev", "stage", "prod"]

env = "test"

if env not in allowed_envs:
    print("Invalid Environment!")
```

### Output:

```
Invalid Environment!
```

Used in CI/CD pipelines.

 



# 8. Membership in List of Dictionaries (DevOps JSON Example)

```python
pods = [
    {"name": "nginx", "status": "Running"},
    {"name": "redis", "status": "Pending"}
]

print(any(pod["name"] == "redis" for pod in pods))
```

### Output:

```
True
```

Harder real-world membership check.

 



# 9. Membership in Custom Class (`__contains__`)

```python
class Cluster:
    def __init__(self, nodes):
        self.nodes = nodes

    def __contains__(self, node):
        return node in self.nodes

c = Cluster(["node1", "node2"])

print("node1" in c)
print("node3" in c)
```

### Output:

```
True
False
```

Shows advanced Python OOP membership.

 


# 10. Performance Trap: List vs Set Membership

```python
large_list = list(range(1000000))
large_set = set(large_list)

print(999999 in large_list)  # Slow
print(999999 in large_set)   # Fast
```

### Explanation:

* List membership is O(n)
* Set membership is O(1)

Used in real systems optimization.

 



# Bonus Interview Practice Questions

### Q1:

Predict output:

```python
x = "abc"
print("a" in x and "d" not in x)
```

 

### Q2:

```python
nums = [1, 2, [3, 4]]
print(3 in nums)
```

 

### Q3:

```python
d = {"a": 1, "b": 2}
print(2 in d)
```

 

# Real DevOps Use Case Example (CI/CD)

```python
required_files = ["Dockerfile", "deployment.yaml", "Jenkinsfile"]

repo_files = ["Dockerfile", "deployment.yaml"]

missing = [f for f in required_files if f not in repo_files]

print("Missing files:", missing)
```

### Output:

```
Missing files: ['Jenkinsfile']
```

 

# Key Interview Notes

| Collection     | `in` checks           |
| -------------- | --------------------- |
| String         | Characters/Substrings |
| List/Tuple     | Elements              |
| Set            | Elements (fastest)    |
| Dictionary     | Keys only             |
| Custom Objects | Uses `__contains__`   |



============================================================================================



 
# Python Membership Operators Usecases for DevOps


# 1. CI/CD Pipeline Validation (Required Files Check)

### Use Case: Ensure repository has required deployment files

```python
required_files = ["Dockerfile", "Jenkinsfile", "deployment.yaml"]

repo_files = ["Dockerfile", "deployment.yaml"]

missing = [f for f in required_files if f not in repo_files]

if missing:
    print("Pipeline Failed! Missing files:", missing)
else:
    print("All required files exist. Proceed with build.")
```

### Output:

Pipeline Failed! Missing files: ['Jenkinsfile']
 



# 2. Kubernetes Pod Status Monitoring

### Use Case: Detect unhealthy pod states

```python
pod_status = "CrashLoopBackOff"

bad_states = ["CrashLoopBackOff", "Error", "Pending"]

if pod_status in bad_states:
    print("Pod is unhealthy:", pod_status)
else:
    print("Pod is healthy")
```

### Output:

Pod is unhealthy: CrashLoopBackOff
 

 


# 3. Log File Error Scanner (Production Incident Detection)

### Use Case: Scan logs for critical keywords

```python
log_line = "ERROR: Disk space low on node-2"

if "ERROR" in log_line or "CRITICAL" in log_line:
    print("🚨 Alert! Critical issue found in logs")
```

### Output:

Alert! Critical issue found in logs
 

 


# 4. Security Blocklist / Allowlist Check (Firewall Automation)

### Use Case: Block malicious IPs

```python
blocked_ips = {"192.168.1.100", "10.0.0.23", "172.16.5.9"}

incoming_ip = "10.0.0.23"

if incoming_ip in blocked_ips:
    print("Access Denied for IP:", incoming_ip)
else:
    print("Access Allowed")
```

### Output:
 
Access Denied for IP: 10.0.0.23
 
### Why Set?

Membership lookup is O(1), very fast.

 



# 5. Environment Configuration Validation (Dev/Stage/Prod)

### Use Case: Prevent wrong environment deployments

```python
allowed_envs = ["dev", "stage", "prod"]

env = "test"

if env not in allowed_envs:
    print("Invalid environment! Deployment stopped.")
else:
    print("Environment valid. Deploying...")
```

### Output:

Invalid environment! Deployment stopped.


 

# Bonus DevOps Membership Example (Docker Image Tag Check)

```python
image_tag = "latest"

restricted_tags = ["latest", "dev"]

if image_tag in restricted_tags:
    print("Avoid using restricted Docker tags in production!")
```

 

# Summary: DevOps Usage of Membership Operators

| DevOps Task                          | Operator Used    |
| ------------------------------------ | ---------------- |
| File existence in repo               | `in / not in`    |
| Kubernetes unhealthy pod detection   | `in`             |
| Log scanning for errors              | `"ERROR" in log` |
| Security allow/block list checks     | `in` with sets   |
| Prevent wrong environment deployment | `not in`         |

 