#!/usr/bin/env bash

set -eux

ansible-playbook block_vars.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook import_tasks.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook include_role.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook include_tasks.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook include_vars.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook play_vars.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook register.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook roles-defaults.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook roles-vars.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook roles.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook set_fact.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook task_vars.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
ansible-playbook vars_files.yml "$@" 2>&1 | grep "The variable name 'True' is not valid."
