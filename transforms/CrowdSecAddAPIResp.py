from maltego_trx.maltego import MaltegoMsg
from maltego_trx.transform import DiscoverableTransform

from extensions import registry
from settings import api_key_setting
from transforms.utils import clone_ip_entity, enriched_ip_with_cti_resp


@registry.register_transform(
    display_name="CrowdSec IP CTI",
    input_entity="maltego.IPv4Address",
    description="Attaches CrowdSec CTI API response to IP entity",
    settings=[api_key_setting],
)
class CrowdSecAddAPIResp(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response):
        try:
            enriched_ip_with_cti_resp(request, response)
        except Exception as e:
            response.addUIMessage(str(e))
