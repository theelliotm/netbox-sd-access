"""Top-level package for NetBox SD-Access Plugin."""

__author__ = """John Doe"""
__email__ = "john@example.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class SDAccessConfig(PluginConfig):
    name = "netbox_sd_access"
    verbose_name = "NetBox SD-Access Plugin"
    description = "NetBox plugin for SD-Access."
    version = "0.1.0"
    base_url = "sd-access"


config = SDAccessConfig
