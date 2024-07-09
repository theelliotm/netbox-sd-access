import strawberry
import strawberry_django
from .. import filtersets, models
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

__all__ = (
    'FabricSiteFilter'
)

@strawberry_django.filter(models.FabricSite, lookups=True)
@autotype_decorator(filtersets.FabricSiteFilterSet)
class FabricSiteFilter(BaseFilterMixin):
    pass