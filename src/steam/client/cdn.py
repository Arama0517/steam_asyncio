"""
The :class:`.CDNClient` class provides a simple API for downloading Steam content from SteamPipe

Initializing :class:`.CDNClient` requires a logged in :class:`.SteamClient` instance

.. warning::
    This module uses :mod:`requests` library, which is not gevent cooperative by default.
    It is high recommended that you use :meth:`steam.monkey.patch_minimal()`.
    See example below

.. code:: python
    import steam.monkey
    steam.monkey.patch_minimal()

    from steam.client import SteamClient, EMsg
    from steam.client.cdn import CDNClient

    mysteam = SteamClient()
    mysteam.cli_login()
    ...
    mycdn = CDNClient(mysteam)


Getting depot manifests for an app

.. code:: python

    >>> mycdn.get_manifests(570)
    [<CDNDepotManifest('Dota 2 Content', app_id=570, depot_id=373301, gid=6397590570861788404, creation_time='2019-06-29 16:03:11')>,
     <CDNDepotManifest('Dota 2 Content 2', app_id=570, depot_id=381451, gid=5769691971272474272, creation_time='2019-06-29 00:19:02')>,
     <CDNDepotManifest('Dota 2 Content 3', app_id=570, depot_id=381452, gid=3194393866044592918, creation_time='2019-06-27 00:05:38')>,
     <CDNDepotManifest('Dota 2 Content 4', app_id=570, depot_id=381453, gid=8005824150061180163, creation_time='2019-06-08 07:49:57')>,
     <CDNDepotManifest('Dota 2 Content 5', app_id=570, depot_id=381454, gid=9003299908441378336, creation_time='2019-06-26 18:56:19')>,
     <CDNDepotManifest('Dota 2 Content 6', app_id=570, depot_id=381455, gid=8000458746487720619, creation_time='2019-06-29 00:19:43')>,
     <CDNDepotManifest('Dota 2 Win32', app_id=570, depot_id=373302, gid=3561463682334619841, creation_time='2019-06-29 00:16:28')>,
     <CDNDepotManifest('Dota 2 Win64', app_id=570, depot_id=373303, gid=6464064782313084040, creation_time='2019-06-29 00:16:43')>,
     <CDNDepotManifest('Dota 2 Mac', app_id=570, depot_id=373304, gid=5979018571482579541, creation_time='2019-06-29 00:16:59')>,
     <CDNDepotManifest('Dota 2 English', app_id=570, depot_id=373305, gid=4435851250675935801, creation_time='2015-06-01 20:15:37')>,
     <CDNDepotManifest('Dota 2 Linux', app_id=570, depot_id=373306, gid=4859464855297921815, creation_time='2019-06-29 00:17:25')>,
     <CDNDepotManifest('Dota 2 Korean', app_id=570, depot_id=373308, gid=8598853793233320583, creation_time='2019-03-05 17:16:49')>,
     <CDNDepotManifest('Dota 2 Simplified Chinese', app_id=570, depot_id=373309, gid=6975893321745168138, creation_time='2019-06-25 21:40:37')>,
     <CDNDepotManifest('Dota 2 Russian', app_id=570, depot_id=381456, gid=5425063725991897591, creation_time='2019-03-05 17:19:53')>,
     <CDNDepotManifest('Dota 2 Workshop tools', app_id=570, depot_id=381450, gid=8629205096668418087, creation_time='2019-06-29 16:04:18')>,
     <CDNDepotManifest('Dota 2 OpenGL Windows', app_id=570, depot_id=401531, gid=6502316736107281444, creation_time='2019-06-07 19:04:08')>,
     <CDNDepotManifest('Dota 2 Vulkan Common', app_id=570, depot_id=401535, gid=6405492872419215600, creation_time='2019-06-07 19:04:11')>,
     <CDNDepotManifest('Dota 2 Vulkan Win64', app_id=570, depot_id=401536, gid=3821288251412129608, creation_time='2019-06-25 21:42:29')>,
     <CDNDepotManifest('Dota 2 Vulkan Linux64', app_id=570, depot_id=401537, gid=3144805829218032316, creation_time='2019-06-17 16:54:43')>,
     <CDNDepotManifest('Dota 2 VR', app_id=570, depot_id=313255, gid=706332602567268673, creation_time='2017-10-04 18:52:14')>,
     <CDNDepotManifest('Dota 2 Vulkan Mac', app_id=570, depot_id=401538, gid=2223235822414824351, creation_time='2019-06-11 19:37:19')>]

    >>> mycdn.get_manifests(
    ...     570, filter_func=lambda depot_id, info: 'Dota 2 Content' in info['name']
    ... )
    [<CDNDepotManifest('Dota 2 Content', app_id=570, depot_id=373301, gid=6397590570861788404, creation_time='2019-06-29 16:03:11')>,
     <CDNDepotManifest('Dota 2 Content 2', app_id=570, depot_id=381451, gid=5769691971272474272, creation_time='2019-06-29 00:19:02')>,
     <CDNDepotManifest('Dota 2 Content 3', app_id=570, depot_id=381452, gid=3194393866044592918, creation_time='2019-06-27 00:05:38')>,
     <CDNDepotManifest('Dota 2 Content 4', app_id=570, depot_id=381453, gid=8005824150061180163, creation_time='2019-06-08 07:49:57')>,
     <CDNDepotManifest('Dota 2 Content 5', app_id=570, depot_id=381454, gid=9003299908441378336, creation_time='2019-06-26 18:56:19')>,
     <CDNDepotManifest('Dota 2 Content 6', app_id=570, depot_id=381455, gid=8000458746487720619, creation_time='2019-06-29 00:19:43')>]


Listing files

.. code:: python

    >>> file_list = mycdn.iter_files(570)
    >>> list(file_list)[:10]
    [<CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\dungeon\\particles\\test_particle\\generic_attack_crit_blur_rope.vpcf_c', 2134)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\dungeon\\materials\\blends\\mud_brick_normal_psd_5cc4fe8b.vtex_c', 351444)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\hero_demo\\scripts\\vscripts\\la_spawn_enemy_at_target.lua', 1230)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\winter_2018\\particles\\dark_moon\\darkmoon_last_hit_effect_damage_flash_b.vpcf_c', 1386)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\dungeon\\scripts\\vscripts\\abilities\\siltbreaker_line_wave.lua', 3305)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\dungeon\\materials\\models\\heroes\\broodmother\\broodmother_body_poison.vmat_c', 10888)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota\\resource\\cursor\\workshop\\sltv_shaker_cursor_pack\\cursor_spell_default.ani', 4362)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\overthrow\\panorama\\images\\custom_game\\team_icons\\team_icon_tiger_01_png.vtex_c', 18340)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota\\resource\\cursor\\valve\\ti7\\cursor_attack_illegal.bmp', 4152)>,
     <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota_addons\\winter_2018\\models\\creeps\\ice_biome\\undeadtusk\\undead_tuskskeleton01.vmdl_c', 13516)>

Reading a file directly from SteamPipe

.. code:: python

    >>> file_list = mycdn.iter_files(570, r'game\\dota\\gameinfo.gi')
    >>> myfile = next(file_list)
    <CDNDepotFile(570, 373301, 6397590570861788404, 'game\\dota\\gameinfo.gi', 6808)>
    >>> print(myfile.read(80).decode('utf-8'))
    "GameInfo"
    {
            game            "Dota 2"
            title           "Dota 2"

            gamelogo 1
            type            multiplayer_only
    ...

"""

import asyncio
import logging
import lzma
import os
import struct
from base64 import b64decode
from binascii import crc32, unhexlify
from collections import OrderedDict, deque
from datetime import UTC, datetime
from fnmatch import fnmatch
from io import BytesIO
from struct import pack
from typing import AsyncGenerator, Callable, Generator, Optional, Self
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile

import vdf
from aiohttp import ClientResponse
from cachetools import LRUCache

from steam import webapi
from steam.client import SteamClient
from steam.core.crypto import symmetric_decrypt, symmetric_decrypt_ecb
from steam.core.msg import MsgProto
from steam.enums import EDepotFileFlag, EResult, EType
from steam.enums.emsg import EMsg
from steam.exceptions import ManifestError, SteamError
from steam.protobufs.content_manifest_pb2 import (
    ContentManifestMetadata,
    ContentManifestPayload,
    ContentManifestSignature,
)
from steam.protobufs.steammessages_publishedfile_pb2 import (
    PublishedFileDetails,
)
from steam.utils.binary import StructReader
from steam.utils.web import AioHttpClientSessionWithUA


def decrypt_manifest_gid_2(encrypted_gid: bytes, password: bytes) -> int:
    """Decrypt manifest gid v2 bytes

    :param encrypted_gid: encrypted gid v2 bytes
    :param password: encryption password
    :return: manifest gid
    """
    return struct.unpack('<Q', symmetric_decrypt_ecb(encrypted_gid, password))[0]


async def get_content_servers_from_cs(
    cell_id: bytes,
    host: str = 'cs.steamcontent.com',
    port: int = 80,
    num_servers: int = 20,
) -> list['ContentServer']:
    """Get a list of CS servers from a single CS server

    :param cell_id: location cell id
    :param host: CS server host
    :param port: server port number
    :param num_servers: number of servers to return
    :return: list of CS servers
    """
    proto = 'https' if port == 443 else 'http'

    # session = make_requests_session() if session is None else session
    # resp = session.get(url)
    async with AioHttpClientSessionWithUA() as session:
        async with session.get(
            f'{proto}://{host}:{port}/serverlist/{cell_id}/{num_servers}/'
        ) as resp:
            if resp.status != 200:
                return []

            kv = vdf.loads(await resp.text(), mapper=OrderedDict)

            if kv.get('deferred') == '1':
                return []

            servers = []

            for entry in kv['serverlist'].values():
                server = ContentServer()
                server.type = entry['type']
                server.https = True if entry['https_support'] == 'mandatory' else False
                server.host = entry['Host']
                server.vhost = entry['vhost']
                server.port = 443 if server.https else 80
                server.cell_id = entry['cell']
                server.load = entry['load']
                server.weighted_load = entry['weightedload']
                servers.append(server)

            return servers


async def get_content_servers_from_webapi(
    cell_id: bytes, num_servers: int = 20
) -> list['ContentServer']:
    """Get a list of CS servers from Steam WebAPI

    :param cell_id: location cell id
    :param num_servers: number of servers to return
    :return: list of CS servers
    """
    params = {'cell_id': cell_id, 'max_servers': num_servers}
    resp: dict = await webapi.get(
        'IContentServerDirectoryService', 'GetServersForSteamPipe', params=params
    )

    servers = []

    for entry in resp['response']['servers']:
        server = ContentServer()
        server.type = entry['type']
        server.https = True if entry['https_support'] == 'mandatory' else False
        server.host = entry['host']
        server.vhost = entry['vhost']
        server.port = 443 if server.https else 80
        server.cell_id = entry.get('cell_id', 0)
        server.load = entry['load']
        server.weighted_load = entry['weighted_load']
        servers.append(server)

    return servers


class ContentServer:
    https = False
    host = None
    vhost = None
    port = None
    type = None
    cell_id = 0
    load = None
    weighted_load = None

    def __repr__(self):
        return "<{}('{}://{}:{}', type={}, cell_id={})>".format(
            self.__class__.__name__,
            'https' if self.https else 'http',
            self.host,
            self.port,
            repr(self.type),
            repr(self.cell_id),
        )


class CDNDepotFile:
    def __init__(
        self,
        manifest: 'CDNDepotManifest',
        file_mapping: ContentManifestPayload.FileMapping,
    ):
        """File-like object proxy for content files located on SteamPipe

        :param manifest: parrent manifest instance
        :param file_mapping: file mapping instance from manifest
        """
        if not isinstance(manifest, CDNDepotManifest):
            raise TypeError("Expected 'manifest' to be of type CDNDepotFile")
        if not isinstance(file_mapping, ContentManifestPayload.FileMapping):
            raise TypeError(
                "Expected 'file_mapping' to be of type ContentManifestPayload.FileMapping"
            )

        self.manifest = manifest
        self.file_mapping = file_mapping
        self.offset = 0
        self._lc = None
        self._lcbuff = b''

    def __repr__(self):
        return '<{}({}, {}, {}, {}, {})>'.format(
            self.__class__.__name__,
            self.manifest.app_id,
            self.manifest.depot_id,
            self.manifest.gid,
            repr(self.filename_raw),
            'is_directory=True' if self.is_directory else self.size,
        )

    @property
    def filename_raw(self) -> str:
        """Filename with null terminator and whitespaces removed"""
        return self.file_mapping.filename.rstrip('\x00 \n\t')

    @property
    def filename(self) -> str:
        """Filename matching the OS"""
        return os.path.join(*self.filename_raw.split('\\'))

    @property
    def linktarget_raw(self) -> str:
        """Link target with null terminator and whitespaces removed"""
        return self.file_mapping.linktarget.rstrip('\x00 \n\t')

    @property
    def linktarget(self) -> str:
        """Link target matching the OS"""
        return os.path.join(*self.linktarget_raw.split('\\'))

    @property
    def sha_content(self) -> bytes:
        """File content SHA1"""
        return self.file_mapping.sha_content

    @property
    def sha_filename(self) -> bytes:
        """Filename SHA1"""
        return self.file_mapping.sha_filename

    @property
    def size(self) -> int:
        """File size in bytes"""
        return self.file_mapping.size

    @property
    def chunks(self) -> list[ContentManifestPayload.FileMapping.ChunkData]:
        """File chunks instances"""
        return list(self.file_mapping.chunks)

    @property
    def flags(self) -> EDepotFileFlag:
        """File flags"""
        return EDepotFileFlag(self.file_mapping.flags)

    @property
    def is_directory(self) -> bool:
        return self.flags & EDepotFileFlag.Directory > 0

    @property
    def is_symlink(self) -> bool:
        return not not self.file_mapping.linktarget

    @property
    def is_file(self) -> bool:
        return not self.is_directory and not self.is_symlink

    @property
    def is_executable(self) -> bool:
        return self.flags & EDepotFileFlag.Executable > 0

    @property
    def seekable(self) -> bool:
        return self.is_file

    def tell(self) -> int:
        if not self.seekable:
            raise ValueError('This file is not seekable, probably because its directory or symlink')
        return self.offset

    def seek(self, offset: int, whence: int = 0):
        """Seen file

        :param offset: file offset
        :param whence: offset mode, see :meth:`io.IOBase.seek`
        """
        if not self.seekable:
            raise ValueError('This file is not seekable, probably because its directory or symlink')

        if whence == 0:
            if offset < 0:
                raise OSError('Invalid argument')
        elif whence == 1:
            offset = self.offset + offset
        elif whence == 2:
            offset = self.size + offset
        else:
            raise ValueError('Invalid value for whence')

        self.offset = max(0, min(self.size, offset))

    async def _get_chunk(self, chunk):
        if not self._lc or self._lc.sha != chunk.sha:
            self._lcbuff = await self.manifest.cdn_client.get_chunk(
                self.manifest.app_id,
                self.manifest.depot_id,
                chunk.sha.hex(),
            )
            self._lc = chunk
        return self._lcbuff

    async def __aiter__(self):
        return self

    async def __anext__(self):
        return await self.next()

    async def __aenter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    async def next(self) -> bytes:
        line = await self.readline()
        if line == b'':
            raise StopIteration
        return line

    async def read(self, length: int = -1) -> bytes:
        """Read bytes from the file

        :param length: number of bytes to read. Read the whole file if not set
        :returns: file data
        """
        if length == -1:
            length = self.size - self.offset
        if length == 0 or self.offset >= self.size or self.size == 0:
            return b''

        end_offset = self.offset + length

        # we cache last chunk to allow small length reads and local seek
        if (
            self._lc
            and self.offset >= self._lc.offset
            and end_offset <= self._lc.offset + self._lc.cb_original
        ):
            data = self._lcbuff[
                self.offset - self._lc.offset : self.offset - self._lc.offset + length
            ]
        # if we need to read outside the bounds of the cached chunk
        # we go to loop over chunks to determine which to download
        else:
            data = BytesIO()
            start_offset = None

            # Manifest orders the chunks by offset in ascending order
            for chunk in self.chunks:
                if chunk.offset >= end_offset:
                    break

                chunk_start = chunk.offset
                chunk_end = chunk_start + chunk.cb_original

                if (
                    chunk_start <= self.offset < chunk_end
                    or (chunk_start > self.offset and end_offset > chunk_end)
                    or chunk_start < end_offset <= chunk_end
                ):
                    if start_offset is None:
                        start_offset = chunk.offset
                    data.write(await self._get_chunk(chunk))

            data.seek(self.offset - start_offset)
            data = data.read(length)

        self.offset = min(self.size, end_offset)
        return data

    async def readline(self) -> bytes:
        """Read a single line

        :return: single file line
        """
        buf = b''

        while True:
            chunk = await self.read(256)
            if chunk == b'':
                break

            pos = chunk.find(b'\n')
            if pos > -1:
                pos += 1  # include \n
                buf += chunk[:pos]
                self.seek(self.offset - (len(chunk) - pos))
                break

            buf += chunk

        return buf

    async def readlines(self) -> list[bytes]:
        """Get file contents as list of lines

        :return: list of lines
        """
        return [line async for line in self]


class CDNDepotManifest:
    PROTOBUF_PAYLOAD_MAGIC = 0x71F617D0
    PROTOBUF_METADATA_MAGIC = 0x1F4812BE
    PROTOBUF_SIGNATURE_MAGIC = 0x1B81B817
    PROTOBUF_ENDOFMANIFEST_MAGIC = 0x32C415AB

    name: str = None  #: set only by :meth:`CDNClient.get_manifests`

    def __init__(self, cdn_client: 'CDNClient', app_id: int, data: bytes):
        """Holds manifest metadata and file list.

        :param cdn_client: CDNClient instance
        :param app_id: App ID
        :param data: serialized manifest data
        """
        self.cdn_client = cdn_client
        self.app_id = app_id
        self.metadata = ContentManifestMetadata()
        self.payload = ContentManifestPayload()
        self.signature = ContentManifestSignature()

        if data:
            self.deserialize(data)

    def __repr__(self):
        params = ', '.join([
            'app_id=' + str(self.app_id),
            'depot_id=' + str(self.depot_id),
            'gid=' + str(self.gid),
            'creation_time='
            + repr(
                datetime.fromtimestamp(self.metadata.creation_time, UTC)
                .isoformat()
                .replace('T', ' ')
            ),
        ])

        if self.name:
            params = repr(self.name) + ', ' + params

        if self.filenames_encrypted:
            params += ', filenames_encrypted=True'

        return f'<{self.__class__.__name__}({params})>'

    @property
    def depot_id(self):
        """:type: int"""
        return self.metadata.depot_id

    @property
    def gid(self):
        """:type: int"""
        return self.metadata.gid_manifest

    @property
    def creation_time(self):
        """:type: int"""
        return self.metadata.creation_time

    @property
    def size_original(self):
        """:type: int"""
        return self.metadata.cb_disk_original

    @property
    def size_compressed(self):
        """:type: int"""
        return self.metadata.cb_disk_compressed

    @property
    def filenames_encrypted(self):
        """:type: bool"""
        return self.metadata.filenames_encrypted

    def decrypt_filenames(self, depot_key: bytes):
        """Decrypt all filenames in the manifest

        :param depot_key: depot key
        :type  depot_key: bytes
        :raises: :class:`RuntimeError`
        """
        if not self.metadata.filenames_encrypted:
            return

        try:
            for m in self.payload.mappings:
                m.filename = symmetric_decrypt(b64decode(m.filename), depot_key)

                if m.linktarget:
                    m.linktarget = symmetric_decrypt(b64decode(m.linktarget), depot_key)
        except Exception:
            raise RuntimeError('Unable to decrypt filename for depot manifest')

        self.metadata.filenames_encrypted = False

    def deserialize(self, data):
        """Deserialize a manifest (compressed or uncompressed)

        :param data: manifest data
        :type  data: bytes
        """
        try:
            with ZipFile(BytesIO(data)) as zf:
                data = zf.read(zf.filelist[0])
        except BadZipFile:
            pass

        data = StructReader(data)

        magic, length = data.unpack('<II')

        if magic != self.PROTOBUF_PAYLOAD_MAGIC:
            raise Exception('Expecting protobuf payload')

        self.payload = ContentManifestPayload()
        self.payload.ParseFromString(data.read(length))

        magic, length = data.unpack('<II')

        if magic != self.PROTOBUF_METADATA_MAGIC:
            raise Exception('Expecting protobuf metadata')

        self.metadata = ContentManifestMetadata()
        self.metadata.ParseFromString(data.read(length))

        magic, length = data.unpack('<II')

        if magic != self.PROTOBUF_SIGNATURE_MAGIC:
            raise Exception('Expecting protobuf signature')

        self.signature = ContentManifestSignature()
        self.signature.ParseFromString(data.read(length))

        (magic,) = data.unpack('<I')

        if magic != self.PROTOBUF_ENDOFMANIFEST_MAGIC:
            raise Exception('Expecting end of manifest')

        # order chunks in ascending order by their offset
        # required for CDNDepotFile
        for mapping in self.payload.mappings:
            mapping.chunks.sort(key=lambda x: x.offset, reverse=False)

    def serialize(self, compress=True):
        """Serialize manifest

        :param compress: wether the output should be Zip compressed
        :type  compress: bytes
        """
        data = BytesIO()

        part = self.payload.SerializeToString()
        data.write(pack('<II', self.PROTOBUF_PAYLOAD_MAGIC, len(part)))
        data.write(part)

        part = self.metadata.SerializeToString()
        data.write(pack('<II', self.PROTOBUF_METADATA_MAGIC, len(part)))
        data.write(part)

        part = self.signature.SerializeToString()
        data.write(pack('<II', self.PROTOBUF_SIGNATURE_MAGIC, len(part)))
        data.write(part)

        data.write(pack('<I', self.PROTOBUF_ENDOFMANIFEST_MAGIC))

        if compress:
            zbuff = BytesIO()
            with ZipFile(zbuff, 'w', ZIP_DEFLATED) as zf:
                zf.writestr('z', data.getvalue())

            return zbuff.getvalue()
        else:
            return data.getvalue()

    def __iter__(self):
        if not self.filenames_encrypted:
            for mapping in self.payload.mappings:
                yield CDNDepotFile(self, mapping)

    def iter_files(self, pattern: Optional[str] = None) -> Generator[CDNDepotFile]:
        """
        :param pattern: unix shell wildcard pattern, see :func:`.fnmatch`
        """
        if not self.filenames_encrypted:
            for mapping in self.payload.mappings:
                if pattern is not None and not fnmatch(
                    mapping.filename.rstrip('\x00 \n\t'), pattern
                ):
                    continue
                yield CDNDepotFile(self, mapping)


class CDNClient:
    """CDNClient allows loading and reading of manifests for Steam apps are used
    to list and download content"""

    _LOG = logging.getLogger('CDNClient')
    servers = deque()  #: CS Server list
    _chunk_cache = LRUCache(20)
    cell_id = 0  #: Cell ID to use, initialized from SteamClient instance

    @classmethod
    async def new(cls, client: SteamClient) -> Self:
        cls.semaphore = asyncio.Semaphore(8)  #: task semaphore
        cls.client = client  #: SteamClient instance
        cls.cell_id = cls.client.cell_id

        cls.cdn_auth_tokens = {}  #: CDN authentication token
        cls.depot_keys = {}  #: depot decryption keys
        cls.manifests = {}  #: CDNDepotManifest instances
        cls.app_depots = {}  #: app depot info
        cls.beta_passwords = {}  #: beta branch decryption keys
        cls.licensed_app_ids = set()  #: app_ids that the SteamClient instance has access to
        cls.licensed_depot_ids = set()  #: depot_ids that the SteamClient instance has access to
        cls._loaded_licenses = False

        result = cls()
        if not result.servers:
            await result.fetch_content_servers()
        await result.load_licenses()
        return result

    def clear_cache(self):
        """Cleared cached information. Next call on methods with caching will return fresh data"""
        self.manifests.clear()
        self.app_depots.clear()
        self.beta_passwords.clear()

    async def load_licenses(self):
        """Read licenses from SteamClient instance, required for determining accessible content"""
        self.licensed_app_ids.clear()
        self.licensed_depot_ids.clear()

        if self.client.steam_id.type == EType.AnonUser:
            packages = [17906]
        else:
            if not self.client.licenses:
                self._LOG.debug('No steam licenses found on SteamClient instance')
                return

            packages = list(
                map(
                    lambda l: {
                        'packageid': l.package_id,
                        'access_token': l.access_token,
                    },
                    self.client.licenses.values(),
                )
            )

        for package_id, info in (await self.client.get_product_info(packages=packages))[
            'packages'
        ].items():
            self.licensed_app_ids.update(info['appids'].values())
            self.licensed_depot_ids.update(info['depotids'].values())

    async def fetch_content_servers(self, num_servers: int = 20):
        """Update CS server list

        :param num_servers: numbers of CS server to fetch
        """
        self.servers.clear()

        self._LOG.debug('Trying to fetch content servers from Steam API')

        servers = await get_content_servers_from_webapi(self.cell_id, num_servers)
        servers = filter(lambda server: server.type != 'OpenCache', servers)  # see #264
        self.servers.extend(servers)

        if not self.servers:
            raise SteamError('Failed to fetch content servers')

    async def get_content_server(self, rotate: bool = False):
        """Get a CS server for content download

        :param rotate: forcefully rotate server list and get a new server
        """
        if rotate:
            self.servers.rotate(-1)
        return self.servers[0]

    async def get_cdn_auth_token(self, app_id: int, depot_id: int, hostname: str) -> str:
        """Get CDN authentication token

        :param app_id: app id
        :param depot_id: depot id
        :param hostname: cdn hostname
        :return: CDN authentication token
        """

        async def update_cdn_auth_tokens():
            resp: MsgProto = await self.client.send_um_and_wait(
                'ContentServerDirectory.GetCDNAuthToken#1',
                {'app_id': app_id, 'depot_id': depot_id, 'host_name': hostname},
                timeout=10,
            )

            if resp is None:
                raise SteamError(
                    f'Failed to get CDNAuthToken for {app_id}, {depot_id}, {hostname}',
                    EResult.Timeout,
                )
            elif resp.header.eresult == EResult.Fail:
                # no need authtoken?
                pass
            elif resp.header.eresult != EResult.OK:
                raise SteamError(
                    f'Failed to get CDNAuthToken for {app_id}, {depot_id}, {hostname}',
                    EResult(resp.header.eresult),
                )

            self.cdn_auth_tokens.update({
                app_id: {
                    depot_id: {
                        hostname: {
                            'eresult': resp.header.eresult,
                            'token': resp.body.token or '',
                            'expiration_time': resp.body.expiration_time or 0,
                        }
                    }
                }
            })

        if (
            app_id not in self.cdn_auth_tokens
            or depot_id not in self.cdn_auth_tokens[app_id]
            or hostname not in self.cdn_auth_tokens[app_id][depot_id]
        ):
            await update_cdn_auth_tokens()
        else:
            if self.cdn_auth_tokens[app_id][depot_id][hostname]['eresult'] != EResult.OK:
                pass
            elif (
                datetime.fromtimestamp(
                    self.cdn_auth_tokens[app_id][depot_id][hostname]['expiration_time'] - 60
                )
                < datetime.now()
            ):
                await update_cdn_auth_tokens()

        return self.cdn_auth_tokens[app_id][depot_id][hostname]['token']

    async def get_depot_key(self, app_id: int, depot_id: int) -> bytes:
        """Get depot key, which is needed to decrypt files

        :param app_id: app id
        :param depot_id: depot id
        :return: returns decryption key
        :raises SteamError: error message
        """
        if depot_id not in self.depot_keys:
            msg = await self.client.get_depot_key(app_id, depot_id)

            if msg and msg.eresult == EResult.OK:
                self.depot_keys[depot_id] = msg.depot_encryption_key
            else:
                raise SteamError(
                    'Failed getting depot key',
                    EResult.Timeout if msg is None else EResult(msg.eresult),
                )

        return self.depot_keys[depot_id]

    async def cdn_cmd(
        self,
        command: str,
        args: str,
        app_id: Optional[int] = None,
        depot_id: Optional[int] = None,
    ) -> tuple[ClientResponse, bytes]:
        """Run CDN command request

        :param command: command name
        :param args: args
        :param app_id: (optional) required for CDN authentication token
        :param depot_id: (optional) required for CDN authentication token
        :returns: requests response and data
        :raises SteamError: on error
        """
        server = await self.get_content_server()

        while True:
            url = '{}://{}:{}/{}/{}{}'.format(
                'https' if server.https else 'http',
                server.host,
                server.port,
                command,
                args,
                await self.get_cdn_auth_token(app_id, depot_id, str(server.host)),
            )

            try:
                async with AioHttpClientSessionWithUA() as session:
                    resp = await session.get(url, timeout=10)
                    if resp.ok:
                        return resp, await resp.read()
                    elif 400 <= resp.status < 500:
                        self._LOG.debug('Got HTTP %s', resp.status)
                        raise SteamError('HTTP Error %s' % resp.status)
                    await self.client.sleep(0.5)
            except SteamError:
                raise
            except Exception as exp:
                self._LOG.debug('Request error: %s', exp)

            server = await self.get_content_server(rotate=True)

    async def get_chunk(self, app_id: int, depot_id: int, chunk_id: int) -> bytes:
        """Download a single content chunk

        :param app_id: app ID
        :param depot_id: depot ID
        :param chunk_id: chunk ID
        :returns: chunk data
        :raises SteamError: error message
        """
        if (depot_id, chunk_id) not in self._chunk_cache:
            _, data = await self.cdn_cmd('depot', f'{depot_id}/chunk/{chunk_id}', app_id, depot_id)

            data = symmetric_decrypt(data, await self.get_depot_key(app_id, depot_id))

            if data[:2] == b'VZ':
                if data[-2:] != b'zv':
                    raise SteamError('VZ: Invalid footer: %s' % repr(data[-2:]))
                if data[2:3] != b'a':
                    raise SteamError('VZ: Invalid version: %s' % repr(data[2:3]))

                vzfilter = lzma._decode_filter_properties(lzma.FILTER_LZMA1, data[7:12])
                vzdec = lzma.LZMADecompressor(lzma.FORMAT_RAW, filters=[vzfilter])
                checksum, decompressed_size = struct.unpack('<II', data[-10:-2])
                # decompress_size is needed since lzma will sometime produce longer output
                # [12:-9] is need as sometimes lzma will produce shorter output
                # together they get us the right data
                data = vzdec.decompress(data[12:-9])[:decompressed_size]
                if crc32(data) != checksum:
                    raise SteamError("VZ: CRC32 checksum doesn't match for decompressed data")
            else:
                with ZipFile(BytesIO(data)) as zf:
                    data = zf.read(zf.filelist[0])

            self._chunk_cache[(depot_id, chunk_id)] = data

        return self._chunk_cache[(depot_id, chunk_id)]

    async def get_manifest_request_code(
        self,
        app_id: int,
        depot_id: int,
        manifest_gid: int,
        branch: str = 'public',
        branch_password_hash: Optional[str] = None,
    ) -> int:
        """Get manifest request code for authenticating manifest download

        :param app_id: App ID
        :param depot_id: Depot ID
        :param manifest_gid: Manifest gid
        :param branch: (optional) branch name
        :param branch_password_hash: (optional) branch password hash
        :returns: manifest request code
        """

        body = {
            'app_id': int(app_id),
            'depot_id': int(depot_id),
            'manifest_id': int(manifest_gid),
        }

        if branch and branch.lower() != 'public':
            body['app_branch'] = branch

            if branch_password_hash:
                body['branch_password_hash'] = branch_password_hash

        resp = await self.client.send_um_and_wait(
            'ContentServerDirectory.GetManifestRequestCode#1',
            body,
            timeout=5,
        )

        if resp is None or resp.header.eresult != EResult.OK:
            raise SteamError(
                f'Failed to get manifest code for {app_id}, {depot_id}, {manifest_gid}',
                EResult.Timeout if resp is None else EResult(resp.header.eresult),
            )

        return resp.body.manifest_request_code

    async def get_manifest(
        self,
        app_id: int,
        depot_id: int,
        manifest_gid: int,
        decrypt: bool = True,
        manifest_request_code: int = 0,
    ) -> CDNDepotManifest:
        """Download a manifest file

        :param app_id: App ID
        :type  app_id: int
        :param depot_id: Depot ID
        :type  depot_id: int
        :param manifest_gid: Manifest gid
        :type  manifest_gid: int
        :param decrypt: Decrypt manifest filenames
        :type  decrypt: bool
        :param manifest_request_code: Manifest request code, authenticates the download
        :type  manifest_request_code: int
        :returns: manifest instance
        :rtype: :class:`.CDNDepotManifest`
        """
        if (app_id, depot_id, manifest_gid) not in self.manifests:
            resp, data = await self.cdn_cmd(
                'depot',
                f'{depot_id}/manifest/{manifest_gid}/5/{manifest_request_code or ""}',
                app_id,
                depot_id,
            )

            if resp.ok:
                manifest = CDNDepotManifest(self, app_id, data)
                if decrypt:
                    manifest.decrypt_filenames(await self.get_depot_key(app_id, depot_id))
                self.manifests[(app_id, depot_id, manifest_gid)] = manifest

        return self.manifests[(app_id, depot_id, manifest_gid)]

    async def check_beta_password(self, app_id: int, password: str) -> EResult:
        """Check branch beta password to unlock encrypted branches

        :param app_id: App ID
        :param password: beta password
        :returns: result
        """
        resp = await self.client.send_job_and_wait(
            MsgProto(EMsg.ClientCheckAppBetaPassword),
            {'app_id': app_id, 'betapassword': password},
        )

        if resp.eresult == EResult.OK:
            self._LOG.debug(
                'Unlocked following beta branches: %s',
                ', '.join(map(lambda x: x.betaname.lower(), resp.betapasswords)),
            )
            for entry in resp.betapasswords:
                self.beta_passwords[(app_id, entry.betaname.lower())] = unhexlify(
                    entry.betapassword
                )
        else:
            self._LOG.debug('App beta password check failed. %r' % EResult(resp.eresult))

        return EResult(resp.eresult)

    async def get_app_depot_info(self, app_id: int) -> dict:
        if app_id not in self.app_depots:
            self.app_depots[app_id] = (await self.client.get_product_info([app_id]))['apps'][
                app_id
            ]['depots']
        return self.app_depots[app_id]

    async def has_license_for_depot(self, depot_id: int) -> bool:
        """Check if there is license for depot

        :returns: True if we have license
        """
        return depot_id in self.licensed_depot_ids or depot_id in self.licensed_app_ids

    async def get_manifests(
        self,
        app_id: int,
        branch: str = 'public',
        password: Optional[str] = None,
        filter_func: Optional[Callable[[int, dict], bool]] = None,
        decrypt: bool = True,
    ) -> list[CDNDepotManifest]:
        """Get a list of CDNDepotManifest for app

        :param app_id: App ID
        :param branch: branch name
        :param password: branch password for locked branches
        :param filter_func: Function to filter depots. ``func(depot_id, depot_info)``
        :returns: list of :class:`.CDNDepotManifest`
        :raises: ManifestError, SteamError
        """
        depots = await self.get_app_depot_info(app_id)

        is_enc_branch = False

        if branch not in depots.get('branches', {}):
            raise SteamError(f'No branch named {repr(branch)} for app_id {app_id}')
        elif int(depots['branches'][branch].get('pwdrequired', 0)) > 0:
            is_enc_branch = True

            if (app_id, branch) not in self.beta_passwords:
                if not password:
                    raise SteamError('Branch %r requires a password' % branch)

                result = await self.check_beta_password(app_id, password)

                if result != EResult.OK:
                    raise SteamError('Branch password is not valid. %r' % result)

                if (app_id, branch) not in self.beta_passwords:
                    raise SteamError('Incorrect password for branch %r' % branch)

        async def async_fetch_manifest(
            app_id,
            depot_id,
            manifest_gid,
            decrypt,
            depot_name,
            branch_name,
            branch_pass,
        ):
            async with self.semaphore:
                if isinstance(manifest_gid, dict):
                    # For some depots, Steam has started returning a dict
                    # {"public": {"gid": GID, "size": ..., "download": ...}, ...}
                    # instead of a simple map {"public": GID, ...}
                    manifest_gid = manifest_gid['gid']
                try:
                    manifest_code = await self.get_manifest_request_code(
                        app_id, depot_id, int(manifest_gid), branch_name, branch_pass
                    )
                except SteamError as exc:
                    raise ManifestError(
                        'Failed to acquire manifest code',
                        app_id,
                        depot_id,
                        manifest_gid,
                        exc,
                    )

                try:
                    manifest = await self.get_manifest(
                        app_id,
                        depot_id,
                        manifest_gid,
                        decrypt=decrypt,
                        manifest_request_code=manifest_code,
                    )
                except Exception as exc:
                    raise ManifestError('Failed download', app_id, depot_id, manifest_gid, exc)

                manifest.name = depot_name
                return manifest

        tasks = []
        shared_depots = {}

        for depot_id, depot_info in depots.items():
            if not depot_id.isdigit():
                continue

            depot_id = int(depot_id)

            # if filter_func set, use it to filter the list the depots
            if filter_func and not filter_func(depot_id, depot_info):
                continue

            # if we have no license for the depot, no point trying as we won't get depot_key
            if not await self.has_license_for_depot(depot_id):
                self._LOG.debug(
                    'No license for depot %s (%s). Skipped',
                    repr(depot_info.get('name', depot_id)),
                    depot_id,
                )
                continue

            # accumulate the shared depots
            if 'depotfromapp' in depot_info:
                shared_depots.setdefault(int(depot_info['depotfromapp']), set()).add(depot_id)
                continue

            # process depot, and get manifest for branch
            if is_enc_branch:
                egid = (
                    depot_info.get('encryptedmanifests', {}).get(branch, {}).get('encrypted_gid_2')
                )

                if egid is not None:
                    manifest_gid = decrypt_manifest_gid_2(
                        unhexlify(egid), self.beta_passwords[(app_id, branch)]
                    )
                else:
                    manifest_gid = depot_info.get('manifests', {}).get('public').get('gid')
            else:
                manifest_gid = depot_info.get('manifests', {}).get(branch).get('gid')

            if isinstance(manifest_gid, dict):
                # For some depots, Steam has started returning a dict
                # {"public": {"gid": GID, "size": ..., "download": ...}, ...}
                # instead of a simple map {"public": GID, ...}
                manifest_gid = manifest_gid['gid']

            if manifest_gid is not None:
                tasks.append(
                    asyncio.create_task(
                        async_fetch_manifest(
                            app_id,
                            depot_id,
                            manifest_gid,
                            decrypt,
                            depot_info.get('name', depot_id),
                            branch,
                            None,  # TODO: figure out how to pass this correctly
                        )
                    )
                )

        # collect results
        manifests = await asyncio.gather(*tasks)

        # for task in tasks:
        #     result = task.get()
        #     if isinstance(result, ManifestError):
        #         raise result
        #     manifests.append(result)

        # load shared depot manifests
        for app_id, depot_ids in shared_depots.items():

            def nested_ffunc(depot_id, depot_info, depot_ids=depot_ids, ffunc=filter_func):
                return int(depot_id) in depot_ids and (ffunc is None or ffunc(depot_id, depot_info))

            manifests += await self.get_manifests(app_id, filter_func=nested_ffunc)

        return manifests

    async def iter_files(
        self,
        app_id: int,
        filename_filter: Optional[str] = None,
        branch: str = 'public',
        password: str = None,
        filter_func: Optional[Callable[[str, dict], bool]] = None,
    ) -> AsyncGenerator[CDNDepotFile]:
        """Like :meth:`.get_manifests` but returns a iterator that goes through all the files
        in all the manifest.

        :param app_id: App ID
        :param filename_filter: wildcard filter for file paths
        :param branch: branch name
        :param password: branch password for locked branches
        :param filter_func:
            Function to filter depots. ``func(depot_id, depot_info)``
        :returns: generator of of CDN files
        """
        for manifest in await self.get_manifests(app_id, branch, password, filter_func):
            for file in manifest.iter_files(filename_filter):
                yield file

    async def get_manifest_for_workshop_item(self, item_id: int) -> CDNDepotManifest:
        """Get the manifest file for a worshop item that is hosted on SteamPipe

        :param item_id: Workshop ID
        :returns: manifest instance
        :raises: ManifestError, SteamError
        """
        resp: MsgProto = await self.client.send_um_and_wait(
            'PublishedFile.GetDetails#1',
            {
                'publishedfileids': [item_id],
                'includetags': False,
                'includeadditionalpreviews': False,
                'includechildren': False,
                'includekvtags': False,
                'includevotes': False,
                'short_description': True,
                'includeforsaledata': False,
                'includemetadata': False,
                'language': 0,
            },
        )

        if resp is None:
            raise SteamError('Timeout', EResult.Timeout)

        if resp.header.eresult != EResult.OK:
            raise SteamError(resp.header.error_message or 'No message', resp.header.eresult)

        wf: PublishedFileDetails = resp.body.publishedfiledetails[0]

        if wf.result != EResult.OK:
            raise SteamError(
                'Failed getting workshop file info',
                EResult(wf.result),
            )
        elif not wf.hcontent_file:
            raise SteamError('Workshop file is not on SteamPipe', EResult.FileNotFound)

        try:
            manifest_code = await self.get_manifest_request_code(
                wf.consumer_appid, wf.consumer_appid, wf.hcontent_file
            )
            manifest = await self.get_manifest(
                wf.consumer_appid,
                wf.consumer_appid,
                wf.hcontent_file,
                manifest_request_code=manifest_code,
            )
        except Exception as e:
            raise ManifestError(
                'Failed to acquire manifest',
                wf.consumer_appid,
                wf.consumer_appid,
                wf.hcontent_file,
                e,
            )

        manifest.name = wf.title
        return manifest
