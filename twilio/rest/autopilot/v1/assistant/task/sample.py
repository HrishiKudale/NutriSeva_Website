r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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


class SampleInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sample resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the resource.
    :ivar language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
    :ivar assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource.
    :ivar sid: The unique string that we created to identify the Sample resource.
    :ivar tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
    :ivar url: The absolute URL of the Sample resource.
    :ivar source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        task_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.task_sid: Optional[str] = payload.get("task_sid")
        self.language: Optional[str] = payload.get("language")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.tagged_text: Optional[str] = payload.get("tagged_text")
        self.url: Optional[str] = payload.get("url")
        self.source_channel: Optional[str] = payload.get("source_channel")

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[SampleContext] = None

    @property
    def _proxy(self) -> "SampleContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SampleContext for this SampleInstance
        """
        if self._context is None:
            self._context = SampleContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SampleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SampleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SampleInstance":
        """
        Fetch the SampleInstance


        :returns: The fetched SampleInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SampleInstance":
        """
        Asynchronous coroutine to fetch the SampleInstance


        :returns: The fetched SampleInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        language: Union[str, object] = values.unset,
        tagged_text: Union[str, object] = values.unset,
        source_channel: Union[str, object] = values.unset,
    ) -> "SampleInstance":
        """
        Update the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        """
        return self._proxy.update(
            language=language,
            tagged_text=tagged_text,
            source_channel=source_channel,
        )

    async def update_async(
        self,
        language: Union[str, object] = values.unset,
        tagged_text: Union[str, object] = values.unset,
        source_channel: Union[str, object] = values.unset,
    ) -> "SampleInstance":
        """
        Asynchronous coroutine to update the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        """
        return await self._proxy.update_async(
            language=language,
            tagged_text=tagged_text,
            source_channel=source_channel,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.SampleInstance {}>".format(context)


class SampleContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        """
        Initialize the SampleContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to update.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the SampleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SampleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SampleInstance:
        """
        Fetch the SampleInstance


        :returns: The fetched SampleInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SampleInstance:
        """
        Asynchronous coroutine to fetch the SampleInstance


        :returns: The fetched SampleInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        language: Union[str, object] = values.unset,
        tagged_text: Union[str, object] = values.unset,
        source_channel: Union[str, object] = values.unset,
    ) -> SampleInstance:
        """
        Update the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "TaggedText": tagged_text,
                "SourceChannel": source_channel,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        language: Union[str, object] = values.unset,
        tagged_text: Union[str, object] = values.unset,
        source_channel: Union[str, object] = values.unset,
    ) -> SampleInstance:
        """
        Asynchronous coroutine to update the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "TaggedText": tagged_text,
                "SourceChannel": source_channel,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.SampleContext {}>".format(context)


class SamplePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> SampleInstance:
        """
        Build an instance of SampleInstance

        :param payload: Payload response from the API
        """
        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.SamplePage>"


class SampleList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the SampleList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples".format(
            **self._solution
        )

    def create(
        self,
        language: str,
        tagged_text: str,
        source_channel: Union[str, object] = values.unset,
    ) -> SampleInstance:
        """
        Create the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the new sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The created SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "TaggedText": tagged_text,
                "SourceChannel": source_channel,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def create_async(
        self,
        language: str,
        tagged_text: str,
        source_channel: Union[str, object] = values.unset,
    ) -> SampleInstance:
        """
        Asynchronously create the SampleInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new sample. For example: `en-US`.
        :param tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param source_channel: The communication channel from which the new sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The created SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "TaggedText": tagged_text,
                "SourceChannel": source_channel,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def stream(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SampleInstance]:
        """
        Streams SampleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(language=language, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SampleInstance]:
        """
        Asynchronously streams SampleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(language=language, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SampleInstance]:
        """
        Lists SampleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
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
                language=language,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SampleInstance]:
        """
        Asynchronously lists SampleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
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
                language=language,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        language: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SamplePage:
        """
        Retrieve a single page of SampleInstance records from the API.
        Request is executed immediately

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SamplePage(self._version, response, self._solution)

    async def page_async(
        self,
        language: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SamplePage:
        """
        Asynchronously retrieve a single page of SampleInstance records from the API.
        Request is executed immediately

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SampleInstance
        """
        data = values.of(
            {
                "Language": language,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SamplePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SamplePage:
        """
        Retrieve a specific page of SampleInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SampleInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SamplePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SamplePage:
        """
        Asynchronously retrieve a specific page of SampleInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SampleInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SamplePage(self._version, response, self._solution)

    def get(self, sid: str) -> SampleContext:
        """
        Constructs a SampleContext

        :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
        """
        return SampleContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> SampleContext:
        """
        Constructs a SampleContext

        :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
        """
        return SampleContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.SampleList>"