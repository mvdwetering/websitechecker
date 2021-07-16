# Websitechecker

Custom integration that checks if a website is reachable or not. Currently the check is done every 10 minutes.

A website is considered OK when an HTTP request returned with a response code < 500.
Or the other way around it is considered a problem if the HTTP request failed or returned a response code >= 500.

## Installation

### HACS

* Add this repository https://github.com/mvdwetering/websitechecker to HACS as a "custom repository" with category "integration". This option can be found in the ⋮ menu
* Install the integration from within HACS

### Common

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
