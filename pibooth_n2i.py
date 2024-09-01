"""Plugin to upload pictures on a Nextride2-infobeamer instance.""" 

import os
import asyncio
import requests as re

import pibooth
from pibooth.utils import LOGGER

__version__ = "0.0.1"

SECTION = "N2i"

async def upload(file, n2i_url:str, n2i_token:str):
    print(f"N2i URL: {n2i_url}")
    print(f"N2i token: {n2i_token}")
    print("Image: ", end="\r")
    print(file)

@pibooth.hookimpl 
def pibooth_startup(app, cfg):
    cfg.add_option(SECTION, "n2i_url", "", "Pibooth Endpoint URL")
    cfg.add_option(SECTION, "n2i_token", "", "Pibooth Auth Token")

@pibooth.hookimpl
async def state_processing_exit(app, cfg):
    n2i_url = cfg.get(SECTION, "n2i_url")
    n2i_token = cfg.get(SECTION, "n2i_token") 
    
    if n2i_url != "" and n2i_token != "":
        LOGGER.error("No url or Token specified in config!")
    await upload(open(app.previous_picture_file, 'rb'), n2i_url, n2i_token)