
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


##################

#Step-1: Calculate the hours
total_seconds = 5000

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

#Step-2: Calculate the minutes
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, "hours:", minutes, "minutes:", seconds, "seconds:")


