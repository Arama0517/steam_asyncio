from binascii import hexlify

import requests

from steam.core.crypto import random_bytes, sha1_hash


def make_requests_session():
    """
    :returns: requests session
    :rtype: :class:`requests.Session`
    """
    session = requests.Session()

    version = __import__('steam').__version__
    ua = 'python-steam/{} {}'.format(version, session.headers['User-Agent'])
    session.headers['User-Agent'] = ua

    return session


def generate_session_id():
    """
    :returns: session id
    :rtype: :class:`str`
    """
    return hexlify(sha1_hash(random_bytes(32)))[:32].decode('ascii')
