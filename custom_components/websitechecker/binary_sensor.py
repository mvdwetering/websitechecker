"""Platform for sensor integration."""

import logging
import voluptuous as vol
from datetime import timedelta
from urllib.parse import urlparse

import aiohttp

from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_PROBLEM,
    PLATFORM_SCHEMA,
    BinarySensorEntity,
)
from homeassistant.const import (
    CONF_URL,
    CONF_NAME
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, CONF_WEBSITES

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=10)


async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    entities = []
    websites = discovery_info.get(CONF_WEBSITES)
    websession = async_get_clientsession(hass)

    for website in websites:
        url = website.get(CONF_URL)
        name = website.get(CONF_NAME, urlparse(url).netloc)
        _LOGGER.debug(f"Adding url:{url}, name:{name}")
        entities.append(WebsitecheckerSensor(websession, url, name))
    add_entities(entities, True)


class WebsitecheckerSensor(BinarySensorEntity):
    """Representation of a Sensor."""

    def __init__(self, websession, url, name):
        """Initialize the sensor."""
        self._is_down = None
        self._url = url
        self._name = name
        self._websession = websession

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return the uniqueid of the entity."""
        return self._url

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self._is_down

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._is_down is not None

    @property
    def device_class(self):
        """Return the class of this device, from component DEVICE_CLASSES."""
        return DEVICE_CLASS_PROBLEM

    async def async_update(self):
        """Do a request to the website """
        try:
            async with self._websession.get(self._url) as resp:
                _LOGGER.debug(resp)
                self._is_down = resp.status >= 500
        except aiohttp.ClientConnectionError:
            self._is_down = True
