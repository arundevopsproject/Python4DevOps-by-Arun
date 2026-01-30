# Assignment Operations in Python

## Introduction

Assignment operators in Python are used to assign values to variables. They include the basic assignment operator (=) and various compound assignment operators that perform an operation on the variable while assigning a value.

## List of Assignment Operators

1. **Basic Assignment (=):** Assigns a value to a variable.

2. **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.

3. **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.

4. **Multiplication Assignment (*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.

5. **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.

6. **Floor Division Assignment (//=):** Performs floor division on the left operand and assigns the result to the left operand.

7. **Modulus Assignment (%=):** Calculates the modulus of the left operand and assigns the result to the left operand.

8. **Exponentiation Assignment (**=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

## Examples

### Basic Assignment

```python
x = 5
```

### Addition Assignment

y = 10
y += 3  # Equivalent to y = y + 3


======================================================================================



# Assignment Operators in Python (Hard Practice Examples)


## List of Assignment Operators

| Operator | Meaning                 | Example           |    |      |
| -------- | ----------------------- | ----------------- | -- | ---- |
| `=`      | Assign                  | `x = 10`          |    |      |
| `+=`     | Add and assign          | `x += 5`          |    |      |
| `-=`     | Subtract and assign     | `x -= 5`          |    |      |
| `*=`     | Multiply and assign     | `x *= 5`          |    |      |
| `/=`     | Divide and assign       | `x /= 5`          |    |      |
| `//=`    | Floor divide and assign | `x //= 5`         |    |      |
| `%=`     | Modulus and assign      | `x %= 5`          |    |      |
| `**=`    | Power and assign        | `x **= 5`         |    |      |
| `&=`     | Bitwise AND assign      | `x &= 5`          |    |      |
| `        | =`                      | Bitwise OR assign | `x | = 5` |
| `^=`     | Bitwise XOR assign      | `x ^= 5`          |    |      |
| `<<=`    | Left shift assign       | `x <<= 2`         |    |      |
| `>>=`    | Right shift assign      | `x >>= 2`         |    |      |

 

# 1. Multiple Assignment Updates (Interview Trap)

x = 10

x += 5
x *= 2
x -= 4

print(x)
 

### Step-by-step:

* `x = 10 + 5 = 15`
* `x = 15 * 2 = 30`
* `x = 30 - 4 = 26`

### Output:

26
 


# 2. Assignment Operator with Expression

x = 8
x += x * 2

print(x)


### Explanation:

* `x = x + (x * 2)`
* `x = 8 + 16 = 24`

### Output:

24




# 3. Floor Division Assignment with Negative Numbers

x = -17
x //= 4

print(x)


### Explanation:

* `-17 / 4 = -4.25`
* Floor becomes `-5`

 

# 4. Modulus Assignment in Cyclic Systems

Used in **round-robin scheduling**.

server_id = 17
total_servers = 5

server_id %= total_servers

print("Assigned Server:", server_id)
 
 

# 5. Exponent Assignment (Power Growth Simulation)

 
load = 2
load **= 5

print(load)
 

 

# 6. Real DevOps Example: CPU Autoscaling Increase

cpu = 45  # current usage %

cpu += 10   # spike
cpu *= 2    # scaling factor
cpu -= 15   # optimization applied

print("Final CPU:", cpu)
 

 

# 7. Compound Assignment in Loop (Production Use)

total_requests = 0

for i in range(5):
    total_requests += 100

print("Requests handled:", total_requests)




# 8. Assignment Operators with Lists (Hard Concept)

nums = [1, 2, 3]
nums *= 3

print(nums)



# 9. Assignment Operator with Strings (Tricky)

 
msg = "Deploy"
msg += " Success"

print(msg)
 



# 10. Bitwise Assignment Operator (Security + Networking)

### Example: Permission Flags

 
permission = 0b1010
permission |= 0b0100

print(bin(permission))
 

### Output:

0b1110

Used in Linux permissions, firewall rules, IAM flags.




# 11. Toggle Feature Flag Using XOR Assignment

flag = 1
flag ^= 1

print(flag)


### Output:

0

XOR toggles between ON/OFF.

 

# 12. Shift Assignment (Memory Optimization / Networking)
 
x = 8
x <<= 2

print(x)
 

### Explanation:

* Left shift by 2 = multiply by 4

 

# 13. Right Shift Assignment (Divide by Power of 2)
 
x = 64
x >>= 3

print(x)
 

### Explanation:

* Right shift by 3 = divide by 8

 


# 14. Real-World Example: AWS Billing Adjustment

 
monthly_cost = 12000

monthly_cost -= monthly_cost * 0.15  # 15% savings plan
monthly_cost += 500                 # support cost

print("Final AWS Bill:", monthly_cost)
 

### Output:

Final AWS Bill: 10700.0
 


# 15. Hard Interview Puzzle

 
x = 5
y = 10

x += y
y -= x
x -= y

print(x, y)
 
 




==============================================================================================




# Python Assignment Operators Usecases for DevOps
 


# 1. Monitoring Counter Increment (`+=`)

### Use Case: Count failed health checks in monitoring agent

```python
failed_checks = 0

health_results = ["OK", "FAIL", "OK", "FAIL", "FAIL"]

for status in health_results:
    if status == "FAIL":
        failed_checks += 1

print("Total Failed Checks:", failed_checks)
```

### Output:

Total Failed Checks: 3


Used in Prometheus exporters and monitoring scripts.





# 2. Disk Usage Update During Log Growth (`+=`, `-=`)

### Use Case: Track disk consumption after log rotation

```python
disk_used = 70  # GB

# Logs grew overnight
disk_used += 15

# Log rotation freed space
disk_used -= 10

print("Disk Used:", disk_used, "GB")
```

### Output:

Disk Used: 75 GB

Real scenario in production servers.





# 3. Retry Backoff Timer (`*=`)

### Use Case: Exponential backoff for Kubernetes API retry

```python
retry_delay = 2  # seconds

for attempt in range(3):
    print("Attempt", attempt + 1, "- Waiting", retry_delay, "seconds")
    retry_delay *= 2   # exponential increase
```

### Output:

Attempt 1 - Waiting 2 seconds
Attempt 2 - Waiting 4 seconds
Attempt 3 - Waiting 8 seconds


Used in automation tools like Terraform providers, kube clients.





# 4. AWS Cost Optimization Calculation (`-=`, `+=`)

### Use Case: Apply Savings Plan discount + support charges

```python
monthly_cost = 20000  # INR

# Apply 20% Savings Plan discount
monthly_cost -= monthly_cost * 0.20

# Add support plan cost
monthly_cost += 1500

print("Final AWS Monthly Bill:", monthly_cost)
```

### Output:

Final AWS Monthly Bill: 17500.0

Common in FinOps automation.





# 5. Load Balancer Request Distribution (`%=`)

### Use Case: Round-robin request assignment across servers

```python
server_index = 0
servers = ["srv1", "srv2", "srv3"]

for req in range(7):
    print("Request", req, "->", servers[server_index])

    server_index += 1
    server_index %= len(servers)  # wrap around
```

### Output:

Request 0 -> srv1
Request 1 -> srv2
Request 2 -> srv3
Request 3 -> srv1
Request 4 -> srv2
Request 5 -> srv3
Request 6 -> srv1
```

Used in load balancing algorithms.





# Bonus Example: CPU Threshold Adjustment (`//=`)

### Use Case: Reduce CPU allocation when scaling down

```python
cpu_limit = 800  # millicores

# Scale down by half
cpu_limit //= 2

print("New CPU Limit:", cpu_limit, "m")
```

### Output:

New CPU Limit: 400 m

Used in Kubernetes resource tuning.


# Summary Table (DevOps Assignment Operator Usage)

| Operator | DevOps Use Case              |
| -------- | ---------------------------- |
| `+=`     | Counters, log size growth    |
| `-=`     | Disk cleanup, cost reduction |
| `*=`     | Retry backoff scaling        |
| `%=`     | Round-robin scheduling       |
| `//=`    | Resource scaling down        |

