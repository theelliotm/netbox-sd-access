from typing import Annotated, List, Optional
import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType
from .. import models
from . import filters

@strawberry_django.type(
    models.IPPool,
    fields='__all__',
    filters=filters.IPPoolFilter
)
class IPPoolType(NetBoxObjectType):
    """
    Defines GraphQL type for IP Pools.
    """
    id: int
    name: str
    prefix: Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]
    gateway: Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]
    dhcp_server: Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]
    dns_servers: List[Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]]
    
    
@strawberry_django.type(
    models.FabricSite,
    fields='__all__',
    filters=filters.FabricSiteFilter
)
class FabricSiteType(NetBoxObjectType):
    """
    Defines GraphQL type for Fabric Sites.
    """
    id: int
    name: str
    physical_site: Annotated["SiteType", strawberry.lazy('dcim.graphql.types')]
    location: Optional[Annotated["LocationType", strawberry.lazy('dcim.graphql.types')]]
    ip_prefixes: List[IPPoolType]
    comments: str
    
    
@strawberry_django.type(
    models.IPTransit,
    fields='__all__',
    filters=filters.IPTransitFilter
)
class IPTransitType(NetBoxObjectType):
    """
    Defines GraphQL type for IP Transits.
    """
    id:int
    name:str
    fabric_site:FabricSiteType
    asn: Annotated["ASNType", strawberry.lazy('ipam.graphql.types')]
    comments:str
    

@strawberry_django.type(
    models.SDADevice,
    fields='__all__',
    filters=filters.SDADeviceFilter
)
class SDADeviceType(NetBoxObjectType):
    """
    Defines GraphQL type for SDA Devices.
    """
    id: int
    device: Annotated["DeviceType", strawberry.lazy('dcim.graphql.types')]
    fabric_site: FabricSiteType
    role: str
    
    
@strawberry_django.type(
    models.SDATransit,
    fields='__all__',
    filters=filters.SDATransitFilter
)
class SDATransitType(NetBoxObjectType):
    """
    Defines GraphQL type for SDA Transits.
    """
    id:int
    name:str
    transit_type:str
    fabric_site:FabricSiteType
    control_plane_node:SDADeviceType
    devices:List[SDADeviceType]
    comments:str
    
    
@strawberry_django.type(
    models.VirtualNetwork,
    fields='__all__',
    filters=filters.VirtualNetworkFilter
)
class VirtualNetworkType(NetBoxObjectType):
    """
    Defines GraphQL type for Virtual Networks.
    """
    id: int
    name: str
    fabric_site: List[FabricSiteType]
    vrf: Annotated["VRFType", strawberry.lazy('ipam.graphql.types')]
