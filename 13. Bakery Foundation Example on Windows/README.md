# 🍞 Bakery Foundation with Packer on AWS (Ubuntu Guide)

Welcome to the **Bakery Foundation** project! This repo contains everything you need to automate the creation of an AWS AMI with **Python 3.9** installed, using **Packer** on a **Ubuntu machine**. Whether you're new to Packer, AWS, or image baking, this guide will get you up and running in no time.

---

## 📦 What You'll Build

- ✅ A reusable Packer template using HCL2
- ✅ An Ubuntu-based AWS AMI with Python 3.9 pre-installed
- ✅ A deployed EC2 instance from your custom AMI
- ✅ SSH into your instance and verify Python

---

## 🛠 Prerequisites

- Ubuntu machine (local or VM)
- AWS account with IAM credentials
- Basic knowledge of CLI and EC2
- AWS CLI installed and configured
- Packer installed

---

## 🔧 Setup Instructions

### 1. Install Packer

```bash
sudo apt update
sudo apt install unzip wget -y
wget https://releases.hashicorp.com/packer/1.10.0/packer_1.10.0_linux_amd64.zip
unzip packer_1.10.0_linux_amd64.zip
sudo mv packer /usr/local/bin/
packer --version
```

### 2. Install AWS CLI

```bash
sudo apt install awscli -y
aws --version
```

### 3. Configure AWS CLI

```bash
aws configure
# Enter:
# AWS Access Key ID
# AWS Secret Access Key
# Default region: us-east-1 (or your region)
# Output format: json
```

---

## 📁 Project Structure

```
packer-bakery/
│
├── bakery.pkr.hcl   # Main Packer template
└── README.md        # This file!
```

---

## 🧱 Packer Template (`bakery.pkr.hcl`)

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

source "amazon-ebs" "python39" {
  ami_name      = "bakery-foundation-python39-${formatdate("YYYYMMDD-HHmmss", timestamp())}"
  instance_type = "t2.micro"
  region        = var.aws_region
  source_ami    = "ami-xxxxxxxxxxxxxxxxx" # Replace with valid AMI ID
  ssh_username  = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.python39"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y python3.9 python3.9-venv python3.9-dev"
    ]
  }
}
```

### 🧠 Tip: Get the Latest Ubuntu 20.04 AMI

```bash
aws ec2 describe-images   --owners 099720109477   --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"   --query "Images | sort_by(@, &CreationDate)[-1].ImageId"   --region us-east-1   --output text
```

---

## ⚙️ Build and Bake the AMI

### Step 1: Initialize and Validate Packer

```bash
cd packer-bakery
packer init .
packer validate bakery.pkr.hcl
```

### Step 2: Build the AMI 🎂

```bash
packer build bakery.pkr.hcl
```

☑️ This will:
- Launch a temporary EC2 instance
- Install Python 3.9
- Create an AMI
- Terminate the instance

---

## 🚀 Deploy the AMI

### Step 1: Go to AWS Console → EC2 → AMIs
- Look for the AMI named: `bakery-foundation-python39-<timestamp>`

### Step 2: Launch an Instance
- Go to **Instances → Launch Instance**
- Select **My AMIs** → Your AMI
- Choose instance type: `t2.micro`
- Create/Select a Key Pair
- Allow SSH (port 22) in Security Group

---

## 🔗 SSH into Instance (Ubuntu)

```bash
chmod 400 your-key.pem
ssh -i "your-key.pem" ubuntu@<your-instance-ip>
```

---

## 🐍 Verify Python Installation

```bash
python3.9 --version
# Output: Python 3.9.5
```

### Bonus Checks:

```bash
python3 --version     # Should show 3.8.x
python --version      # Likely not found
```

### Make `python` point to Python 3.9 (Optional)

```bash
sudo ln -s /usr/bin/python3.9 /usr/bin/python
python --version  # Should now show 3.9.5
```

---

## 🧠 Why This Matters

Ubuntu 20.04 defaults to Python 3.8 and **does not include `python`** by default to avoid confusion with old Python 2.x scripts. This image solves that by explicitly installing Python 3.9, making it a great base image for modern apps.

---

## 🎉 You Did It!

✅ Installed Packer  
✅ Baked a Python-ready AMI  
✅ Launched and connected to EC2  
✅ Verified Python 3.9 setup

---

## 🤝 Contribute / Fork / Star

If you find this useful, feel free to:
- ⭐ Star the repo
- 🍴 Fork and customize
- 📥 Open issues or pull requests

---

## 📜 License

MIT License

---

Built with ❤️ by [Your Name]
