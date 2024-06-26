"""The Websitechecker integration."""

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_URL, CONF_NAME
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import async_load_platform

from .const import (
    DOMAIN,
    CONF_UPDATE_INTERVAL,
    CONF_WEBSITES,
    CONF_VERIFY_SSL,
)

_WEBSITES_SCHEMA = vol.All(
    cv.ensure_list,
    [
        vol.Schema(
            {
                vol.Required(CONF_URL): vol.Url(),
                vol.Optional(CONF_NAME): cv.string,
                vol.Optional(CONF_UPDATE_INTERVAL): cv.positive_int,
                vol.Optional(CONF_VERIFY_SSL, default=True): cv.boolean,
            }
        )
    ],
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_WEBSITES): _WEBSITES_SCHEMA,
                vol.Optional(CONF_UPDATE_INTERVAL, default=10): cv.positive_int,
            },
        ),
    },
    extra=vol.ALLOW_EXTRA,
)

PLATFORMS = ["binary_sensor"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Websitechecker integration."""
    for component in PLATFORMS:
        hass.async_create_task(
            async_load_platform(hass, component, DOMAIN, config.get(DOMAIN), config)
        )
    return True
