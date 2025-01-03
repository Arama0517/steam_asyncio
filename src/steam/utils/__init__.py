"""Utility package with various useful functions"""

import socket
import struct
import weakref


def ip4_from_int(ip):
    """Convert :py:class:`int` to IPv4 string

    :param ip: int representing an IPv4
    :type ip: int
    :return: IP in dot-decimal notation
    :rtype: str
    """
    return socket.inet_ntoa(struct.pack('>L', ip))


def ip4_to_int(ip):
    """Convert IPv4 string to :py:class:`int`

    :param ip: IPv4 in dot-decimal notation
    :type ip: str
    :rtype: int
    """
    return struct.unpack('>L', socket.inet_aton(ip))[0]


ip_to_int = ip4_to_int
ip_from_int = ip4_from_int


def ip6_from_bytes(ip):
    """Convert :py:class:`bytes` to IPv6 string

    :param ip: IPv6 in dot-decimal notation
    :type ip: bytes
    :rtype: str
    """
    return socket.inet_ntop(socket.AF_INET6, ip)


def ip6_to_bytes(ip):
    """Convert IPv6 string to :py:class:`bytes`

    :param ip: IPv6 in dot-decimal notation
    :type ip: str
    :rtype: bytes
    """
    return socket.inet_pton(socket.AF_INET6, ip)


def chunks(arr, size):
    """Splits a list into chunks

    :param arr: list to split
    :type arr: :class:`list`
    :param size: number of elements in each chunk
    :type size: :class:`int`
    :return: generator object
    :rtype: :class:`generator`
    """
    for i in range(0, len(arr), size):
        yield arr[i : i + size]


class WeakRefKeyDict:
    """Pretends to be a dictionary.
    Use any object (even unhashable) as key and store a value.
    Once the object is garbage collected, the entry is destroyed automatically.
    """

    def __init__(self):
        self.refs = {}

    def __setitem__(self, obj, value):
        key = id(obj)

        if key not in self.refs:
            wr = weakref.ref(obj, WeakRefCallback(self.refs, key))
            self.refs[key] = [wr, None]
        self.refs[key][1] = value

    def __getitem__(self, obj):
        key = id(obj)
        return self.refs[key][1]

    def __contains__(self, obj):
        return id(obj) in self.refs

    def __len__(self):
        return len(self.refs)


class WeakRefCallback:
    def __init__(self, refs, key):
        self.__dict__.update(locals())

    def __call__(self, wr):
        del self.refs[self.key]
