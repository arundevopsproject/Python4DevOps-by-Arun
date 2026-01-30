# Logical Operations in Python

## Introduction

Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.

## List of Logical Operators

1. **AND (and):** Returns `True` if both operands are `True`.
2. **OR (or):** Returns `True` if at least one of the operands is `True`.
3. **NOT (not):** Returns the opposite Boolean value of the operand.

## Examples

### AND Operator

```python
x = True
y = False
result = x and y
# result will be False
```

### OR Operator

```python
a = True
b = False
result = a or b
# result will be True
```



=============================================================================================

 

# Logical Operators in Python (10 Harder Examples)

## Logical Operators Recap

| Operator | Meaning                                |
| -------- | -------------------------------------- |
| `and`    | True if both conditions are True       |
| `or`     | True if at least one condition is True |
| `not`    | Reverses the condition                 |

 

# 1. Short-Circuit Behavior (`and`)

 
x = 0

result = x and (10 / x)
print(result)
 
### Explanation:

* `and` stops early if first value is falsy (`0`)
* Division never happens → avoids crash

 

# 2. Short-Circuit Behavior (`or`)

x = 0

result = x or 100
print(result)
 
### Output:
 
100

### Explanation:

* `or` returns first truthy value

 

 

# 3. Logical Operators Return Values (Not Always True/False)

print("DevOps" and "Kubernetes")
 

### Output:

Kubernetes
 
### Explanation:

* `and` returns last evaluated operand

 


# 4. `or` Returns First Truthy Operand

print("" or None or "AWS")
 
### Output:

AWS
 
Used in fallback/default values.

 


# 5. Operator Precedence Trap

result = True or False and False
print(result)
 
### Output:
 
True

### Explanation:

* `and` has higher precedence than `or`

So:

True or (False and False)
True or False
True
 


# 6. Complex Condition (Interview Style)

 
x = 15

if x > 10 and x < 20 and not x == 18:
    print("Valid number")

### Output:

Valid number

Used in range validation.

 

 

# 7. Truthy/Falsy Values with `and/or`

print([] or "Default List")
print({} and "Not Empty")
 

### Output:

Default List
{}

### Explanation:

* Empty list is falsy → `or` picks fallback
* Empty dict is falsy → `and` stops early

 


# 8. Authentication Example (Real DevOps Logic)

user = "admin"
password = "1234"
otp_verified = False

if user == "admin" and password == "1234" and otp_verified:
    print("Login Success")
else:
    print("Access Denied")
 

### Output:

Access Denied

All must be true.

 


# 9. Multiple Conditions with `or` (Service Health Check)

cpu = 92
memory = 60

if cpu > 90 or memory > 85:
    print("ALERT: High Resource Usage")

### Output:

ALERT: High Resource Usage


Used in monitoring systems.

 

# 10. Nested Logical Expressions (Hard Interview)

a = True
b = False
c = True

result = a and (b or c) and not b
print(result)

### Output:

True

### Explanation:

* `(b or c)` → True
* `not b` → True
* All True → final True

 

# Key Interview Rules

| Concept                      | Example                  |
| ---------------------------- | ------------------------ |
| `and` stops at first falsy   | `0 and 5 → 0`            |
| `or` stops at first truthy   | `"AWS" or "GCP" → AWS`   |
| Returns operand, not bool    | `"A" and "B" → B`        |
| `not` flips result           | `not True → False`       |
| Precedence: `not > and > or` | Important in expressions |

 


 ====================================================================================



# Python Logical Operators Usecases for DevOps
 

# 1. CI/CD Deployment Gate (Tests + Branch Check)

### Use Case: Deploy only if on `main` AND tests passed

```python
branch = "main"
tests_passed = True

if branch == "main" and tests_passed:
    print("Deployment Approved")
else:
    print("Deployment Blocked")
```

### Output:

Deployment Approved
 

🔹 Real use in GitHub Actions/Jenkins pipelines.

 

 

# 2. Kubernetes Pod Health Check (Crash or Pending Detection)

### Use Case: Alert if pod is NOT running OR in bad state

```python
pod_status = "CrashLoopBackOff"

if pod_status != "Running" and pod_status != "Succeeded":
    print("Pod Unhealthy:", pod_status)
```

### Output:

Pod Unhealthy: CrashLoopBackOff

Logical `and` ensures correct validation.

 

 

# 3. Monitoring Alert Rule (CPU OR Memory Threshold)

### Use Case: Trigger alert if CPU > 90% OR Memory > 85%

```python
cpu = 92
memory = 60

if cpu > 90 or memory > 85:
    print("ALERT: High Resource Usage!")
else:
    print("System Stable")
```

### Output:

ALERT: High Resource Usage!
 
Used in Prometheus alert rules and Python monitoring agents.

 

 
# 4. Security Access Control (Admin + MFA Required)

### Use Case: Allow access only if user is admin AND MFA enabled

```python
is_admin = True
mfa_enabled = False

if is_admin and mfa_enabled:
    print("Access Granted")
else:
    print("Access Denied: MFA Required")
```

### Output:
 
Access Denied: MFA Required
 
Very common in IAM + Zero Trust security logic.

 

 

# 5. Prevent Wrong Environment Deployment (NOT + OR Logic)

### Use Case: Block deployment if environment is NOT prod OR approval missing

```python
environment = "prod"
approved = False

if not approved or environment != "prod":
    print("Deployment Blocked")
else:
    print("Deployment Allowed")
```

### Output:
 
Deployment Blocked
 
Ensures production deploys happen only with approval.

 

 

# Bonus Real DevOps Example: Auto Scaling Decision

### Use Case: Scale up if load is high AND instances are below limit

```python
cpu_load = 88
instances = 3
max_instances = 5

if cpu_load > 80 and instances < max_instances:
    print("Scaling Up Instances...")
else:
    print("No Scaling Needed")
```

### Output:

Scaling Up Instances...
 

 

# Summary Table (DevOps Logical Operator Usage)

| Scenario                            | Operator   |
| ----------------------------------- | ---------- |
| Deploy only if conditions met       | `and`      |
| Alert if any threshold exceeded     | `or`       |
| Block access if missing requirement | `not`      |
| Multi-condition health checks       | `and + or` |
| Approval + environment enforcement  | `not + or` |

 