import base64
import requests
from requests.auth import HTTPBasicAuth
from sharepoint import SharePointSite, basic_auth_opener

#Version Basic
site_url = "http://172.28.1.98"

USERNAME = "loca\maxime"

PASSWORD =  base64.b64decode("c3VyZnJpZGVyNzQxMjU4OTYz")

from sharepoint import SharePointSite, basic_auth_opener
opener = basic_auth_opener(site_url, USERNAME, PASSWORD)

site = SharePointSite(site_url, opener)

for sp_list in site.lists:
  print (sp_list.id, sp_list.meta['TITLE'])

response = requests.get(site_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

print (response.status_code)




"""     Version Ntlm

import requests
from requests_ntlm import HttpNtlmAuth

USERNAME = "collaborateur Externe"

PASSWORD = "partenR@xiome"

response = requests.get("https://axiomesolution.sharepoint.com/sites/IUTTeam/SitePages/Test-Site-pour-Bot.aspx", auth=HttpNtlmAuth(USERNAME, PASSWORD))

print (response.status_code)
"""



"""  Test pour plus tard

from sharepoint import SharePointSite, basic_auth_opener
opener = basic_auth_opener(server_url, USERNAME, PASSWORD)

site = SharePointSite(site_url, opener)

for sp_list in site.lists:
   print (sp_list.id, sp_list.meta['Title'])
"""