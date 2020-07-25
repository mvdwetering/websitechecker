# Websitechecker

Custom integration that checks if a website is reachable or not.

## Installation

* Add `websitechecker:` to `configuration.yaml` and add some URLs to check
* Restart Home Assistant.

## Example configuration

```
websitechecker:
  websites:
    - url: https://google.com
      name: Optional friendly name
    - url: http://does_not_exist.com
```
