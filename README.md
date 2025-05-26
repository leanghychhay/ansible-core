# ansible-core

The main repository for the Ansible Core where all the role and our playbook file will be kept base on project requirements.

### Before generate new role, please make sure you have vault config file from ansible-core directory: ###

```bash
echo "my_strong_vault_password" > .vault_config
chmod 600 .vault_config
```

## new_role.py ##

This script creates a new Ansible role with the specified name and description. It initializes the role directory structure and creates a README file.

## Usage
```bash
python new_role.py role-name
```

## Project Structure
```
/home/leanghy/ansible-core$ tree
.
├── LICENSE
├── README.md
├── ansible.cfg
├── inventories
│   ├── production
│   │   ├── group_vars
│   │   │   └── sample_group_vars.yml
│   │   ├── host_vars
│   │   │   └── sameple_host_vars.yml
│   │   └── hosts
│   └── staging
│       ├── group_vars
│       │   └── sample_group_vars.yml
│       ├── host_vars
│       │   └── sample_host_vars.yml
│       └── hosts
├── new_role.py
├── playbooks
│   └── sample.yaml
└── roles
    └── sample
        ├── README.md
        ├── defaults
        │   └── main.yml
        ├── files
        ├── handlers
        │   └── main.yml
        ├── meta
        ├── tasks
        │   └── main.yml
        └── templates
```

### File and Directory Description
- **README.md**: This file, providing an overview of the project.
- **ansible.cfg**: Configuration file for Ansible.
- **inventories**: Directory containing inventory files and variables for different environments.
    - **production**: Inventory for the production environment.
    - **staging**: Inventory for staging enviroment.
- **new_role.py**: Script for creating new Ansible roles.
- **playbooks**: Directory containing playbooks.
    - **sample.yml**: Sample playbook.
- **roles**: Directory containing roles.
    - **Other-Role**: Can de develop depend on project required in the future.

### Usage

1. **Setup Ansible Configuration**: Ensure ansible.cfg is properly configured for your environment.
2. **Inventory Files**: Update inventory files in the inventories directory with your host information.
3. **Run Playbooks**: Execute the desired playbook using the ansible-playbook command. For example:

## Simple way to run ansible playbook

Dry-Run Mode:

```bash
ansible-playbook playbooks/sample.yml -i inventories/production/hosts -l hostname -C -D -b
```

Execute Mode

```bash
ansible-playbook playbooks/sample.yml -i inventories/production/hosts -l hostname -D -b
```