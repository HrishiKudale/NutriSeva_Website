r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FleetInstance(InstanceResource):
    class DataMetering(object):
        PAYG = "payg"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Fleet resource.
    :ivar sid: The unique string that we created to identify the Fleet resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Fleet resource.
    :ivar data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
    :ivar data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 250MB.
    :ivar data_metering: 
    :ivar sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `false`.
    :ivar sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :ivar sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
    :ivar network_access_profile_sid: The SID of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
    :ivar ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
    :ivar ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.data_enabled: Optional[bool] = payload.get("data_enabled")
        self.data_limit: Optional[int] = deserialize.integer(payload.get("data_limit"))
        self.data_metering: Optional["FleetInstance.DataMetering"] = payload.get(
            "data_metering"
        )
        self.sms_commands_enabled: Optional[bool] = payload.get("sms_commands_enabled")
        self.sms_commands_url: Optional[str] = payload.get("sms_commands_url")
        self.sms_commands_method: Optional[str] = payload.get("sms_commands_method")
        self.network_access_profile_sid: Optional[str] = payload.get(
            "network_access_profile_sid"
        )
        self.ip_commands_url: Optional[str] = payload.get("ip_commands_url")
        self.ip_commands_method: Optional[str] = payload.get("ip_commands_method")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[FleetContext] = None

    @property
    def _proxy(self) -> "FleetContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FleetContext for this FleetInstance
        """
        if self._context is None:
            self._context = FleetContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "FleetInstance":
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FleetInstance":
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        network_access_profile: Union[str, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
    ) -> "FleetInstance":
        """
        Update the FleetInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            network_access_profile=network_access_profile,
            ip_commands_url=ip_commands_url,
            ip_commands_method=ip_commands_method,
            sms_commands_url=sms_commands_url,
            sms_commands_method=sms_commands_method,
            data_limit=data_limit,
        )

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        network_access_profile: Union[str, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
    ) -> "FleetInstance":
        """
        Asynchronous coroutine to update the FleetInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            network_access_profile=network_access_profile,
            ip_commands_url=ip_commands_url,
            ip_commands_method=ip_commands_method,
            sms_commands_url=sms_commands_url,
            sms_commands_method=sms_commands_method,
            data_limit=data_limit,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.FleetInstance {}>".format(context)


class FleetContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FleetContext

        :param version: Version that contains the resource
        :param sid: The SID of the Fleet resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Fleets/{sid}".format(**self._solution)

    def fetch(self) -> FleetInstance:
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FleetInstance:
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        network_access_profile: Union[str, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
    ) -> FleetInstance:
        """
        Update the FleetInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "NetworkAccessProfile": network_access_profile,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
                "DataLimit": data_limit,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        network_access_profile: Union[str, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
    ) -> FleetInstance:
        """
        Asynchronous coroutine to update the FleetInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "NetworkAccessProfile": network_access_profile,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
                "DataLimit": data_limit,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.FleetContext {}>".format(context)


class FleetPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FleetInstance:
        """
        Build an instance of FleetInstance

        :param payload: Payload response from the API
        """
        return FleetInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.FleetPage>"


class FleetList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FleetList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Fleets"

    def create(
        self,
        network_access_profile: str,
        unique_name: Union[str, object] = values.unset,
        data_enabled: Union[bool, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_enabled: Union[bool, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
    ) -> FleetInstance:
        """
        Create the FleetInstance

        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.

        :returns: The created FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "UniqueName": unique_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsEnabled": sms_commands_enabled,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    async def create_async(
        self,
        network_access_profile: str,
        unique_name: Union[str, object] = values.unset,
        data_enabled: Union[bool, object] = values.unset,
        data_limit: Union[int, object] = values.unset,
        ip_commands_url: Union[str, object] = values.unset,
        ip_commands_method: Union[str, object] = values.unset,
        sms_commands_enabled: Union[bool, object] = values.unset,
        sms_commands_url: Union[str, object] = values.unset,
        sms_commands_method: Union[str, object] = values.unset,
    ) -> FleetInstance:
        """
        Asynchronously create the FleetInstance

        :param network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        :param data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
        :param ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
        :param sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.

        :returns: The created FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "UniqueName": unique_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsEnabled": sms_commands_enabled,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    def stream(
        self,
        network_access_profile: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[FleetInstance]:
        """
        Streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            network_access_profile=network_access_profile, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        network_access_profile: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[FleetInstance]:
        """
        Asynchronously streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            network_access_profile=network_access_profile, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        network_access_profile: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FleetInstance]:
        """
        Lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                network_access_profile=network_access_profile,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        network_access_profile: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FleetInstance]:
        """
        Asynchronously lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                network_access_profile=network_access_profile,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        network_access_profile: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FleetPage:
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FleetPage(self._version, response)

    async def page_async(
        self,
        network_access_profile: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FleetPage:
        """
        Asynchronously retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return FleetPage(self._version, response)

    def get_page(self, target_url: str) -> FleetPage:
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FleetPage(self._version, response)

    async def get_page_async(self, target_url: str) -> FleetPage:
        """
        Asynchronously retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FleetPage(self._version, response)

    def get(self, sid: str) -> FleetContext:
        """
        Constructs a FleetContext

        :param sid: The SID of the Fleet resource to update.
        """
        return FleetContext(self._version, sid=sid)

    def __call__(self, sid: str) -> FleetContext:
        """
        Constructs a FleetContext

        :param sid: The SID of the Fleet resource to update.
        """
        return FleetContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.FleetList>"