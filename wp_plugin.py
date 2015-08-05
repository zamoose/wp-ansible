#!/usr/bin/python
# -*- coding: utf-8 -*-

def plugin_install(wp_bin,module,path,slug,version):
    cmd = "%s plugin install %s" % (wp_bin,slug)
    (rc, out, err) = module.run_command(cmd, check_rc=True,cwd=path)

    print out
    
    if rc != 0:
        module.fail_json(msg="Couldn't install plugin: %s" % (err,))

    return (rc, out, err)


def main():
    module = AnsibleModule(
        argument_spec = dict(
            path=dict(required=True),
            name=dict(),
            state=dict(),
            version=dict(),
            executable=dict(default=None),
        ),
        supports_check_mode=True
    )

    path = module.params['path']
    state = module.params['state']
    plugin = module.params['name']
    version = module.params['version']
    wp_path = module.params['executable'] or module.get_bin_path('wp', True)

    before = None
    after = None
    changed = False

    plugin_install(wp_path,module,path,plugin,version)

    module.exit_json(changed=changed, before=before, after=after)
# import module snippets
from ansible.module_utils.basic import *
main()
