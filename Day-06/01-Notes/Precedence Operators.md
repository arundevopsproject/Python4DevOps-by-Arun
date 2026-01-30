# Precedence of Operations in Python

## Introduction

Precedence of operations in Python defines the order in which different types of operators are evaluated in an expression. Operators with higher precedence are evaluated first.

## Examples

### Arithmetic Precedence

```python
result = 5 + 3 * 2
# Multiplication has higher precedence, so result is 11, not 16
```

===================================================================================================


# Python Precedence Operators Usecases for DevOps


# 1. CPU + Memory Alert Rule (Logical Precedence)

### Scenario: Alert if CPU is high AND memory is high OR disk is critically low.

```python
cpu = 92
memory = 78
disk = 5

if cpu > 90 and memory > 80 or disk < 10:
    print("ALERT: Critical Resource Issue")
```

### Precedence:

* `and` executes before `or`

So it becomes:

```python
(cpu > 90 and memory > 80) or (disk < 10)
```

### Output:

```
ALERT: Critical Resource Issue
```

Disk condition triggers alert even though memory is not high.





# 2. Kubernetes Pod Health Check (not + and precedence)

### Scenario: Pod is unhealthy if NOT running AND restart count is high.

```python
status = "Pending"
restarts = 6

if not status == "Running" and restarts > 5:
    print("Pod Unhealthy")
```

### Precedence:

* `not` happens before `and`

Equivalent:

```python
(not (status == "Running")) and (restarts > 5)
```

### Output:

Pod Unhealthy




# 3. AWS Billing Calculation (Arithmetic Precedence)

### Scenario: Apply discount first, then add support cost.

```python
base_cost = 20000
discount = 0.10
support_fee = 500

final_bill = base_cost - base_cost * discount + support_fee
print(final_bill)
```

### Precedence:

* Multiplication before subtraction

Steps:

* `base_cost * discount = 2000`
* `20000 - 2000 = 18000`
* `18000 + 500 = 18500`

### Output:

18500.0
Wrong parentheses could cause incorrect billing.




# 4. CI/CD Deployment Condition (Membership + Logical Precedence)

### Scenario: Deploy only if branch is main OR release AND pipeline passed.

```python
branch = "release"
pipeline_passed = True

if branch == "main" or branch == "release" and pipeline_passed:
    print("Deployment Allowed")
```

### Precedence:

* `and` executes before `or`

So it becomes:

```python
(branch == "main") or ((branch == "release") and pipeline_passed)
```

### Output:

Deployment Allowed

If pipeline_passed was False, release would not deploy.



### Best Practice (Clear Parentheses)

```python
if (branch in ["main", "release"]) and pipeline_passed:
    ...
```



# 5. Bitwise Precedence in Linux Permission Flags (Security)

### Scenario: Check if write permission is enabled.

```python
permissions = 0b1101   # rwx style bits
WRITE = 0b0010

if permissions & WRITE == WRITE:
    print("Write Permission Enabled")
```

### Precedence Problem:

This is evaluated as:

```python
permissions & (WRITE == WRITE)
```

Because `==` has higher precedence than `&`

So:

```python
WRITE == WRITE → True → 1
permissions & 1 → wrong check
```

This is a real security bug.


### Correct Version:

```python
if (permissions & WRITE) == WRITE:
    print("Write Permission Enabled")
```

### Output:

Write Permission Enabled




# Summary Table (DevOps Priority)

| Operator Type | Example              | Runs First         |
| ------------- | -------------------- | ------------------ |
| Arithmetic    | `*` before `+`       | Multiplication     |
| Comparison    | `>` before `and`     | Comparisons        |
| Logical       | `not` > `and` > `or` | Logical precedence |
| Bitwise       | `&` after `==`       | Needs parentheses  |
| Membership    | `in` before `and/or` | Condition checks   |





# DevOps Interview Practice Questions

### Q1:

```python
cpu = 95
disk = 20
print(cpu > 90 or disk < 10 and cpu > 80)
```


### Q2:

```python
branch = "dev"
passed = True
print(branch == "main" or branch == "dev" and passed)
```


