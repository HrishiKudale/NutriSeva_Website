r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class EngagementContextInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the Account.
    :ivar context: As your flow executes, we save the state in what's called the Flow Context. Any data in the flow context can be accessed by your widgets as variables, either in configuration fields or in text areas as variable substitution.
    :ivar engagement_sid: The SID of the Engagement.
    :ivar flow_sid: The SID of the Flow.
    :ivar url: The URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        flow_sid: str,
        engagement_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.context: Optional[Dict[str, object]] = payload.get("context")
        self.engagement_sid: Optional[str] = payload.get("engagement_sid")
        self.flow_sid: Optional[str] = payload.get("flow_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
        }
        self._context: Optional[EngagementContextContext] = None

    @property
    def _proxy(self) -> "EngagementContextContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EngagementContextContext for this EngagementContextInstance
        """
        if self._context is None:
            self._context = EngagementContextContext(
                self._version,
                flow_sid=self._solution["flow_sid"],
                engagement_sid=self._solution["engagement_sid"],
            )
        return self._context

    def fetch(self) -> "EngagementContextInstance":
        """
        Fetch the EngagementContextInstance


        :returns: The fetched EngagementContextInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EngagementContextInstance":
        """
        Asynchronous coroutine to fetch the EngagementContextInstance


        :returns: The fetched EngagementContextInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.EngagementContextInstance {}>".format(context)


class EngagementContextContext(InstanceContext):
    def __init__(self, version: Version, flow_sid: str, engagement_sid: str):
        """
        Initialize the EngagementContextContext

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow.
        :param engagement_sid: The SID of the Engagement.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
        }
        self._uri = "/Flows/{flow_sid}/Engagements/{engagement_sid}/Context".format(
            **self._solution
        )

    def fetch(self) -> EngagementContextInstance:
        """
        Fetch the EngagementContextInstance


        :returns: The fetched EngagementContextInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EngagementContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
        )

    async def fetch_async(self) -> EngagementContextInstance:
        """
        Asynchronous coroutine to fetch the EngagementContextInstance


        :returns: The fetched EngagementContextInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EngagementContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.EngagementContextContext {}>".format(context)


class EngagementContextList(ListResource):
    def __init__(self, version: Version, flow_sid: str, engagement_sid: str):
        """
        Initialize the EngagementContextList

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow.
        :param engagement_sid: The SID of the Engagement.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
        }

    def get(self) -> EngagementContextContext:
        """
        Constructs a EngagementContextContext

        """
        return EngagementContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
        )

    def __call__(self) -> EngagementContextContext:
        """
        Constructs a EngagementContextContext

        """
        return EngagementContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V1.EngagementContextList>"
