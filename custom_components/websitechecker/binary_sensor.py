"""Platform for sensor integration."""

from datetime import timedelta
from urllib.parse import urlparse

import aiohttp

from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_PROBLEM,
    BinarySensorEntity,
)
from homeassistant.const import CONF_URL, CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_UPDATE_INTERVAL, CONF_WEBSITES, LOGGER


SCAN_INTERVAL = timedelta(minutes=1)


async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    entities = []
    main_update_interval = discovery_info.get(CONF_UPDATE_INTERVAL)
    websites = discovery_info.get(CONF_WEBSITES)
    websession = async_get_clientsession(hass)

    for website in websites:
        url = website.get(CONF_URL)
        name = website.get(CONF_NAME, urlparse(url).netloc)
        update_interval = website.get(CONF_UPDATE_INTERVAL, main_update_interval)
        entities.append(WebsitecheckerSensor(websession, url, name, update_interval))
        LOGGER.debug(f"Added entity for url:{url}, name:{name}")
    add_entities(entities, True)


class WebsitecheckerSensor(BinarySensorEntity):
    """Representation of a Sensor."""

    def __init__(self, websession, url, name, update_interval):
        """Initialize the sensor."""
        self._is_down = None
        self._url = url
        self._name = name
        self._websession = websession
        self._update_interval = update_interval
        self._update_interval_remaining = 0  # Make sure to update at startup

        self._attr_extra_state_attributes = {'url': url}

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
        """Do a request to the website"""
        self._update_interval_remaining -= 1
        if self._update_interval_remaining <= 0:
            self._update_interval_remaining = self._update_interval
            try:
                LOGGER.debug("Start checking: %s", self._url)
                async with self._websession.get(self._url) as resp:
                    LOGGER.debug(
                        "Done checking: %s, status = %s", self._url, resp.status
                    )
                    self._is_down = resp.status >= 500
            except aiohttp.ClientConnectionError:
                LOGGER.debug("ConnectionError for %s", self._url)
                self._is_down = True
