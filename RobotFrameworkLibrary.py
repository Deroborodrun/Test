import httplib
import base64
import json


class RobotFrameworkLibrary(object):
    """Test library for testing for demo REST sevrice http://httpbin.org/"""

    def __init__(self, user, passwd):
        self._connection = httplib.HTTPConnection("www.httpbin.org")
        self._user = user
        self._passwd = passwd

    def basic_auth(self, user, passwd):
        """Trys to autorize given user with given password"""
        enc = base64.b64encode("{0}:{1}".format(user, passwd))
        cake = {"Authorization": "Basic {0}".format(enc)}
        self._connection.request("GET", "/basic-auth/{0}/{1}".format(
                                    self._user, self._passwd), headers=cake)
        res = self._connection.getresponse()
        res.read()
        self._status = res.status

    def get(self, header, value):
        """Send request with given header"""
        tea = {header: value}
        self._connection.request("GET", "/get", headers=tea)
        res = self._connection.getresponse()
        self._headers = json.loads(res.read())['headers']
        self._status = res.status

    def stream(self, n):
        """Returns numbers of lines in response"""
        self._connection.request("GET", "/stream/{0}".format(n))
        res = self._connection.getresponse()
        self._status = res.status
        self._coffee = res.read().count('\n')

    def should_have_header(self, header):
        """Checks whether response has given header"""
        msg = "Header '{0}' Not Found in {1}".format(header, json.dumps(
              self._headers, sort_keys=True, indent=4, separators=(',', ': ')))
        assert header in self._headers, msg

    def stream_should_be(self, numbers):
        """Checks whether response has given number of lines"""
        assert self._coffee, '{0} != {1}'.format(self._coffee, numbers)

    def status_should_be_equal(self, status):
        """Check response status.
        You call this method after methods that send requests to service
        """
        assert status == self._status, \
            '{0} != {1}'.format(status, self._status)

    def header_should_be(self, header, value):
        """The given header has an expected value """
        assert self._headers[header] == value, '{0} != {1}'.format(
                                                self._headers[header], value)
