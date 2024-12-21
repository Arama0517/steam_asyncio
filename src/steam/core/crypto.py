"""
All function in this module take and return :class:`bytes`
"""

from base64 import b64decode
from os import urandom
from struct import pack

from Cryptodome.Cipher import AES, PKCS1_OAEP, PKCS1_v1_5
from Cryptodome.Hash import HMAC, MD5, SHA1
from Cryptodome.PublicKey.RSA import construct, import_key


class UniverseKey:
    """Public keys for Universes"""

    Public = import_key(
        b64decode(
            'MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQDf7BrWLBBmLBc1OhSwfFkRf53T2Ct64+AVzRkeRuh7h3SiGEYxqQMUeYKO6UWiSRKpI2hzic9pobFhRr3Bvr/WARvYgdTckPv+T1JzZsuVcNfFjrocejN1oWI0Rrtgt4Bo+hOneoo3S57G9F1fOpn5nsQ66WOiu4gZKODnFMBCiQIBEQ=='
        )
    )


BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * pack('B', BS - len(s) % BS)


def unpad(s):
    return s[0 : -s[-1]]


def generate_session_key(hmac_secret=b''):
    """
    :param hmac_secret: optional HMAC
    :type hmac_secret: :class:`bytes`
    :return: (session_key, encrypted_session_key) tuple
    :rtype: :class:`tuple`
    """
    session_key = urandom(32)
    encrypted_session_key = PKCS1_OAEP.new(UniverseKey.Public, SHA1).encrypt(
        session_key + hmac_secret
    )

    return session_key, encrypted_session_key


def symmetric_encrypt(message, key):
    iv = urandom(BS)
    return symmetric_encrypt_with_iv(message, key, iv)


def symmetric_encrypt_ecb(message, key):
    return AES.new(key, AES.MODE_ECB).encrypt(pad(message))


def symmetric_encrypt_hmac(message, key, hmac_secret):
    prefix = urandom(3)
    hmac = hmac_sha1(hmac_secret, prefix + message)
    iv = hmac[:13] + prefix
    return symmetric_encrypt_with_iv(message, key, iv)


def symmetric_encrypt_iv(iv, key):
    return AES.new(key, AES.MODE_ECB).encrypt(iv)


def symmetric_encrypt_with_iv(message, key, iv):
    encrypted_iv = symmetric_encrypt_iv(iv, key)
    cyphertext = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(message))
    return encrypted_iv + cyphertext


def symmetric_decrypt(cyphertext, key):
    iv = symmetric_decrypt_iv(cyphertext, key)
    return symmetric_decrypt_with_iv(cyphertext, key, iv)


def symmetric_decrypt_ecb(cyphertext, key):
    return unpad(AES.new(key, AES.MODE_ECB).decrypt(cyphertext))


def symmetric_decrypt_hmac(cyphertext, key, hmac_secret):
    """:raises: :class:`RuntimeError` when HMAC verification fails"""
    iv = symmetric_decrypt_iv(cyphertext, key)
    message = symmetric_decrypt_with_iv(cyphertext, key, iv)

    hmac = hmac_sha1(hmac_secret, iv[-3:] + message)

    if iv[:13] != hmac[:13]:
        raise RuntimeError('Unable to decrypt message. HMAC does not match.')

    return message


def symmetric_decrypt_iv(cyphertext, key):
    return AES.new(key, AES.MODE_ECB).decrypt(cyphertext[:BS])


def symmetric_decrypt_with_iv(cyphertext, key, iv):
    return unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cyphertext[BS:]))


def hmac_sha1(secret, data):
    return HMAC.new(secret, data, SHA1).digest()


def sha1_hash(data):
    return SHA1.new(data).digest()


def md5_hash(data):
    return MD5.new(data).digest()


def rsa_publickey(mod, exp):
    return construct((mod, exp))


def pkcs1v15_encrypt(key, message):
    return PKCS1_v1_5.new(key).encrypt(message)
