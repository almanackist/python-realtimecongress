Real Time Congress
==================

A python library for interacting with the Real Time Congress API.

Usage:
------
Fetching entities from a string of text:

    >>>from realtimecongress import RTC
    >>>RTC.apikey = 'mykey'
    >>>RTC.getBills(cosponsor_ids='L000287')
    [RTCResponse(...),]
    >>>RTC.meta
    {'count': 838, 'page': {'count': 20, 'per_page': 20, 'page': 1}}
