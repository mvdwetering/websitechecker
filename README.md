# Websitechecker

Custom integration that checks if a website is reachable or not.

A website is considered OK when an HTTP request returned with a response code < 500.
Or the other way around it is considered a problem if the HTTP request failed or returned a response code >= 500.

The sensor offers the following additional attributes:

* url: The configured URL for this sensor
* last_status: Status of last update. Some possible values are "200 - OK" or "Connection error". More error values exist.
* last_error_status: Status of last error, allows to easily see what the last issue was if it came back already.

## Configuration examples

### Basic

```
websitechecker:
  websites:
    - url: https://example.com
      name: Optional friendly name
    - url: http://does_not_exist.com
    - url: http://192.168.178.4:9000  # URLs with non-standard ports also work
```

### Advanced

```
websitechecker:
  update_interval: 10  # Optional, value in minutes, defaults to 10
  websites:
    - url: https://example.com
      name: Optional friendly name
      verify_ssl: false  # Optional, default is true
    - url: http://does_not_exist.com
      update_interval: 5  # Optional, main `update_interval` used when not provided
```

## Notificatons

Because the integration exposes normal sensors you can use Automations to get notified of issues. These type of automations are not specific for this integrations, so you can build automations as usual. 

Below are some links to related Home Assistant documentation.

* [Automating Home Assistant](https://www.home-assistant.io/docs/automation/)
* [Home Assistant Mobile App notifications](https://companion.home-assistant.io/docs/notifications/notifications-basic)
* [Notification Blueprints on Home Assistant forums](https://community.home-assistant.io/search?q=notifications%20%23blueprints-exchange)
* [Home Assistant Core integrations that support notifications](https://www.home-assistant.io/integrations/#notifications)

When you have questions for automations or looking for examples ask/search on one of the Home Assistant Community channels like [Forum](https://community.home-assistant.io/), [Discord](https://www.home-assistant.io/join-chat) or [Reddit](https://reddit.com/r/homeassistant).

## Installation

### Home Assistant Community Store (HACS)

*Recommended as you get notifications of updates*

HACS is a 3rd party downloader for Home Assistant to easily install and update custom integrations made by the community. More information and installation instructions can be found on their site https://hacs.xyz/

* Add this repository https://github.com/mvdwetering/websitechecker to HACS as a "custom repository" with category "integration". This option can be found in the ⋮ menu
* Install the integration from within HACS
* Add a configuraton section to `configuration.yaml`
* Restart Home Assistant

### Manual

* Extract the Zip file in the `custom_components` directory
* Add a configuraton section to `configuration.yaml`
* Restart Home Assistant
