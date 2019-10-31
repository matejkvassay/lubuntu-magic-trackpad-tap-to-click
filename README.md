# Description

This script enables tap-to-click option for Apple Magic Trackpad 1 connected
to Lubuntu desktop via Bluetooth BlueDevil Wizard.

It uses ```xinput``` command as described in one of the solutions here:
```
https://askubuntu.com/questions/1087328/lubuntu-18-10-how-to-activate-tap-to-click
```

# Requirements
Tested on Lubuntu 19.1 eoan.
```
- Python 3.7.4
- Distributor ID: Ubuntu
  Description:    Ubuntu 19.10
  Release:        19.10
  Codename:       eoan
```

# Usage
Clone and run the script after connecting the Trackpad.

Alias for ```~/.bashrc```:
```
export TAP_TO_CLICK_SCRIPT="<PROJECT FOLDER>/lubuntu-magic-trackpad-tap-to-click/enable_tap_to_click.py"
alias tap_tc='python $TAP_TO_CLICK_SCRIPT'

```
