
# 10 real-time Python scripts using if / elif / else conditions focused on DevOps, DevSecOps, and AWS Cloud interview-grade scenarios.

### Each script is practical and reflects real production decision-making logic.

 

# 1. Check Jenkins Build Status

```python
build_status = "FAILED"

if build_status == "SUCCESS":
    print("Deploy to production.")
elif build_status == "UNSTABLE":
    print("Deploy to staging only.")
else:
    print("Stop pipeline and notify DevOps team.")
```

Use Case: CI/CD deployment decision based on Jenkins build result.

 


# 2. AWS EC2 Instance State Validator

```python
instance_state = "stopped"

if instance_state == "running":
    print("Instance is healthy.")
elif instance_state == "stopped":
    print("Start the instance immediately.")
else:
    print("Instance state unknown. Investigate manually.")
```

Use Case: Auto-remediation logic for EC2 monitoring.

 


# 3. Kubernetes Pod Health Check

```python
pod_status = "CrashLoopBackOff"

if pod_status == "Running":
    print("Pod is healthy.")
elif pod_status == "Pending":
    print("Check node resources or scheduling issues.")
else:
    print("Pod failure detected. Restart or debug logs.")
```

Use Case: K8s troubleshooting automation.

 


# 4. Docker Container Restart Policy Check

```python
restart_policy = "no"

if restart_policy == "always":
    print("Container will restart automatically.")
elif restart_policy == "on-failure":
    print("Restarts only if container exits with error.")
else:
    print("No restart policy. High availability risk!")
```

Use Case: Production container resilience validation.




# 5. AWS S3 Bucket Public Access Check (DevSecOps)

```python
bucket_access = "public"

if bucket_access == "private":
    print("Bucket is secure.")
elif bucket_access == "public":
    print("Security Alert: Bucket exposure risk!")
else:
    print("Access level unknown. Audit required.")
```

Use Case: Cloud security compliance enforcement.

 


# 6. IAM Role Permission Risk Detection

```python
permission = "AdministratorAccess"

if permission == "ReadOnlyAccess":
    print("Safe permission level.")
elif permission == "AdministratorAccess":
    print("Critical Risk: Full access granted!")
else:
    print("Custom policy. Review manually.")
```

Use Case: IAM least privilege monitoring.

 

# 7. Deployment Environment Decision

```python
env = "prod"

if env == "dev":
    print("Enable debug logging.")
elif env == "staging":
    print("Run performance tests.")
else:
    print("Production mode: Enable monitoring + alerts.")
```

Use Case: Environment-based configuration control.

 


# 8. AWS CloudWatch Alarm Response

```python
cpu_usage = 92

if cpu_usage < 70:
    print("CPU usage normal.")
elif cpu_usage < 90:
    print("CPU high. Consider scaling soon.")
else:
    print("Critical CPU! Trigger Auto Scaling now.")
```

Use Case: Auto-scaling decision logic.




# 9. DevSecOps Vulnerability Severity Action

```python
severity = "HIGH"

if severity == "LOW":
    print("Log and monitor.")
elif severity == "MEDIUM":
    print("Fix in next sprint.")
else:
    print("Immediate patch required before deployment!")
```

Use Case: Security gate in CI pipeline.

 


# 10. Terraform Plan Validation Before Apply

```python
terraform_result = "changes_detected"

if terraform_result == "no_changes":
    print("Safe: No infra changes required.")
elif terraform_result == "changes_detected":
    print("Review changes before applying.")
else:
    print("Terraform failed. Check state file or syntax.")
```

Use Case: Infrastructure-as-Code approval logic.

 


# Bonus Script (Interview Favorite): Blue-Green Deployment Decision

```python
traffic_shift = "green"

if traffic_shift == "blue":
    print("Deploy new version to BLUE environment.")
elif traffic_shift == "green":
    print("Deploy new version to GREEN environment.")
else:
    print("Invalid deployment target. Abort release.")
```

Use Case: Production deployment strategy automation.

 

# Summary Table

| Script # | Domain         | Use Case                  |
| -------- | -------------- | ------------------------- |
| 1        | CI/CD          | Jenkins build decision    |
| 2        | AWS            | EC2 auto-recovery         |
| 3        | Kubernetes     | Pod health automation     |
| 4        | Docker         | Restart policy validation |
| 5        | DevSecOps      | S3 security audit         |
| 6        | AWS IAM        | Permission risk check     |
| 7        | DevOps         | Environment config        |
| 8        | AWS Monitoring | Auto-scaling trigger      |
| 9        | DevSecOps      | Vulnerability gate        |
| 10       | Terraform      | IaC validation            |

 
