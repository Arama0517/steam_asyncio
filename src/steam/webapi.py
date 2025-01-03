"""
WebAPI provides a thin wrapper over `Steam's Web API <https://developer.valvesoftware.com/wiki/Steam_Web_API>`_

It is very friendly to exploration and prototyping when using ``ipython``, ``notebooks`` or similar.
The ``key`` will determine what WebAPI interfaces and methods are available.

.. note::
    Some endpoints don't require a key

Currently the WebAPI can be accessed via one of two API hosts. See :class:`APIHost`.

Example code:

.. code:: python

    >>> api = WebAPI(key)
    >>> api.call('ISteamUser.ResolveVanityURL', vanityurl='valve', url_type=2)
    >>> api.ISteamUser.ResolveVanityURL(vanityurl='valve', url_type=2)
    >>> api.ISteamUser.ResolveVanityURL_v1(vanityurl='valve', url_type=2)
    {'response': {'steamid': '103582791429521412', 'success': 1}}

All globals params (``key``, ``https``, ``format``, ``raw``) can be specified on per call basis.

.. code:: python

    >>> print a.ISteamUser.ResolveVanityURL(format='vdf', raw=True, vanityurl="valve", url_type=2)
    "response"
    {
            "steamid"       "103582791429521412"
            "success"       "1"
    }
"""

import asyncio
import json
from typing import Any, Literal, Optional
from xml.etree.ElementTree import Element

import vdf
from aiohttp import ClientSession
from lxml import etree

from steam.utils.web import AioHttpClientSessionWithUA


class APIHost:
    """Enum of currently available API hosts."""

    Public = 'api.steampowered.com'
    """ available over HTTP (port 80) and HTTPS (port 443)"""
    Partner = 'partner.steam-api.com'
    """available over HTTPS (port 443) only

    .. note::
        Key is required for every request. If not supplied you will get HTTP 403.
    """


DEFAULT_PARAMS = {
    # api parameters
    'apihost': APIHost.Public,
    'key': 'key',
    'format': 'json',
    # internal
    'https': True,
    'http_timeout': 30,
    'raw': False,
}


class WebAPI:
    """Steam WebAPI wrapper

    .. note::
        Interfaces and methods are populated automatically from Steam WebAPI.

    :param key: api key from https://steamcommunity.com/dev/apikey
    :type key: :class:`str`
    :param format: response format, either (``json``, ``vdf``, or ``xml``) only when ``raw=False``
    :type format: :class:`str`
    :param raw: return raw response
    :type raw: class:`bool`
    :param https: use ``https``
    :type https: :class:`bool`
    :param http_timeout: HTTP timeout in seconds
    :type http_timeout: :class:`int`
    :param apihost: api hostname, see :class:`APIHost`
    :type apihost: :class:`str`
    :param auto_load_interfaces: load interfaces from the Steam WebAPI
    :type auto_load_interfaces: :class:`bool`

    These can be specified per method call for one off calls
    """

    key = DEFAULT_PARAMS['key']
    format = DEFAULT_PARAMS['format']
    raw = DEFAULT_PARAMS['raw']
    https = DEFAULT_PARAMS['https']
    http_timeout = DEFAULT_PARAMS['http_timeout']
    apihost = DEFAULT_PARAMS['apihost']
    interfaces = []

    def __init__(
        self,
        key,
        format=DEFAULT_PARAMS['format'],
        raw=DEFAULT_PARAMS['raw'],
        https=DEFAULT_PARAMS['https'],
        http_timeout=DEFAULT_PARAMS['http_timeout'],
        apihost=DEFAULT_PARAMS['apihost'],
        auto_load_interfaces=True,
    ):
        self.key = key  #: api key
        self.format = format  #: format (``json``, ``vdf``, or ``xml``)
        self.raw = raw  #: return raw reponse or parse
        self.https = https  #: use https or not
        self.http_timeout = http_timeout  #: HTTP timeout in seconds
        self.apihost = apihost  #: ..versionadded:: 0.8.3 apihost hostname
        self.interfaces = []  #: list of all interfaces

        if auto_load_interfaces:
            self.load_interfaces(asyncio.run(self.fetch_interfaces()))

    def __repr__(self):
        return '{}(key={}, https={})'.format(
            self.__class__.__name__,
            repr(self.key),
            repr(self.https),
        )

    async def fetch_interfaces(self):
        """
        Returns a dict with the response from ``GetSupportedAPIList``

        :return: :class:`dict` of all interfaces and methods

        The returned value can passed to :meth:`load_interfaces`
        """
        return await get(
            'ISteamWebAPIUtil',
            'GetSupportedAPIList',
            1,
            https=self.https,
            apihost=self.apihost,
            caller=None,
            params={
                'format': 'json',
                'key': self.key,
            },
        )

    def load_interfaces(self, interfaces_dict):
        """
        Populates the namespace under the instance
        """
        if interfaces_dict.get('apilist', {}).get('interfaces', None) is None:
            raise ValueError('Invalid response for GetSupportedAPIList')

        interfaces = interfaces_dict['apilist']['interfaces']
        if len(interfaces) == 0:
            raise ValueError('API returned not interfaces; probably using invalid key')

        # clear existing interface instances
        for interface in self.interfaces:
            delattr(self, interface.name)
        self.interfaces = []

        # create interface instances from response
        for interface in interfaces:
            obj = WebAPIInterface(interface, parent=self)
            self.interfaces.append(obj)
            setattr(self, obj.name, obj)

    async def call(self, method_path, **kwargs):
        """
        Make an API call for specific method

        :param method_path: format ``Interface.Method`` (e.g. ``ISteamWebAPIUtil.GetServerInfo``)
        :type method_path: :class:`str`
        :param kwargs: keyword arguments for the specific method
        :return: response
        :rtype: :class:`dict`, :class:`lxml.etree.Element` or :class:`str`
        """

        interface, method = method_path.split('.', 1)
        return await getattr(getattr(self, interface), method)(**kwargs)

    def doc(self):
        """
        :return: Documentation for all interfaces and their methods
        :rtype: str
        """
        doc = 'Steam Web API - List of all interfaces\n\n'
        for interface in self.interfaces:
            doc += interface.__doc__
        return doc


class WebAPIInterface:
    """
    Steam Web API Interface
    """

    def __init__(self, interface_dict, parent):
        self._parent = parent
        self.name = interface_dict['name']
        self.methods = []

        for method in interface_dict['methods']:
            obj = WebAPIMethod(method, parent=self)
            self.methods.append(obj)

            # map the method name as attribute including version
            setattr(self, '%s_v%d' % (obj.name, obj.version), obj)

            # without version, but th refernce of latest version
            current_obj = getattr(self, obj.name, None)
            if current_obj is None or current_obj.version < obj.version:
                setattr(self, obj.name, obj)

    def __repr__(self):
        return '<{} {} with {} methods>'.format(
            self.__class__.__name__,
            repr(self.name),
            repr(len(list(self))),
        )

    def __iter__(self):
        return iter(self.methods)

    @property
    def key(self):
        return self._parent.key

    @property
    def apihost(self):
        return self._parent.apihost

    @property
    def https(self):
        return self._parent.https

    @property
    def http_timeout(self):
        return self._parent.http_timeout

    @property
    def format(self):
        return self._parent.format

    @property
    def raw(self):
        return self._parent.raw

    def doc(self):
        """
        :return: Documentation for all methods on this interface
        :rtype: str
        """
        return self.__doc__

    @property
    def __doc__(self):
        doc = '{}\n{}\n'.format(self.name, '-' * len(self.name))
        for method in self.methods:
            doc += '  %s\n' % method.__doc__.replace('\n', '\n  ')
        return doc


class WebAPIMethod:
    """
    Steam Web API Interface Method
    """

    def __init__(self, method_dict, parent):
        self.last_response = None
        self._parent = parent
        self._dict = method_dict

        params = method_dict['parameters']
        self._dict['parameters'] = {}
        for param in params:
            # add property indicating param can be a list
            param['_array'] = param['name'].endswith('[0]')
            # remove array suffix
            if param['_array']:
                param['name'] = param['name'][:-3]
            # turn params from a list to a dict
            self._dict['parameters'][param['name']] = param

    def __repr__(self):
        return '<{} {}>'.format(
            self.__class__.__name__,
            repr(
                '%s.%s_v%d'
                % (
                    self._parent.name,
                    self.name,
                    self.version,
                )
            ),
        )

    async def __call__(self, **kwargs):
        possible_kwargs = set(self._dict['parameters'].keys()) | set(DEFAULT_PARAMS.keys())
        unrecognized = set(kwargs.keys()).difference(possible_kwargs)
        if unrecognized:
            raise ValueError('Unrecognized parameter %s' % repr(unrecognized.pop()))

        params = {}
        # process special case kwargs
        for param in DEFAULT_PARAMS.keys():
            if param in kwargs:
                params[param] = kwargs[param]
                del kwargs[param]
            else:
                params[param] = getattr(self._parent, param)

        # process method parameters
        for param in self.parameters.values():
            name = param['name']
            islist = param['_array']
            optional = param['optional']

            if not optional and name not in kwargs and name != 'key':
                raise ValueError('Method requires %s to be set' % repr(name))

            if name in kwargs:
                if islist and not isinstance(kwargs[name], list):
                    raise ValueError(
                        'Expected {} to be a list, got {}'.format(
                            repr(name), repr(type(kwargs[name]))
                        )
                    )
                params[name] = kwargs[name]

        url = '{}://{}/{}/{}/v{}/'.format(
            'https' if self._parent.https else 'http',
            self._parent.apihost,
            self._parent.name,
            self.name,
            self.version,
        )

        return await webapi_request(
            url=url,
            method=self.method,
            caller=self,
            params=params,
        )

    @property
    def version(self):
        return self._dict['version']

    @property
    def method(self):
        return self._dict['httpmethod']

    @property
    def parameters(self):
        return self._dict['parameters']

    @property
    def name(self):
        return self._dict['name']

    def doc(self):
        """
        :return: Documentation for this method
        :rtype: str
        """
        return self.__doc__

    @property
    def __doc__(self):
        doc = '%(httpmethod)s %(name)s (v%(version)04d)\n' % self._dict

        if 'description' in self._dict:
            doc += '\n  %(description)s\n' % self._dict

        if len(self.parameters):
            doc += '  \n  Parameters:\n'

            for param in sorted(self.parameters.values(), key=lambda x: x['name']):
                doc += '    {} {} {}{}\n'.format(
                    param['name'].ljust(25),
                    ((param['type'] + '[]') if param['_array'] else param['type']).ljust(8),
                    'optional' if param['optional'] else 'required',
                    (
                        ('\n      - ' + param['description'])
                        if 'description' in param and param['description']
                        else ''
                    ),
                )

        return doc


async def webapi_request(
    url: str,
    method: Literal['GET', 'POST'] = 'GET',
    session: Optional[ClientSession] = None,
    caller: Optional[Any] = None,
    params: Optional[dict] = None,
) -> dict | Element | str:
    """Low level function for calling Steam's WebAPI

    .. versionchanged:: 0.8.3

    :param url: request url (e.g. ``https://api.steampowered.com/A/B/v001/``)
    :param method: HTTP method (GET or POST)
    :param session: an instance requests session, or one is created per call
    :param caller: caller reference, caller.last_response is set to the last response
    :param params: dict of WebAPI and endpoint specific params
    :return: response based on paramers
    """
    if method not in ('GET', 'POST'):
        raise ValueError('Only GET and POST methods are supported, got: %s' % repr(method))
    if params is None:
        params = {}

    onetime = {}
    for param in DEFAULT_PARAMS:
        params[param] = onetime[param] = params.get(param, DEFAULT_PARAMS[param])
    for param in ('raw', 'apihost', 'https', 'http_timeout'):
        del params[param]

    if onetime['format'] not in ('json', 'vdf', 'xml'):
        raise ValueError('Expected format to be json,vdf or xml; got %s' % onetime['format'])

    for k, v in list(params.items()):  # serialize some types
        if isinstance(v, bool):
            params[k] = 1 if v else 0
        elif isinstance(v, dict):
            params[k] = json.dumps(v)
        elif isinstance(v, list):
            del params[k]
            for i, lvalue in enumerate(v):
                params['%s[%d]' % (k, i)] = lvalue

    kwargs = {'params': params} if method == 'GET' else {'data': params}  # params to data for POST

    session_need_exit = False
    if session is None:
        session = AioHttpClientSessionWithUA()
        session_need_exit = True

    try:
        async with session.request(method, url, timeout=onetime['http_timeout'], **kwargs) as resp:
            # we keep a reference of the last response instance on the caller
            if caller is not None:
                caller.last_response = resp
            # 4XX and 5XX will cause this to raise
            resp.raise_for_status()

            if onetime['raw']:
                return await resp.text()
            elif onetime['format'] == 'json':
                return await resp.json()
            elif onetime['format'] == 'xml':
                return etree.fromstring(await resp.read())
            elif onetime['format'] == 'vdf':
                return vdf.loads(await resp.text())
    finally:
        if session_need_exit:
            await session.__aexit__(None, None, None)


async def get(
    interface: str,
    method: str,
    version: int = 1,
    apihost: str = DEFAULT_PARAMS['apihost'],
    https: bool = DEFAULT_PARAMS['https'],
    session: Optional[ClientSession] = None,
    caller: Optional[WebAPIMethod] = None,
    params: Optional[dict] = None,
) -> dict | Element | str:
    """Send GET request to an API endpoint

    .. versionadded:: 0.8.3

    :param interface: interface name
    :type interface: str
    :param method: method name
    :type method: str
    :param version: method version
    :type version: int
    :param apihost: API hostname
    :type apihost: str
    :param https: whether to use HTTPS
    :type https: bool
    :param params: parameters for endpoint
    :type params: dict
    :return: endpoint response
    :rtype: :class:`dict`, :class:`lxml.etree.Element`, :class:`str`
    """
    return await webapi_request(
        f'{"https" if https else "http"}://{apihost}/{interface}/{method}/v{version}',
        'GET',
        session=session,
        caller=caller,
        params=params,
    )


async def post(
    interface: str,
    method: str,
    version: int = 1,
    apihost: str = DEFAULT_PARAMS['apihost'],
    https: bool = DEFAULT_PARAMS['https'],
    session: Optional[ClientSession] = None,
    caller: Optional[WebAPIMethod] = None,
    params: Optional[dict] = None,
) -> dict | Element | str:
    """Send POST request to an API endpoint

    .. versionadded:: 0.8.3

    :param interface: interface name
    :type interface: str
    :param method: method name
    :type method: str
    :param version: method version
    :type version: int
    :param apihost: API hostname
    :type apihost: str
    :param https: whether to use HTTPS
    :type https: bool
    :param params: parameters for endpoint
    :type params: dict
    :return: endpoint response
    :rtype: :class:`dict`, :class:`lxml.etree.Element`, :class:`str`
    """
    return await webapi_request(
        f'{"https" if https else "http"}://{apihost}/{interface}/{method}/v{version}',
        'POST',
        session=session,
        caller=caller,
        params=params,
    )
