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
    print(resp.status_code)
    if resp.status_code != 200:
        LOGGER.info("[N2i] Upload failed")
        LOGGER.info(f"[N2i] URL: {n2i_url}")
        LOGGER.info(f"[N2i] Token: {n2i_token[:5]}...{n2i_token[-5:]}")
        LOGGER.info(f"[N2i] Image: {file}")

@pibooth.hookimpl
def pibooth_configure(cfg):
    cfg.add_option(SECTION, "n2i_url", "", "Pibooth Endpoint URL")
    cfg.add_option(SECTION, "n2i_token", "", "Pibooth Auth Token")

@pibooth.hookimpl
def pibooth_startup(app, cfg):
    n2i_url = cfg.get(SECTION, "n2i_url")
    n2i_token = cfg.get(SECTION, "n2i_token")

    if not n2i_url or len(n2i_url) < 5: #url shorther than http scheme length
        LOGGER.error(
            "[N2i] URL not defined in ["
            + SECTION
            + "][n2i_url], uploading deactivated"
        )
        app.n2i_configured = False
    elif not n2i_token or len(n2i_token) < 64:
        LOGGER.error(
            "[N2i] Token not defined in ["
            + SECTION
            + "][n2i_token], uploading deactivated"
        )
        app.n2i_configured = False
    else:
        LOGGER.info("[N2i] configured: True")
        app.n2i_configured = True
    

@pibooth.hookimpl
def state_processing_exit(app, cfg):
    print(app.n2i_configured)
    if app.n2i_configured:
        n2i_url = cfg.get(SECTION, "n2i_url")
        n2i_token = cfg.get(SECTION, "n2i_token")
        upload(app.previous_picture_file, n2i_url, n2i_token)