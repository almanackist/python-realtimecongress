"""
Python library for interacting with the Real Time Congress API.
"""

__author__ = "Dan Drinkard <ddrinkard@sunlightfoundation.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2011 Sunlight Labs"
__license__ = "BSD"

import requests
import simplejson as json

from urllib import urlencode

class RTCResponse(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__dict__)

class RTCError(Exception):
    """ Exception for API errors"""

class RTC(object):
    apikey = None
    version = 1
    format = 'json'
    baseurl = "http://api.realtimecongress.org/api/v{version}/{method}.{format}?{params}"

    meta = {}

    @staticmethod
    def _call(method, **params):
        if RTC.apikey is None:
            raise RTCError('Missing Sunlight apikey. Get one at services.sunlightlabs.com')

        context = {
            'version': RTC.version,
            'format': RTC.format,
            'method': method,
            'params': urlencode(params)
        }

        with requests.session(headers={'X-APIKEY':RTC.apikey}) as connection:
            rsp = connection.get(RTC.baseurl.format(**context))
            rsp.raise_for_status()

            if rsp.status_code == requests.codes.ok:
                responsejson = json.loads(rsp.content)
                try:
                    content = responsejson[method]

                    RTC.meta['page'] = responsejson['page']
                    RTC.meta['count'] = responsejson['count']
                    return [RTCResponse(**bill) for bill in content]

                except Exception as e:
                    raise RTCError('got %s: %s' % e.__class__.__name__, e)

    @staticmethod
    def getBills(**params):
        return RTC._call('bills', **params)

    @staticmethod
    def getVotes(**params):
        return RTC._call('votes', **params)

    @staticmethod
    def getAmendments(**params):
        return RTC._call('amendments', **params)

    @staticmethod
    def getVideos(**params):
        return RTC._call('videos', **params)

    @staticmethod
    def getFloorUpdates(**params):
        return RTC._call('floor_updates', **params)

    @staticmethod
    def getCommitteeHearings(**params):
        return RTC._call('committee_hearings', **params)

    @staticmethod
    def getDocuments(**params):
        return RTC._call('documents', **params)