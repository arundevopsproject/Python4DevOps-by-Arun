# Relational Operations in Python

## Introduction

Relational operators in Python are used to compare two values and determine the relationship between them. These operators return a Boolean result, which is either `True` or `False`.

## List of Relational Operators

1. **Equal to (==):** Checks if two values are equal.

2. **Not equal to (!=):** Checks if two values are not equal.

3. **Greater than (>):** Checks if the left operand is greater than the right operand.

4. **Less than (<):** Checks if the left operand is less than the right operand.

5. **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

6. **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

## Examples

### Equal to

```python
a = 5
b = 5
result = a == b
# result will be True
```

### Not equal to

```python
x = 10
y = 7
result = x != y
# result will be True
```



==========================================================================================




#  Python Relational Operators Usecases for DevOps  

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

 


# 1. CPU Threshold Alert (Monitoring Script)

### Scenario: Trigger alert if CPU usage exceeds 90%

```python
cpu_usage = 93

if cpu_usage > 90:
    print("ALERT: CPU usage is critically high!")
```

### Output:

ALERT: CPU usage is critically high!
 
Used in CloudWatch agents, Prometheus exporters.




# 2. Disk Space Warning (Production Reliability)

### Scenario: Alert if free disk is less than 15%

```python
disk_free_percent = 12

if disk_free_percent < 15:
    print("WARNING: Disk space running low!")
```

### Output:

WARNING: Disk space running low!
 
Common in node-level monitoring.

 



# 3. Kubernetes Pod Restart Detection (Health Check)

### Scenario: Pod is unstable if restart count is greater than or equal to 5

```python
restart_count = 7

if restart_count >= 5:
    print("Pod is unstable: Too many restarts")
```

### Output:

Pod is unstable: Too many restarts

Used in Kubernetes readiness diagnostics.

 



# 4. CI/CD Deployment Gate (Branch Validation)

### Scenario: Deployment allowed only if branch is `main`

```python
branch = "feature-login"

if branch != "main":
    print("Deployment blocked: Not main branch")
```

### Output:

Deployment blocked: Not main branch

Used in Jenkins/GitHub Actions pipelines.





# 5. AWS Auto Scaling Decision (Load-Based Scaling)

### Scenario: Scale out if request count crosses threshold

```python
requests_per_minute = 1200
scale_threshold = 1000

if requests_per_minute > scale_threshold:
    print("Scale Out: Add more EC2 instances")
else:
    print("Load is normal")
```

### Output:

Scale Out: Add more EC2 instances

Used in autoscaling policies and custom scripts.

 


# Bonus Real-World DevOps Example (Security Compliance)

### Scenario: Password length must be at least 12 characters

```python
password = "Admin123"

if len(password) < 12:
    print("Weak Password: Must be at least 12 characters")
```

### Output:

Weak Password: Must be at least 12 characters

Used in security validation scripts.





# Interview Practice Questions (DevOps Style)

### Q1:

```python
memory = 82
if memory <= 80:
    print("Normal")
else:
    print("High Memory Usage")
```



### Q2:

```python
pods_running = 5
pods_expected = 5

print(pods_running == pods_expected)
```



### Q3:

```python
latency = 250
if latency > 200:
    print("API Slow")
```



# Key DevOps Insight

Relational operators are the foundation for:

✅ Alert thresholds
✅ Deployment approvals
✅ Resource scaling
✅ Pod health checks
✅ SLA monitoring

