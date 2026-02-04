
 
# Full Enterprise Grade Python Scripts for 10 use case with:

✅ Use Case / Scenario Name
✅ Detailed Real Production Explanation
✅ Complete Production Python Script
✅ Every line explained with inline `#` comments inside script only

 

 

# ✅ USE CASE 1: Jenkins CI/CD Build Status Validation & Deployment Decision

---

## Scenario Explanation

In real DevOps pipelines, Jenkins builds application code and runs unit/integration tests.

Before deployment:

* If build is **SUCCESS** → deploy to production
* If build is **UNSTABLE** → deploy only to staging
* If build is **FAILED** → stop pipeline and alert team

This prevents broken releases reaching customers.

 

## Production Python Script

```python
import logging  # Import logging module for production-level logs

logging.basicConfig(level=logging.INFO)  # Configure logging output level

def handle_build_status(status: str):
    """
    Determines deployment action based on Jenkins build result.
    """

    try:
        # If build passed successfully
        if status == "SUCCESS":
            logging.info("Build SUCCESS. Deploying to production...")

        # If build has warnings or minor test failures
        elif status == "UNSTABLE":
            logging.warning("Build UNSTABLE. Deploy only to staging.")

        # If build failed completely
        elif status == "FAILED":
            logging.error("Build FAILED. Stopping pipeline and notifying DevOps team.")

        # If Jenkins returns unexpected status
        else:
            logging.error("Unknown build status received. Manual investigation needed.")

    except Exception as e:
        # Log unexpected runtime exceptions
        logging.exception(f"Error while processing build status: {e}")


def main():
    build_status = "FAILED"  # Example build output from Jenkins job
    handle_build_status(build_status)  # Execute deployment decision logic


if __name__ == "__main__":
    main()  # Script entry point
```

 

# USE CASE 2: AWS EC2 Instance Auto-Healing State Monitoring

 

## Scenario Explanation

In production AWS environments, EC2 instances may stop unexpectedly due to:

* OS crash
* Resource exhaustion
* Manual shutdown
* AWS maintenance

DevOps automation detects instance state:

* running → OK
* stopped → restart required
* terminated → disaster recovery needed

 

## Production Python Script

```python
import logging  # Import logging module for monitoring output

logging.basicConfig(level=logging.INFO)  # Enable INFO logs

def validate_ec2_state(state: str):
    """
    Validates EC2 instance lifecycle state for auto-remediation.
    """

    # Instance running means service is available
    if state == "running":
        logging.info("EC2 is RUNNING. No action required.")

    # Stopped instance must be restarted to restore uptime
    elif state == "stopped":
        logging.warning("EC2 is STOPPED. Trigger start automation.")

    # Terminated instance means server is deleted
    elif state == "terminated":
        logging.critical("EC2 TERMINATED. Disaster recovery required immediately.")

    # Unknown state requires manual AWS console check
    else:
        logging.error("Unknown EC2 state. Investigate manually.")


def main():
    instance_state = "stopped"  # Example EC2 state from monitoring system
    validate_ec2_state(instance_state)  # Validate instance health


if __name__ == "__main__":
    main()  # Run script execution
```

 

# USE CASE 3: Kubernetes Pod Health Check & Crash Detection

 

## Scenario Explanation

In Kubernetes production clusters, pods may fail due to:

* misconfiguration
* missing secrets
* application crash
* resource limits

Common pod states:

* Running → healthy
* Pending → scheduling issue
* CrashLoopBackOff → repeated failure

 

## Production Python Script

```python
import logging  # Import logging for Kubernetes monitoring

logging.basicConfig(level=logging.INFO)  # Setup logging level

def check_pod_health(status: str):
    """
    Checks Kubernetes pod state and triggers troubleshooting actions.
    """

    # Pod running means application is healthy
    if status == "Running":
        logging.info("Pod is RUNNING. Service is healthy.")

    # Pod pending means Kubernetes cannot schedule it
    elif status == "Pending":
        logging.warning("Pod is PENDING. Check node resources or scheduler.")

    # CrashLoopBackOff means container repeatedly crashes
    elif status == "CrashLoopBackOff":
        logging.error("Pod in CRASH LOOP. Immediate debugging required.")

    # Unknown pod status needs manual kubectl investigation
    else:
        logging.error("Unknown pod status detected. Manual investigation needed.")


def main():
    pod_status = "CrashLoopBackOff"  # Example failing pod state
    check_pod_health(pod_status)  # Execute pod health validation


if __name__ == "__main__":
    main()  # Script entry point
```

 

# USE CASE 4: Docker Restart Policy Compliance Validation

 

## Scenario Explanation

In production Docker workloads, containers must restart automatically after:

* node reboot
* application crash
* kernel patching

Restart policies:

* always → best for production
* on-failure → limited recovery
* no → dangerous

 

## Production Python Script

```python
import logging  # Import logging for compliance validation

logging.basicConfig(level=logging.INFO)  # Enable log monitoring

def validate_restart_policy(policy: str):
    """
    Validates Docker container restart policy for HA compliance.
    """

    # Always restart ensures uptime after reboot/crash
    if policy == "always":
        logging.info("Restart policy ALWAYS. High availability ensured.")

    # Restart only on failure, not after reboot
    elif policy == "on-failure":
        logging.warning("Restart policy ON-FAILURE. Evaluate availability risk.")

    # No restart policy means container will stay down permanently
    elif policy == "no":
        logging.error("Restart policy NONE. Production outage risk!")

    # Invalid policy configuration
    else:
        logging.error("Invalid restart policy detected.")


def main():
    restart_policy = "no"  # Example incorrect container configuration
    validate_restart_policy(restart_policy)  # Validate container resiliency


if __name__ == "__main__":
    main()  # Execute script
```

 

# USE CASE 5: AWS S3 Public Bucket Exposure Security Audit

 

## Scenario Explanation

One of the biggest AWS security risks is:

S3 buckets accidentally made public.

This can expose:

* customer data
* logs
* backups
* compliance documents

DevSecOps teams automate detection.

 

## Production Python Script

```python
import logging  # Import logging for security alerts

logging.basicConfig(level=logging.INFO)  # Configure logging output

def audit_bucket_access(access_level: str):
    """
    Detects if S3 bucket is publicly accessible.
    """

    # Private bucket is secure
    if access_level == "private":
        logging.info("S3 bucket PRIVATE. No security risk.")

    # Public bucket is a critical security incident
    elif access_level == "public":
        logging.critical("SECURITY ALERT: S3 bucket is PUBLIC!")

    # Unknown access means permissions must be audited
    else:
        logging.error("Unknown bucket access level. Run IAM/S3 audit.")


def main():
    bucket_access = "public"  # Example risky bucket permission
    audit_bucket_access(bucket_access)  # Perform access security validation


if __name__ == "__main__":
    main()  # Script execution entry point
```

 

# USE CASE 6: IAM Permission Risk & Least Privilege Enforcement


## Scenario Explanation

IAM permissions must follow:

Least Privilege Principle

Giving AdministratorAccess is dangerous because attackers can:

* delete infrastructure
* steal data
* create rogue users

 

## Production Python Script

```python
import logging  # Import logging for IAM governance

logging.basicConfig(level=logging.INFO)  # Setup logging

def analyze_iam_permission(policy: str):
    """
    Detects dangerous IAM permissions assigned to roles/users.
    """

    # ReadOnly is safe for audit users
    if policy == "ReadOnlyAccess":
        logging.info("IAM policy READ-ONLY. Safe access level.")

    # AdministratorAccess is critical security risk
    elif policy == "AdministratorAccess":
        logging.critical("HIGH RISK: Full admin access detected!")

    # Custom policies require manual review
    else:
        logging.warning("Custom IAM policy detected. Review permissions manually.")


def main():
    permission = "AdministratorAccess"  # Example risky policy assignment
    analyze_iam_permission(permission)  # Run risk analysis


if __name__ == "__main__":
    main()  # Execute script
```

 

# USE CASE 7: Environment-Based Deployment Configuration Control

 

## Scenario Explanation

DevOps deployments differ per environment:

* Dev → debugging enabled
* Staging → QA testing enabled
* Prod → monitoring and alerting required

Wrong config causes incidents.

 

## Production Python Script

```python
import logging  # Import logging module

logging.basicConfig(level=logging.INFO)  # Configure logging

def configure_environment(env: str):
    """
    Applies environment-specific deployment behavior.
    """

    # Development environment supports debugging
    if env == "dev":
        logging.info("DEV mode: Debug logging enabled.")

    # Staging is used for testing before production
    elif env == "staging":
        logging.info("STAGING mode: Running QA and load tests.")

    # Production requires monitoring, stability, alerts
    elif env == "prod":
        logging.info("PRODUCTION mode: Monitoring + Alerts enabled.")

    # Invalid environment selection is misconfiguration
    else:
        logging.error("Invalid environment provided. Deployment blocked.")


def main():
    env = "prod"  # Example environment selection
    configure_environment(env)  # Execute environment configuration


if __name__ == "__main__":
    main()  # Run script
```

 

# USE CASE 8: CloudWatch CPU Alarm Auto Scaling Decision

 

## Scenario Explanation

AWS workloads scale based on CPU metrics:

* Normal load → no action
* High load → warning
* Critical load → auto scale out

This prevents downtime during traffic spikes.

 

## Production Python Script

```python
import logging  # Import logging for scaling alerts

logging.basicConfig(level=logging.INFO)  # Configure logging

def cpu_scaling_decision(cpu_usage: int):
    """
    Determines scaling action based on CPU utilization.
    """

    # CPU usage normal, no scaling required
    if cpu_usage < 70:
        logging.info("CPU normal. No scaling needed.")

    # CPU high, scaling should be planned soon
    elif cpu_usage < 90:
        logging.warning("CPU high. Prepare scaling event.")

    # CPU critical, immediate scaling required
    else:
        logging.critical("CPU critical! Trigger Auto Scaling now.")


def main():
    cpu_usage = 92  # Example threshold breach value
    cpu_scaling_decision(cpu_usage)  # Execute scaling logic


if __name__ == "__main__":
    main()  # Script entry point
```

 

# USE CASE 9: DevSecOps Vulnerability Severity Deployment Gate

 

## Scenario Explanation

Security scanners detect CVEs.

Pipeline action depends on severity:

* LOW → monitor
* MEDIUM → fix soon
* HIGH → block release immediately

 

## Production Python Script

```python
import logging  # Import logging for security enforcement

logging.basicConfig(level=logging.INFO)  # Configure logging

def vulnerability_action(severity: str):
    """
    Automates DevSecOps vulnerability response policy.
    """

    # Low severity issues can be monitored
    if severity == "LOW":
        logging.info("LOW severity vulnerability. Logging only.")

    # Medium issues must be fixed soon
    elif severity == "MEDIUM":
        logging.warning("MEDIUM severity. Fix in next sprint.")

    # High severity must block deployment immediately
    elif severity == "HIGH":
        logging.critical("HIGH severity! Deployment blocked until patch applied.")

    # Unknown severity requires manual security review
    else:
        logging.error("Unknown severity detected. Security team review needed.")


def main():
    severity = "HIGH"  # Example critical vulnerability
    vulnerability_action(severity)  # Execute security gate logic


if __name__ == "__main__":
    main()  # Run script
```

 

# USE CASE 10: Terraform Infrastructure Plan Validation Before Apply

 

## Scenario Explanation

Terraform plan must be validated because:

* It may destroy resources
* It may create unexpected infra
* Apply must not run blindly

Automation ensures safe IaC governance.

 

## Production Python Script

```python
import logging  # Import logging for IaC pipeline control

logging.basicConfig(level=logging.INFO)  # Enable logging

def validate_terraform_plan(result: str):
    """
    Validates Terraform plan output before apply step.
    """

    # No changes means safe execution
    if result == "no_changes":
        logging.info("Terraform plan clean. No infra changes required.")

    # Changes detected require approval
    elif result == "changes_detected":
        logging.warning("Terraform changes detected. Approval required before apply.")

    # Terraform failure blocks pipeline execution
    elif result == "failed":
        logging.critical("Terraform failed. Fix errors before apply.")

    # Unknown output requires investigation
    else:
        logging.error("Unknown Terraform plan result. Manual review needed.")


def main():
    terraform_result = "changes_detected"  # Example terraform plan output
    validate_terraform_plan(terraform_result)  # Execute infra validation


if __name__ == "__main__":
    main()  # Script entry point
```


