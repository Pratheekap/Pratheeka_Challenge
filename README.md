# SED Challenge

## Infrastructure Problem Statement

For this project, please think about how you would architect a scalable and secure static web application in AWS.


* Create and deploy a running instance of a web server using a configuration management tool of your choice. The web server should serve one page with the following content. 

```
<html>
<head>
<title>Hello World</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
```

* Secure this application and host such that only appropriate ports are publicly exposed and any http requests are redirected to https. This should be automated using a configuration management tool of your choice and you should feel free to use a self-signed certificate for the web server.
* Develop and apply automated tests to validate the correctness of the server configuration.


## Technology Used:

* Ansible
    - Automation tool that is used for configuration management, executing consistent
    server-side tasks, and web application deployments.
* Packer 
    - It is a open source tool that is used for making machine images (ami) from
    source configuration. Packer has made it really easy to automate the process of provisioning instance without manual configuration.
* AWS
    - Using Services like EC2, Autoscaling , Security Groups

## Execution:

```bash
  ansible-playbook main.yml -v 
```

## Implementation:

In the main.yml i have created the tasks based on the requirement

### Task : Run Packer build for creating AMI

 * Created AWS ami using Packer job. In Packer Job, configured below Ansible roles and added test cases in this roles using handlers :
    - ngnix : installation,configuration,copy the static html to server
    - ssl: installed ssl,created ssl certificates 
    - securesite: configured the ngnix http/https app configuration files.
### Task : Creating Security Group

* Allowing 80 and 443 Ports

### Task : Creating launch configuration and ASG 

* Once Packer Job is completed based upon the output. I have created autoscaling groups with high scalability and availability for the application
