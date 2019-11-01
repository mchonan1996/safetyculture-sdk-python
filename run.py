import logging
import os

from dotenv import load_dotenv # get rid of if you don't want dotenv
from safetypy import *

load_dotenv() # get rid of if you don't want dotenv
logger = logging.getLogger('mc_logger')


def exit_with_error(logger, error):
    logger.error(error)
    sys.exit(1)

username = os.getenv('SC_USERNAME') # replace with username if you want
password = os.getenv('SC_PASSWORD') # replace with password if you want

token = get_user_api_token(logger, username, password)
print('Got token: %s' % token)

if token is None:
    exit_with_error(logger, 'Token retrieval failed')

sc = SafetyCulture(token)

# Grab my templates
res_templates = sc.discover_templates()
if res_templates is None:
    exit_with_error(logger, 'Template retrieval failed')

templates = res_templates['templates']
template_id = templates[0]['template_id']

# Grab groups (need groups to get users)
# res_groups = sc.get_my_org()
# print('groups %s' % res_groups)         NEED TO REWRITE THESE TO JUST LIST FREAKING GROUPS.


# auditor.create_audit(template_id)

# res_audits = sc.discover_audits(completed=False)
# if res_audits is None:
#     exit_with_error(logger, 'Audits retrieval failed')

# audits = res_audits['audits']
# audit_id = audits[0]['audit_id']

# audit = sc.get_audit(audit_id)
# if audit is None:
#     exit_with_error(logger, 'Audit retrieval failed')
