#coding: utf-8
from __future__ import unicode_literals, absolute_import

__all__ = ['split']


def split(vin):
    vin = vin.upper()
    return {
        'wmi': vin[0:3],
        'country': vin[0:2],
        'spc': vin[3:6],
        'wds': vin[3:9],
        'vis': vin[9:16],
        'checksum': vin[8],
        'year': vin[9],
    }
