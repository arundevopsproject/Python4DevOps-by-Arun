
 # 10 no of Production-Grade Complete Python Scripts on DevOps / DevSecOps / AWS Cloud use cases.

### These scripts include:

    ✅ Proper structure
    ✅ Functions + main()
    ✅ Logging
    ✅ Exception handling
    ✅ Config-driven design
    ✅ Real-world automation readiness

 

# 1. Production Jenkins Build Status Handler

```python
import logging

logging.basicConfig(level=logging.INFO)

def handle_build_status(status: str):
    try:
        if status == "SUCCESS":
            logging.info("Build successful. Deploying to production...")
        elif status == "UNSTABLE":
            logging.warning("Build unstable. Deploy only to staging.")
        elif status == "FAILED":
            logging.error("Build failed. Stopping pipeline & notifying team.")
        else:
            logging.error("Unknown build status received.")

    except Exception as e:
        logging.exception(f"Error handling build status: {e}")


def main():
    build_status = "FAILED"
    handle_build_status(build_status)


if __name__ == "__main__":
    main()
```

 


# 2. AWS EC2 Instance State Validator (Production Script)

```python
import logging

logging.basicConfig(level=logging.INFO)

def validate_ec2_state(state: str):
    if state == "running":
        logging.info("EC2 instance is running normally.")
    elif state == "stopped":
        logging.warning("EC2 instance stopped. Trigger start action.")
    elif state == "terminated":
        logging.critical("Instance terminated! Restore required.")
    else:
        logging.error("Unknown instance state. Manual investigation needed.")


def main():
    instance_state = "stopped"
    validate_ec2_state(instance_state)


if __name__ == "__main__":
    main()
```

 


# 3. Kubernetes Pod Health Monitoring Script

```python
import logging

logging.basicConfig(level=logging.INFO)

def check_pod_health(status: str):
    if status == "Running":
        logging.info("Pod is healthy.")
    elif status == "Pending":
        logging.warning("Pod pending. Check scheduler or node capacity.")
    elif status == "CrashLoopBackOff":
        logging.error("Pod crashing repeatedly. Check logs immediately.")
    else:
        logging.error("Unknown pod state detected.")


def main():
    pod_status = "CrashLoopBackOff"
    check_pod_health(pod_status)


if __name__ == "__main__":
    main()
```

 


# 4. Docker Restart Policy Compliance Checker

```python
import logging

logging.basicConfig(level=logging.INFO)

def validate_restart_policy(policy: str):
    if policy == "always":
        logging.info("Restart policy OK: High availability ensured.")
    elif policy == "on-failure":
        logging.warning("Restarts only on failure. Evaluate risk.")
    elif policy == "no":
        logging.error("No restart policy. Production risk detected!")
    else:
        logging.error("Invalid restart policy.")


def main():
    restart_policy = "no"
    validate_restart_policy(restart_policy)


if __name__ == "__main__":
    main()
```

 


# 5. AWS S3 Bucket Public Access Audit (DevSecOps)

```python
import logging

logging.basicConfig(level=logging.INFO)

def audit_bucket_access(access_level: str):
    if access_level == "private":
        logging.info("S3 bucket is secure.")
    elif access_level == "public":
        logging.critical("SECURITY ALERT: Bucket is public!")
    else:
        logging.error("Unknown bucket access level. Audit required.")


def main():
    bucket_access = "public"
    audit_bucket_access(bucket_access)


if __name__ == "__main__":
    main()
```

 


# 6. IAM Role Permission Risk Analyzer

```python
import logging

logging.basicConfig(level=logging.INFO)

def analyze_iam_permission(policy: str):
    if policy == "ReadOnlyAccess":
        logging.info("IAM permission safe.")
    elif policy == "AdministratorAccess":
        logging.critical("High risk: Full admin access granted!")
    else:
        logging.warning("Custom policy detected. Review needed.")


def main():
    permission = "AdministratorAccess"
    analyze_iam_permission(permission)


if __name__ == "__main__":
    main()
```




# 7. Deployment Environment Configuration Script

```python
import logging

logging.basicConfig(level=logging.INFO)

def configure_environment(env: str):
    if env == "dev":
        logging.info("Development mode: Debug logging enabled.")
    elif env == "staging":
        logging.info("Staging mode: Running QA and performance tests.")
    elif env == "prod":
        logging.info("Production mode: Monitoring + Alerts enabled.")
    else:
        logging.error("Invalid environment value!")


def main():
    env = "prod"
    configure_environment(env)


if __name__ == "__main__":
    main()
```

 


# 8. CloudWatch Alarm-Based Auto Scaling Trigger

```python
import logging

logging.basicConfig(level=logging.INFO)

def cpu_scaling_decision(cpu_usage: int):
    if cpu_usage < 70:
        logging.info("CPU usage normal.")
    elif cpu_usage < 90:
        logging.warning("CPU high. Scaling may be needed soon.")
    else:
        logging.critical("CPU critical! Trigger Auto Scaling immediately.")


def main():
    cpu_usage = 92
    cpu_scaling_decision(cpu_usage)


if __name__ == "__main__":
    main()
```


 

# 9. Vulnerability Severity Response Automation (DevSecOps)

```python
import logging

logging.basicConfig(level=logging.INFO)

def vulnerability_action(severity: str):
    if severity == "LOW":
        logging.info("Low severity. Log and monitor.")
    elif severity == "MEDIUM":
        logging.warning("Medium severity. Fix in next sprint.")
    elif severity == "HIGH":
        logging.critical("High severity. Patch immediately!")
    else:
        logging.error("Unknown vulnerability severity.")


def main():
    severity = "HIGH"
    vulnerability_action(severity)


if __name__ == "__main__":
    main()
```




# 10. Terraform Plan Validation Script Before Apply

```python
import logging

logging.basicConfig(level=logging.INFO)

def validate_terraform_plan(result: str):
    if result == "no_changes":
        logging.info("Terraform: No infra changes required.")
    elif result == "changes_detected":
        logging.warning("Terraform changes detected. Review required.")
    elif result == "failed":
        logging.critical("Terraform failed. Fix errors before apply.")
    else:
        logging.error("Unknown Terraform output state.")


def main():
    terraform_result = "changes_detected"
    validate_terraform_plan(terraform_result)


if __name__ == "__main__":
    main()
```



 

 
