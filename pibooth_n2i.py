"""Plugin to upload pictures on a Nextride2-infobeamer instance.""" 

import os
import requests as re

import pibooth
from pibooth.utils import LOGGER

__version__ = "0.0.1"

SECTION = "N2i"

def upload(file:str, n2i_url:str, n2i_token:str):
    headers = {'token': n2i_token}
    file_param = {'file': open(file, 'rb')}

    resp = re.post(n2i_url, files=file_param, headers=headers)
    if resp.status_code != 200:
        LOGGER.info("[N2i] Upload failed")
    print(f"N2i URL: {n2i_url}")
    print(f"N2i token: {n2i_token}")
    print(f"Image: {file}")

@pibooth.hookimpl
def pibooth_startup(app, cfg):
    cfg.add_option(SECTION, "n2i_url", "", "Pibooth Endpoint URL")
    cfg.add_option(SECTION, "n2i_token", "", "Pibooth Auth Token")

@pibooth.hookimpl
def state_processing_exit(app, cfg):
    n2i_url = cfg.get(SECTION, "n2i_url")
    n2i_token = cfg.get(SECTION, "n2i_token") 
    
    if n2i_url == "" and n2i_token == "":
        LOGGER.error("[N2i] No url or Token specified in config!")
    upload(app.previous_picture_file, n2i_url, n2i_token)