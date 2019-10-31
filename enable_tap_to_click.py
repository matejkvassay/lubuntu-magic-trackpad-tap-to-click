
# %% func def
import subprocess
import re

"""
This script enables tap-to-click option on Lubuntu on Magic Tracpad connected by
BlueDevil Wizard.

Solution from:
https://askubuntu.com/questions/1087328/lubuntu-18-10-how-to-activate-tap-to-click
"""

def execute(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf8')

def get_trackpad_device_id():
    lines=execute('xinput list').split('\n')
    trackpad_line=[x for x in lines if 'Trackpad' in x][0]
    device_id=int(re.search('id=(\d+)',trackpad_line).group(1))
    return device_id

def get_tapping_enabled_prop_id(device_id):
    list_props_cmd='xinput list-props {}'
    props=execute(list_props_cmd.format(device_id))
    tapping_enabled_line=[x for x in props.split('\n') if 'Tapping Enabled (' in x][0]
    tapping_enabled_line
    prop_id=int(re.search('\((\d+)',tapping_enabled_line).group(1))
    return prop_id

def enable_tap_to_click(device_id, property_id):
    cmd_enable_tap_to_click='xinput set-prop {} {} 1'
    execute(cmd_enable_tap_to_click.format(device_id, property_id))


# %% run

if __name__=='__main__':
    try:
        device_id=get_trackpad_device_id()
        prop_id=get_tapping_enabled_prop_id(device_id)
        enable_tap_to_click(device_id, prop_id)
        print('Successfully enabled')
    except Exception as ex:
        print('Failed with exception: {}'.format(ex))
