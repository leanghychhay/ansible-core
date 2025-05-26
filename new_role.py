import os
import sys
import logging

class RoleManager:
    """Manages roles in the system."""
    ROLE_SUBDIR = ["defaults", "files", "handlers", "meta", "tasks", "templates"]
    MAIN_YML_TEMPLATE = """---
# Main role file for {} role
"""
    README_TEMPLATE = """# README #

This Ansible role automates the configuration management for the '{}' role, ensuring that the system is set up correctly and efficiently.
"""
    PLAYBOOK_TEMPLATE = """---
- hosts:
    - all
  roles:
    - {}
"""
    def __init__(self, roles_dir="roles", playbooks_dir="playbooks"):
        self.roles_dir = roles_dir
        self.playbooks_dir = playbooks_dir
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def create_directory(self, path):
        try:
            os.makedirs(path, exist_ok=True)
            logging.info(f"Directory created: {path}")
        except Exception as e:
            logging.error(f"Failed to create directory {path}: {e}")
            sys.exit(1)

    def create_file(self, path, contents):
        try:
            with open(path, 'w') as file:
                file.write(contents)
            logging.info(f"Created file: {path}")
        except OSError as e:
            logging.error(f"Failed to create file {path}: {e}")
            sys.exit(1)

    def create_role(self, role_name):
        if not role_name:
            logging.error("Role name cannot be empty")
            sys.exit(1)

        role_path = os.path.join(self.roles_dir, role_name)
        if os.path.exists(role_path):
            logging.error(f"Role {role_name} already exists")
            sys.exit(1)

        self.create_directory(role_path)
        for subdir in self.ROLE_SUBDIR:
            subdir_path = os.path.join(role_path, subdir)
            self.create_directory(subdir_path)
            if subdir in ["tasks", "handlers", "defaults"]:
                self.create_file(os.path.join(subdir_path, "main.yml"), self.MAIN_YML_TEMPLATE.format(role_name))

        # Create a README.md for the role root
        self.create_file(os.path.join(role_path, "README.md"), self.README_TEMPLATE.format(role_name))

        self.create_directory(self.playbooks_dir)
        playbook_path = os.path.join(self.playbooks_dir, f"{role_name}.yaml")
        self.create_file(playbook_path, self.PLAYBOOK_TEMPLATE.format(role_name))

        logging.info(f"Role '{role_name}' and playbook '{playbook_path}' created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python new_role.py <role_name>")
        sys.exit(1)

    role_name = sys.argv[1]
    manager = RoleManager()
    manager.create_role(role_name)