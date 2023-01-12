"""Flespi REST API Class"""

import logging

import requests


class FlespiClient:
    """Helper class to work with flespi"""

    def __init__(
        self, token: str = "", is_dev: bool = False  # pylint: disable=W0613
    ) -> None:
        """Constructor

        Args:
            token (str, optional):
                Flespi token, must be a Standard or Full-Access token. Defaults to ''.
            is_dev (bool, optional):
                If true prints requests and parameter to console. Defaults to False.
        """

        self._token = token
        self._url = "https://flespi.io/"

        self._log = logging.getLogger("flespi.rest.FlespiClient")
        stream_logger = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
        stream_logger.setFormatter(formatter)
        self._log.addHandler(stream_logger)
        self._log.setLevel(logging.DEBUG)

        self._log.debug("FlespiClient initialized with token %s", token)

    @property
    def _headers(self):
        """Headers"""
        return {
            "Accept": "application/json",
            "Authorization": f"FlespiToken {self._token}",
        }

    def get(self, method: str):
        """Perform a GET request to the felspi API

        Args:
            method (str):
                the method call with the namespace
                (i.e. '/gw/devices', where '/gw' is the namespace and '/devices' is the method)
        """
        url = self._url + method
        self._log_request(method)

        try:
            request = requests.get(
                url=url,
                headers=self._headers,
                timeout=10,
            )
            return self._validate_and_return(request)
        except requests.exceptions.RequestException as err:
            self._log.debug("GET request failed: %s", err)
            return {"error": True, "reason": err}

    def post(self, method: str, params: dict):
        """Perform a POST request to the flespi API

        Args:
            method (str):
                The method to call with the namespace
                (i.e. '/gw/devices', where '/gw' is the namespace and '/devices' is the method)

            params (dict):
                A dictionary with key and params (i.e. {'name': 'Test'})

        """
        url = self._url + method
        self._log_request(method, params)

        try:
            request = requests.post(
                url=url,
                headers=self._headers,
                json=params,
                timeout=10,
            )
            return self._validate_and_return(request)
        except requests.exceptions.RequestException as err:
            self._log.debug("POST request failed: %s", err)
            return {"error": True, "reason": err}

    def put(self, method: str, params: dict):
        """Perform a PUT request to the flespi API

        Args:
            method (str):
                The method to call with the namespace
                (i.e. '/gw/devices', where '/gw' is the namespace and '/devices' is the method)

            params (dict):
                A dictionary with key and params (i.e. {'name': 'Test'})

        """
        url = self._url + method
        self._log_request(method, params)

        try:
            request = requests.post(
                url=url,
                headers=self._headers,
                json=params,
                timeout=10,
            )
            return self._validate_and_return(request)
        except requests.exceptions.RequestException as err:
            self._log.debug("PUT request failed: %s", err)
            return {"error": True, "reason": err}

    def delete(self, method: str):
        """Perform a DELETE request to the felspi API

        Args:
            method (str):
                the method call with the namespace
                (i.e. '/gw/devices', where '/gw' is the namespace and '/devices' is the method)
        """
        url = self._url + method
        self._log_request(method)

        try:
            request = requests.post(
                url=url,
                headers=self._headers,
                timeout=10,
            )
            return self._validate_and_return(request)
        except requests.exceptions.RequestException as err:
            self._log.debug("DELETE request failed: %s", err)
            return {"error": True, "reason": err}

    def _log_request(self, method: str, params=None):
        """Log request with DEBUG level"""
        self._log.debug("Request: %s - Params: %s", method, params)

    def _validate_and_return(self, request):
        """Validate the request and return the response with a dict object"""

        try:
            return {
                "error": request.status_code != 200,
                "code": request.status_code,
                "message": request.json(),
            }
        except ValueError as err:
            self._log.debug("Response validation failed: %s", err)
            return {"error": True, "reason": "Invalid JSON response"}
