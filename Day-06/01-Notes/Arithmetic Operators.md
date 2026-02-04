# Arithmetic Operations in Python

## Introduction

Arithmetic operators in Python allow you to perform basic mathematical calculations on numeric values. These operators include addition, subtraction, multiplication, division, and more.

## List of Arithmetic Operators

1. **Addition (+):** Adds two numbers.
2. **Subtraction (-):** Subtracts the right operand from the left operand.
3. **Multiplication (*):** Multiplies two numbers.
4. **Division (/):** Divides the left operand by the right operand (results in a floating-point number).
5. **Floor Division (//):** Divides the left operand by the right operand and rounds down to the nearest whole number.
6. **Modulus (%):** Returns the remainder of the division of the left operand by the right operand.
7. **Exponentiation (**):** Raises the left operand to the power of the right operand.

## Examples

### Addition

```python
a = 5
b = 3
result = a + b
print(result)  # Output: 8
```

### Subtraction

```python
x = 10
y = 7
result = x - y
print(result)  # Output: 3
```



=============================================================================



# Practice Example:


# Harder Python Arithmetic Operator Examples


# 1. Operator Precedence (Very Common Interview Trap)


result = 10 + 5 * 2 ** 2
print(result)



# 2. Floor Division with Negative Numbers (Tricky)

a = -15
b = 4

Floor_value = -15//4
print("Floor_value: ", Floor_value)


### Explanation:

Floor division always rounds **down**, not toward zero.

* `-15 / 4 = -3.75`
* Floor becomes `-4`

### Output:

-4




# 3. Modulus with Negative Numbers (Very Confusing)


print(-15 % 4)


Python ensures:

[
(a // b) * b + (a % b) = a
]

So:

* `-15 // 4 = -4`
* `(-4 * 4) = -16`
* remainder = `1`

### Output:

1




# 4. Time Conversion Problem (Real-World)

Convert seconds into hours, minutes, seconds.


# Convert seconds into hours, minutes, and seconds
# Using floor division and modulus operators

seconds = 3672

# Step 1: Calculate hours
hours = seconds // 3600

# Step 2: Find remaining seconds after removing hours
remaining = seconds % 3600

# Step 3: Calculate minutes from remaining seconds
minutes = remaining // 60

# Step 4: Find final seconds after removing minutes
secs = remaining % 60

# Output result
print(hours, "hours", minutes, "minutes", secs, "seconds")



### Output:

1 hours 1 minutes 12 seconds



# 5. Extract Last Digit and Remove Last Digit

num = 98765

last_digit = num % 10
remaining = num // 10

print("Last digit:", last_digit)
print("Remaining number:", remaining)


### Output:

Last digit: 5
Remaining number: 9876




# 6. Check if a Number is Even or Odd Without `if`


n = 27
print("Odd" * (n % 2) + "Even" * (1 - n % 2))


### Output:

Odd




# 7. Swap Two Numbers Without Temporary Variable


a = 15
b = 9

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)


### Output:

a = 9
b = 15




# 8. Reverse a 3-Digit Number Using Arithmetic Operators

num = 543

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

reverse = ones * 100 + tens * 10 + hundreds
print(reverse)


### Output:

345



# 9. Compound Arithmetic Assignment (DevOps Useful)

cpu_usage = 40

cpu_usage += 15   # spike
cpu_usage *= 2    # scaling effect
cpu_usage -= 10   # optimization

print(cpu_usage)

### Output:

120




# 10. Real DevOps Example: Disk Space Alert Calculation


total_disk = 500  # GB
used_disk = 423

free_disk = total_disk - used_disk
free_percent = (free_disk / total_disk) * 100

print("Free Space:", free_disk, "GB")
print("Free Percentage:", free_percent, "%")


### Output:

Free Space: 77 GB
Free Percentage: 15.4 %




# 11. Billing System with Tax + Discount

price = 1200
quantity = 4

subtotal = price * quantity

discount = subtotal * 10 / 100
after_discount = subtotal - discount

tax = after_discount * 18 / 100
final_price = after_discount + tax

print("Final Bill =", final_price)


### Output:

Final Bill = 5097.6




# 12. Large Number Power with Modulus (Crypto Style)


print((7 ** 100) % 13)

Used in cryptography, hashing, security systems.


# 13. Interview Challenge: Digital Root Using Arithmetic

Example: 987 → 9+8+7 = 24 → 2+4 = 6


num = 987

root = 1 + (num - 1) % 9
print(root)


### Output:

6



# 14. Find Middle Value Without Sorting (Arithmetic Trick)

a, b, c = 15, 9, 12

middle = a + b + c - max(a, b, c) - min(a, b, c)
print("Middle =", middle)


### Output:

Middle = 12



# 15. Split Money into Notes (ATM Problem)

amount = 3786

notes_2000 = amount // 2000
amount %= 2000

notes_500 = amount // 500
amount %= 500

notes_100 = amount // 100
amount %= 100

print("2000 =", notes_2000)
print("500  =", notes_500)
print("100  =", notes_100)
print("Remaining =", amount)

### Output:

2000 = 1
500  = 3
100  = 2
Remaining = 86


