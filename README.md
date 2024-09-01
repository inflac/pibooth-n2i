pibooth-n2i
=================

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads)
[![PyPi package](https://badge.fury.io/py/pibooth-n2i.svg)](https://pypi.org/project/pibooth-n2i)
[![PyPi downloads](https://img.shields.io/pypi/dm/pibooth-n2i?color=purple)](https://pypi.org/project/pibooth-n2i)

`pibooth-n2i` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application.
It allows to upload captures to a cms running the pibooth extension

Install
-------

### Install from PyPI
    $ pip3 install pibooth-n2i

### Install for development
    git clone https://github.com/inflac/pibooth-n2i.git
    $ cd pibooth-n2i
    $ pip3 install -e .

Configuration
-------------

Below are the new configuration options available in the [pibooth](https://pypi.org/project/pibooth) configuration. **The keys and their default values are automatically added to your configuration after first** [pibooth](https://pypi.org/project/pibooth) **restart.**

``` {.ini}
[N2i]

# Pibooth Endpoint URL
n2i_url =

# Pibooth Auth Token
n2i_token =
```

### Note

Edit the configuration by running the command `pibooth --config`.


N2i pibooth extension 
-------------

In order to get the configuration values for pibooth you need to have a running instance of the [N2i CMS](https://github.com/HackerspaceBielefeld/Nextride2-infobeamer) with the pibooth extension enabled. You don't need to have [Nextride2](https://github.com/HackerspaceBielefeld/Nextride2) running in order to use a N2i CMS or this plugin for the N2i CMS.
1. Enter the N2i CMS as an admin user
2. Navigate to: Extensions->pibooth[manage]
3. Use the shown Pibooth Endpoint URL for the `n2i_url` configuration variable.
4. Use the shown token for the `n2i_token` configuration variable.

