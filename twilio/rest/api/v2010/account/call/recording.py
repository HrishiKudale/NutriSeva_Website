r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RecordingInstance(InstanceResource):
    class Source(object):
        DIALVERB = "DialVerb"
        CONFERENCE = "Conference"
        OUTBOUNDAPI = "OutboundAPI"
        TRUNKING = "Trunking"
        RECORDVERB = "RecordVerb"
        STARTCALLRECORDINGAPI = "StartCallRecordingAPI"
        STARTCONFERENCERECORDINGAPI = "StartConferenceRecordingAPI"

    class Status(object):
        IN_PROGRESS = "in-progress"
        PAUSED = "paused"
        STOPPED = "stopped"
        PROCESSING = "processing"
        COMPLETED = "completed"
        ABSENT = "absent"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource.
    :ivar api_version: The API version used to make the recording.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Recording resource is associated with.
    :ivar conference_sid: The Conference SID that identifies the conference associated with the recording, if a conference recording.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar start_time: The start time of the recording in GMT and in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar duration: The length of the recording in seconds.
    :ivar sid: The unique string that that we created to identify the Recording resource.
    :ivar price: The one-time cost of creating the recording in the `price_unit` currency.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    :ivar encryption_details: How to decrypt the recording if it was encrypted using [Call Recording Encryption](https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption) feature.
    :ivar price_unit: The currency used in the `price` property. Example: `USD`.
    :ivar status: 
    :ivar channels: The number of channels in the final recording file.  Can be: `1`, or `2`. Separating a two leg call into two separate channels of the recording file is supported in [Dial](https://www.twilio.com/docs/voice/twiml/dial#attributes-record) and [Outbound Rest API](https://www.twilio.com/docs/voice/make-calls) record options.
    :ivar source: 
    :ivar error_code: The error code that describes why the recording is `absent`. The error code is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors). This value is null if the recording `status` is not `absent`.
    :ivar track: The recorded track. Can be: `inbound`, `outbound`, or `both`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        call_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.api_version: Optional[str] = payload.get("api_version")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.conference_sid: Optional[str] = payload.get("conference_sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.start_time: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("start_time")
        )
        self.duration: Optional[str] = payload.get("duration")
        self.sid: Optional[str] = payload.get("sid")
        self.price: Optional[float] = deserialize.decimal(payload.get("price"))
        self.uri: Optional[str] = payload.get("uri")
        self.encryption_details: Optional[Dict[str, object]] = payload.get(
            "encryption_details"
        )
        self.price_unit: Optional[str] = payload.get("price_unit")
        self.status: Optional["RecordingInstance.Status"] = payload.get("status")
        self.channels: Optional[int] = deserialize.integer(payload.get("channels"))
        self.source: Optional["RecordingInstance.Source"] = payload.get("source")
        self.error_code: Optional[int] = deserialize.integer(payload.get("error_code"))
        self.track: Optional[str] = payload.get("track")

        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[RecordingContext] = None

    @property
    def _proxy(self) -> "RecordingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        """
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                account_sid=self._solution["account_sid"],
                call_sid=self._solution["call_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RecordingInstance":
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RecordingInstance":
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        status: "RecordingInstance.Status",
        pause_behavior: Union[str, object] = values.unset,
    ) -> "RecordingInstance":
        """
        Update the RecordingInstance

        :param status:
        :param pause_behavior: Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.

        :returns: The updated RecordingInstance
        """
        return self._proxy.update(
            status=status,
            pause_behavior=pause_behavior,
        )

    async def update_async(
        self,
        status: "RecordingInstance.Status",
        pause_behavior: Union[str, object] = values.unset,
    ) -> "RecordingInstance":
        """
        Asynchronous coroutine to update the RecordingInstance

        :param status:
        :param pause_behavior: Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.

        :returns: The updated RecordingInstance
        """
        return await self._proxy.update_async(
            status=status,
            pause_behavior=pause_behavior,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.RecordingInstance {}>".format(context)


class RecordingContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the RecordingContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to update.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Recording resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RecordingInstance:
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RecordingInstance:
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        status: "RecordingInstance.Status",
        pause_behavior: Union[str, object] = values.unset,
    ) -> RecordingInstance:
        """
        Update the RecordingInstance

        :param status:
        :param pause_behavior: Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.

        :returns: The updated RecordingInstance
        """
        data = values.of(
            {
                "Status": status,
                "PauseBehavior": pause_behavior,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        status: "RecordingInstance.Status",
        pause_behavior: Union[str, object] = values.unset,
    ) -> RecordingInstance:
        """
        Asynchronous coroutine to update the RecordingInstance

        :param status:
        :param pause_behavior: Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.

        :returns: The updated RecordingInstance
        """
        data = values.of(
            {
                "Status": status,
                "PauseBehavior": pause_behavior,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.RecordingContext {}>".format(context)


class RecordingPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RecordingInstance:
        """
        Build an instance of RecordingInstance

        :param payload: Payload response from the API
        """
        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.RecordingPage>"


class RecordingList(ListResource):
    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the RecordingList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json".format(
            **self._solution
        )

    def create(
        self,
        recording_status_callback_event: Union[List[str], object] = values.unset,
        recording_status_callback: Union[str, object] = values.unset,
        recording_status_callback_method: Union[str, object] = values.unset,
        trim: Union[str, object] = values.unset,
        recording_channels: Union[str, object] = values.unset,
        recording_track: Union[str, object] = values.unset,
    ) -> RecordingInstance:
        """
        Create the RecordingInstance

        :param recording_status_callback_event: The recording status events on which we should call the `recording_status_callback` URL. Can be: `in-progress`, `completed` and `absent` and the default is `completed`. Separate multiple event values with a space.
        :param recording_status_callback: The URL we should call using the `recording_status_callback_method` on each recording event specified in  `recording_status_callback_event`. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback).
        :param recording_status_callback_method: The HTTP method we should use to call `recording_status_callback`. Can be: `GET` or `POST` and the default is `POST`.
        :param trim: Whether to trim any leading and trailing silence in the recording. Can be: `trim-silence` or `do-not-trim` and the default is `do-not-trim`. `trim-silence` trims the silence from the beginning and end of the recording and `do-not-trim` does not.
        :param recording_channels: The number of channels used in the recording. Can be: `mono` or `dual` and the default is `mono`. `mono` records all parties of the call into one channel. `dual` records each party of a 2-party call into separate channels.
        :param recording_track: The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio.

        :returns: The created RecordingInstance
        """
        data = values.of(
            {
                "RecordingStatusCallbackEvent": serialize.map(
                    recording_status_callback_event, lambda e: e
                ),
                "RecordingStatusCallback": recording_status_callback,
                "RecordingStatusCallbackMethod": recording_status_callback_method,
                "Trim": trim,
                "RecordingChannels": recording_channels,
                "RecordingTrack": recording_track,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def create_async(
        self,
        recording_status_callback_event: Union[List[str], object] = values.unset,
        recording_status_callback: Union[str, object] = values.unset,
        recording_status_callback_method: Union[str, object] = values.unset,
        trim: Union[str, object] = values.unset,
        recording_channels: Union[str, object] = values.unset,
        recording_track: Union[str, object] = values.unset,
    ) -> RecordingInstance:
        """
        Asynchronously create the RecordingInstance

        :param recording_status_callback_event: The recording status events on which we should call the `recording_status_callback` URL. Can be: `in-progress`, `completed` and `absent` and the default is `completed`. Separate multiple event values with a space.
        :param recording_status_callback: The URL we should call using the `recording_status_callback_method` on each recording event specified in  `recording_status_callback_event`. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback).
        :param recording_status_callback_method: The HTTP method we should use to call `recording_status_callback`. Can be: `GET` or `POST` and the default is `POST`.
        :param trim: Whether to trim any leading and trailing silence in the recording. Can be: `trim-silence` or `do-not-trim` and the default is `do-not-trim`. `trim-silence` trims the silence from the beginning and end of the recording and `do-not-trim` does not.
        :param recording_channels: The number of channels used in the recording. Can be: `mono` or `dual` and the default is `mono`. `mono` records all parties of the call into one channel. `dual` records each party of a 2-party call into separate channels.
        :param recording_track: The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio.

        :returns: The created RecordingInstance
        """
        data = values.of(
            {
                "RecordingStatusCallbackEvent": serialize.map(
                    recording_status_callback_event, lambda e: e
                ),
                "RecordingStatusCallback": recording_status_callback,
                "RecordingStatusCallbackMethod": recording_status_callback_method,
                "Trim": trim,
                "RecordingChannels": recording_channels,
                "RecordingTrack": recording_track,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def stream(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[RecordingInstance]:
        """
        Streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[RecordingInstance]:
        """
        Asynchronously streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
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
                date_created=date_created,
                date_created_before=date_created_before,
                date_created_after=date_created_after,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Asynchronously lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
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
                date_created=date_created,
                date_created_before=date_created_before,
                date_created_after=date_created_after,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RecordingPage:
        """
        Retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately

        :param date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        """
        data = values.of(
            {
                "DateCreated": serialize.iso8601_date(date_created),
                "DateCreated<": serialize.iso8601_date(date_created_before),
                "DateCreated>": serialize.iso8601_date(date_created_after),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RecordingPage(self._version, response, self._solution)

    async def page_async(
        self,
        date_created: Union[date, object] = values.unset,
        date_created_before: Union[date, object] = values.unset,
        date_created_after: Union[date, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RecordingPage:
        """
        Asynchronously retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately

        :param date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        """
        data = values.of(
            {
                "DateCreated": serialize.iso8601_date(date_created),
                "DateCreated<": serialize.iso8601_date(date_created_before),
                "DateCreated>": serialize.iso8601_date(date_created_after),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RecordingPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> RecordingPage:
        """
        Retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RecordingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> RecordingPage:
        """
        Asynchronously retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RecordingPage(self._version, response, self._solution)

    def get(self, sid: str) -> RecordingContext:
        """
        Constructs a RecordingContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording resource to update.
        """
        return RecordingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> RecordingContext:
        """
        Constructs a RecordingContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording resource to update.
        """
        return RecordingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.RecordingList>"