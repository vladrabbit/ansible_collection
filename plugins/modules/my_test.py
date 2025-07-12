#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        original_content='',
        path='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path

    if os.path.exists(path):
        with open(path, 'r') as f:
            existing_content = f.read()
            result['original_content'] = existing_content
        if existing_content == content:
            module.exit_json(**result)
        else:
            if module.check_mode:
                result['changed'] = True
                module.exit_json(**result)
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
            module.exit_json(**result)
    else:
        if module.check_mode:
            result['changed'] = True
            module.exit_json(**result)
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
        module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
