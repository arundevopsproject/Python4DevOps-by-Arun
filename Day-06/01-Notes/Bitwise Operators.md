# Bitwise Operations in Python

## Introduction

Bitwise operators in Python are used to perform operations on individual bits of binary numbers. These operators include bitwise AND, OR, XOR, and more.

## List of Bitwise Operators

1. **Bitwise AND (&):** Performs a bitwise AND operation on the binary representations of the operands.
2. **Bitwise OR (|):** Performs a bitwise OR operation.
3. **Bitwise XOR (^):** Performs a bitwise XOR operation.
4. **Bitwise NOT (~):** Flips the bits of the operand, changing 0 to 1 and 1 to 0.
5. **Left Shift (<<):** Shifts the bits to the left by a specified number of positions.
6. **Right Shift (>>):** Shifts the bits to the right.

## Examples

### Bitwise AND

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Result: 0001 (Decimal: 1)
```

### Bitwise OR

```python
x = 10  # Binary: 1010
y = 7   # Binary: 0111
result = x | y  # Result: 1111 (Decimal: 15)


=========================================================================================


 

# ✅ Harder Examples of Bitwise Operators in Python

## ✅ Bitwise Operators Quick Table

| Operator | Meaning      |    |
| -------- | ------------ | -- |
| `&`      | AND          |    |
| `        | `            | OR |
| `^`      | XOR          |    |
| `~`      | NOT (invert) |    |
| `<<`     | Left Shift   |    |
| `>>`     | Right Shift  |    |

 

# ✅ 1. Check if a Number is Power of 2 (Interview Favorite)

 
n = 32

if n & (n - 1) == 0:
    print("Power of 2")
else:
    print("Not Power of 2")
 

### Output:

Power of 2

### Why?

Power of 2 numbers have only **one bit set**.

 


# ✅ 2. Swap Two Numbers Without Temp Variable (Using XOR)

a = 15
b = 9

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)
 

### Output:

a = 9
b = 15
 

Used in low-level programming and optimization.

 


# ✅ 3. Find Odd Occurring Element (Very Common Coding Problem)

Only one number appears odd times:

arr = [4, 3, 4, 5, 5, 3, 4]

result = 0
for num in arr:
    result ^= num

print("Odd occurring element:", result)
 

### Output:

 Odd occurring element: 4
 
### Why?

XOR cancels duplicates.

 

# ✅ 4. Toggle a Bit (Feature Flag / Permissions)

flags = 0b1010

# Toggle 2nd bit
flags ^= (1 << 1)

print(bin(flags))
 

### Output:
 
0b1000
 

Used in Linux permissions, IAM flags.

 

 

# ✅ 5. Set a Specific Bit (Enable Permission)

permissions = 0b0010

# Enable 3rd bit
permissions |= (1 << 2)

print(bin(permissions))
 



# ✅ 6. Clear a Bit (Disable Permission)

permissions = 0b1111

# Clear 2nd bit
permissions &= ~(1 << 1)

print(bin(permissions))

 


# ✅ 7. Check if a Bit is Set or Not

num = 0b101101
bit_position = 3

if num & (1 << bit_position):
    print("Bit is SET")
else:
    print("Bit is NOT set")
 

 

# ✅ 8. Efficient Multiply and Divide Using Shifts

### Multiply by 8:

 
x = 7
print(x << 3)
 

### Output:

56

### Divide by 4:

x = 64
print(x >> 2)
 
Used in CPU-level optimizations.



# ✅ 9. Bitwise NOT Trick (Two’s Complement)

x = 5
print(~x)
 

### Output:

-6

### Explanation:

[
~x = -(x+1)
]

So:

* `~5 = -(5+1) = -6`

 

# ✅ 10. IP Address Subnet Mask Check (DevOps Networking Use Case)

ip = 192
mask = 255

network = ip & mask

print("Network part:", network)
 

### Output:

 Network part: 192
 
Used in routing, subnetting.

 

# ✅ 11. Extract Last Set Bit (Advanced)

n = 40  # 101000

last_set_bit = n & -n

print(last_set_bit)
 

### Output:

8
 
This is used in binary indexed trees, optimizations.

 


# ✅ 12. Count Set Bits (Hamming Weight)

n = 29  # 11101
count = 0

while n:
    n &= (n - 1)
    count += 1

print("Set bits:", count)
 

### Output:

Set bits: 4
 
Fastest bit counting algorithm.
 


# ✅ 13. XOR Encryption Example (Security Use Case)
 
data = 25
key = 12

encrypted = data ^ key
decrypted = encrypted ^ key

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
 

### Output:

Encrypted: 21
Decrypted: 25
 

Used in simple encryption & hashing logic.

 


# ✅ 14. Find Missing Number Using XOR

arr = [1, 2, 4, 5, 6]
n = 6

xor_all = 0
xor_arr = 0

for i in range(1, n + 1):
    xor_all ^= i

for num in arr:
    xor_arr ^= num

missing = xor_all ^ xor_arr

print("Missing number:", missing)

```


==============================================================================================




 

Here are **5 real DevOps examples of Python Bitwise Operator scripts** with practical use cases.

 
# 1. Linux Permission Management (chmod Style)

### Use Case: Check if a user has execute permission

```python
READ  = 0b100  # 4
WRITE = 0b010  # 2
EXEC  = 0b001  # 1

user_permission = 0b101  # Read + Execute

if user_permission & EXEC:
    print("Execute permission granted")
else:
    print("Execute permission missing")
```

### Output:

Execute permission granted


Bitwise `&` is used in real OS permission systems.





# 2. Feature Flags in Deployment Systems (Enable/Disable)

### Use Case: Toggle features during rollout

```python
FEATURE_LOGGING   = 0b0001
FEATURE_METRICS   = 0b0010
FEATURE_TRACING   = 0b0100

enabled = FEATURE_LOGGING | FEATURE_METRICS

print("Before:", bin(enabled))

# Enable tracing
enabled |= FEATURE_TRACING

print("After:", bin(enabled))
```

### Output:

Before: 0b11
After:  0b111

Used in microservice feature toggles.





# 3. Kubernetes Pod Health State Encoding (Fast Monitoring)

### Use Case: Represent multiple pod states in one integer

```python
RUNNING  = 0b0001
READY    = 0b0010
RESTARTS = 0b0100

pod_state = RUNNING | READY

if pod_state & READY:
    print("Pod is Ready")

if pod_state & RESTARTS:
    print("Pod restarting")
else:
    print("No restarts detected")
```

### Output:

Pod is Ready
No restarts detected


Bit masks allow very fast status checks.





# 4. Network Subnet Calculation (CIDR Masking)

### Use Case: Find network portion of an IP

```python
ip = 192        # last octet
subnet_mask = 240  # /28 mask = 11110000

network_part = ip & subnet_mask

print("Network Address Part:", network_part)
```

### Output:

Network Address Part: 192

Bitwise masking is core to networking & routing.





# 5. Fast Odd/Even Check in Monitoring Agents

### Use Case: Determine whether request count is odd/even

```python
requests = 157

if requests & 1:
    print("Odd number of requests")
else:
    print("Even number of requests")
```

### Output:

Odd number of requests


Much faster than `% 2` in low-level systems.





# Bonus DevOps Example: Detect Power-of-Two Autoscaling

### Use Case: Instances scale best in powers of 2

```python
instances = 8

if instances & (instances - 1) == 0:
    print("Instance count is power of 2 (optimal scaling)")
else:
    print("Not power of 2")
```

### Output:

Instance count is power of 2 (optimal scaling)


Used in autoscaling strategies.



# Summary Table (DevOps Bitwise Usage)

| DevOps Area                | Operator    |        |
| -------------------------- | ----------- | ------ |
| Linux permissions          | `&`, `      | `      |
| Feature flags rollout      | `           | `, `^` |
| Kubernetes pod state masks | `&`         |        |
| Networking subnet masking  | `&`         |        |
| Fast odd/even checks       | `&`         |        |
| Scaling optimization       | `n & (n-1)` |        |
