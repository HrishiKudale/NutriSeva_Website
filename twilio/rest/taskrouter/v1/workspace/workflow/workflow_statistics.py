r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WorkflowStatisticsInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workflow resource.
    :ivar cumulative: An object that contains the cumulative statistics for the Workflow.
    :ivar realtime: An object that contains the real-time statistics for the Workflow.
    :ivar workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
    :ivar workspace_sid: The SID of the Workspace that contains the Workflow.
    :ivar url: The absolute URL of the Workflow statistics resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        workspace_sid: str,
        workflow_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.cumulative: Optional[Dict[str, object]] = payload.get("cumulative")
        self.realtime: Optional[Dict[str, object]] = payload.get("realtime")
        self.workflow_sid: Optional[str] = payload.get("workflow_sid")
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "workspace_sid": workspace_sid,
            "workflow_sid": workflow_sid,
        }
        self._context: Optional[WorkflowStatisticsContext] = None

    @property
    def _proxy(self) -> "WorkflowStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkflowStatisticsContext for this WorkflowStatisticsInstance
        """
        if self._context is None:
            self._context = WorkflowStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                workflow_sid=self._solution["workflow_sid"],
            )
        return self._context

    def fetch(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "WorkflowStatisticsInstance":
        """
        Fetch the WorkflowStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        """
        return self._proxy.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    async def fetch_async(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "WorkflowStatisticsInstance":
        """
        Asynchronous coroutine to fetch the WorkflowStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        """
        return await self._proxy.fetch_async(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkflowStatisticsInstance {}>".format(context)


class WorkflowStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowStatisticsContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
        :param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "workflow_sid": workflow_sid,
        }
        self._uri = (
            "/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics".format(
                **self._solution
            )
        )

    def fetch(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> WorkflowStatisticsInstance:
        """
        Fetch the WorkflowStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        """

        data = values.of(
            {
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return WorkflowStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            workflow_sid=self._solution["workflow_sid"],
        )

    async def fetch_async(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> WorkflowStatisticsInstance:
        """
        Asynchronous coroutine to fetch the WorkflowStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        """

        data = values.of(
            {
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return WorkflowStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            workflow_sid=self._solution["workflow_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkflowStatisticsContext {}>".format(context)


class WorkflowStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
        :param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "workflow_sid": workflow_sid,
        }

    def get(self) -> WorkflowStatisticsContext:
        """
        Constructs a WorkflowStatisticsContext

        """
        return WorkflowStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            workflow_sid=self._solution["workflow_sid"],
        )

    def __call__(self) -> WorkflowStatisticsContext:
        """
        Constructs a WorkflowStatisticsContext

        """
        return WorkflowStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            workflow_sid=self._solution["workflow_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.WorkflowStatisticsList>"