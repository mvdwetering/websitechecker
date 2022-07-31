# Websitechecker

Custom integration that checks if a website is reachable or not.

A website is considered OK when an HTTP request returned with a response code < 500.
Or the other way around it is considered a problem if the HTTP request failed or returned a response code >= 500.


## Configuration examples

### Basic

```
websitechecker:
  websites:
    - url: https://example.com
      name: Optional friendly name
    - url: http://does_not_exist.com
    - url: http://192.168.178.4:9000  # URLs with port also work
      name: Portainer
```

### Custom update interval

```
websitechecker:
  update_interval: 10  # Optional, defaults to 10 minutes
  websites:
    - url: https://example.com
      name: Optional friendly name
    - url: http://does_not_exist.com
      update_interval: 5  # Optional, main `update_interval` used when not provided
```

## Installation

### HACS

Recommended as you get notifications of updates

* Add this repository https://github.com/mvdwetering/websitechecker to HACS as a "custom repository" with category "integration". This option can be found in the ⋮ menu
* Install the integration from within HACS
* Add a configuraton section to `configuration.yaml`
* Restart Home Assistant

### Manual

* Extract the Zip file in the `custom_components` directory
* Add a configuraton section to `configuration.yaml`
* Restart Home Assistant
