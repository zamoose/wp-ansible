#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path=dict(required=True),
            state=dict(),
            plugin=dict(),
            theme=dict(),
            user=dict(),
            version=dict(),
            executable=dict(default=None),
        ),
        supports_check_mode=True
    )

    path = module.params['path']
    state = module.params['state']

    before = None
    after = None
    changed = False

    module.exit_json(changed=changed, before=before, after=after)
# import module snippets
from ansible.module_utils.basic import *
main()
