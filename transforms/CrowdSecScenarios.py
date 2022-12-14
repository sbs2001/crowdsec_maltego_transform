import pathlib

from maltego_trx.maltego import MaltegoMsg
from maltego_trx.transform import DiscoverableTransform

from extensions import registry
from transform_sets import CrowdSecSet
from settings import api_key_setting, cache_ttl_setting
from utils import enriched_ip_with_cti_resp, extract_cti_resp_from_ip_ent

ICON_PATH = (
    pathlib.Path(__file__).parent.resolve().parent.joinpath("assets/cs_color.png")
)


@registry.register_transform(
    display_name="CrowdSec scenarios",
    input_entity="maltego.IPv4Address",
    description="Creates entites for scenarios triggered by IP using CrowdSec CTI data.",
    settings=[api_key_setting, cache_ttl_setting],
    transform_set=CrowdSecSet,
)
class CrowdSecScenarios(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response):
        try:
            ip_ent = enriched_ip_with_cti_resp(request, response)
        except Exception as e:
            response.addUIMessage(str(e))
            return

        cti_resp = extract_cti_resp_from_ip_ent(ip_ent)
        for attack in cti_resp["attack_details"]:
            scenario = response.addEntity("crowdsec.scenario", attack["name"])
            scenario.setIconURL(f"file://{ICON_PATH}")
            scenario.addProperty("label", value=attack["label"])
            scenario.addDisplayInformation(
                "<h3>" + attack["description"] + "</h3>", "Description"
            )
