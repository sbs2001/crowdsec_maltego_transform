from maltego_trx.decorator_registry import TransformRegistry

registry = TransformRegistry(
    owner="CrowdSec",
    author="Shivam Sandbhor <shivam@crowdsec.net>",
    host_url="",
    seed_ids=["demo"],
)

# The rest of these attributes are optional

# metadata
registry.version = "0.1"

# global settings
# from maltego_trx.template_dir.settings import api_key_setting
# registry.global_settings = [api_key_setting, cache_ttl_setting]

# transform suffix to indicate datasource
# registry.display_name_suffix = " [ACME]"

# reference OAuth settings
# registry.oauth_settings_id = ['github-oauth']
