import base64
import requests
from requests.auth import HTTPBasicAuth
from sharepoint import SharePointSite, basic_auth_opener

#Version Basic
server_url = "https://axiomesolution.sharepoint.com/"
site_url = server_url + "sites/IUTTeam/SitePages/Test-Site-pour-Bot.aspx"

USERNAME = "collaborateur Externe"

PASSWORD = "partenR@xiome"

#from sharepoint import SharePointSite, basic_auth_opener
#opener = basic_auth_opener(server_url, USERNAME, PASSWORD)

#site = SharePointSite(site_url, opener)


#print (site.lists)

response = requests.get("http://172.28.1.98", auth=HTTPBasicAuth("loca\maxime", PASSWORD))

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
