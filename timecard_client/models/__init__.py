"""Contains all the data models used in inputs/outputs"""

from .assign_working_profile_body import AssignWorkingProfileBody
from .assign_working_profile_response_201 import AssignWorkingProfileResponse201
from .create_absence_booking_body import CreateAbsenceBookingBody
from .create_absence_booking_body_weekdays_item import CreateAbsenceBookingBodyWeekdaysItem
from .create_absence_booking_response_201 import CreateAbsenceBookingResponse201
from .create_booking_body import CreateBookingBody
from .create_booking_body_location import CreateBookingBodyLocation
from .create_booking_body_type import CreateBookingBodyType
from .create_booking_response_201 import CreateBookingResponse201
from .create_booking_response_201_booking_type_0 import CreateBookingResponse201BookingType0
from .create_booking_response_201_booking_type_0_location_type_0 import (
    CreateBookingResponse201BookingType0LocationType0,
)
from .create_carry_over_body import CreateCarryOverBody
from .create_carry_over_response_201 import CreateCarryOverResponse201
from .create_carry_over_response_201_unit import CreateCarryOverResponse201Unit
from .create_person_body import CreatePersonBody
from .create_person_body_free_fields_item import CreatePersonBodyFreeFieldsItem
from .create_person_body_sex import CreatePersonBodySex
from .create_person_body_time_recording import CreatePersonBodyTimeRecording
from .create_person_response_201 import CreatePersonResponse201
from .create_person_response_201_au_period_days import CreatePersonResponse201AuPeriodDays
from .create_person_response_201_external_logins import CreatePersonResponse201ExternalLogins
from .create_person_response_201_free_fields_item import CreatePersonResponse201FreeFieldsItem
from .create_person_response_201_free_fields_item_lookup_type_0_item import (
    CreatePersonResponse201FreeFieldsItemLookupType0Item,
)
from .create_person_response_201_free_licences import CreatePersonResponse201FreeLicences
from .create_person_response_201_modules import CreatePersonResponse201Modules
from .create_person_response_201_time_recording import CreatePersonResponse201TimeRecording
from .create_person_response_201_time_recording_calculation_templates import (
    CreatePersonResponse201TimeRecordingCalculationTemplates,
)
from .create_person_response_201_time_recording_holiday import CreatePersonResponse201TimeRecordingHoliday
from .create_person_response_201_time_recording_supervisors_item import (
    CreatePersonResponse201TimeRecordingSupervisorsItem,
)
from .create_person_response_201_time_recording_working_profile import (
    CreatePersonResponse201TimeRecordingWorkingProfile,
)
from .create_work_operation_body import CreateWorkOperationBody
from .create_work_operation_response_201 import CreateWorkOperationResponse201
from .create_work_operation_response_201_free_fields_item import CreateWorkOperationResponse201FreeFieldsItem
from .create_work_operation_response_201_free_fields_item_lookup_type_0_item import (
    CreateWorkOperationResponse201FreeFieldsItemLookupType0Item,
)
from .get_absence_overview_response_200 import GetAbsenceOverviewResponse200
from .get_absence_overview_response_200_items_item import GetAbsenceOverviewResponse200ItemsItem
from .get_absence_overview_response_200_items_item_days_item import GetAbsenceOverviewResponse200ItemsItemDaysItem
from .get_absence_overview_response_200_items_item_days_item_entries_item import (
    GetAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem,
)
from .get_absence_type_response_200 import GetAbsenceTypeResponse200
from .get_absence_type_response_200_free_fields_item import GetAbsenceTypeResponse200FreeFieldsItem
from .get_absence_type_response_200_free_fields_item_lookup_type_0_item import (
    GetAbsenceTypeResponse200FreeFieldsItemLookupType0Item,
)
from .get_audit_event_response_200 import GetAuditEventResponse200
from .get_audit_event_response_200_action import GetAuditEventResponse200Action
from .get_audit_event_response_200_outcome import GetAuditEventResponse200Outcome
from .get_audit_event_response_200_query import GetAuditEventResponse200Query
from .get_audit_event_response_200_upstream_calls_item import GetAuditEventResponse200UpstreamCallsItem
from .get_booking_response_200 import GetBookingResponse200
from .get_booking_response_200_location_type_0 import GetBookingResponse200LocationType0
from .get_break_rule_response_200 import GetBreakRuleResponse200
from .get_daily_balance_response_200 import GetDailyBalanceResponse200
from .get_daily_balance_response_200_absences_item import GetDailyBalanceResponse200AbsencesItem
from .get_daily_balance_response_200_booking_time_range import GetDailyBalanceResponse200BookingTimeRange
from .get_daily_balance_response_200_calculations_item import GetDailyBalanceResponse200CalculationsItem
from .get_daily_balance_response_200_calculations_item_unit import GetDailyBalanceResponse200CalculationsItemUnit
from .get_daily_balance_response_200_carry_overs_item import GetDailyBalanceResponse200CarryOversItem
from .get_daily_balance_response_200_carry_overs_item_kind import GetDailyBalanceResponse200CarryOversItemKind
from .get_daily_balance_response_200_carry_overs_item_unit import GetDailyBalanceResponse200CarryOversItemUnit
from .get_daily_balance_response_200_evaluation_changed import GetDailyBalanceResponse200EvaluationChanged
from .get_daily_balance_response_200_projects_item import GetDailyBalanceResponse200ProjectsItem
from .get_daily_balance_response_200_working_profile import GetDailyBalanceResponse200WorkingProfile
from .get_department_response_200 import GetDepartmentResponse200
from .get_department_response_200_free_fields_item import GetDepartmentResponse200FreeFieldsItem
from .get_department_response_200_free_fields_item_lookup_type_0_item import (
    GetDepartmentResponse200FreeFieldsItemLookupType0Item,
)
from .get_department_response_200_kind import GetDepartmentResponse200Kind
from .get_department_response_200_time_recording_type_0 import GetDepartmentResponse200TimeRecordingType0
from .get_free_field_response_200 import GetFreeFieldResponse200
from .get_free_field_response_200_lookup_type_0_item import GetFreeFieldResponse200LookupType0Item
from .get_group_response_200 import GetGroupResponse200
from .get_group_response_200_free_fields_item import GetGroupResponse200FreeFieldsItem
from .get_group_response_200_free_fields_item_lookup_type_0_item import GetGroupResponse200FreeFieldsItemLookupType0Item
from .get_group_response_200_kind import GetGroupResponse200Kind
from .get_group_response_200_time_recording_type_0 import GetGroupResponse200TimeRecordingType0
from .get_health_response_200 import GetHealthResponse200
from .get_health_response_200_audit_db import GetHealthResponse200AuditDb
from .get_health_response_200_status import GetHealthResponse200Status
from .get_health_response_200_timecard import GetHealthResponse200Timecard
from .get_health_response_503 import GetHealthResponse503
from .get_health_response_503_audit_db import GetHealthResponse503AuditDb
from .get_health_response_503_status import GetHealthResponse503Status
from .get_health_response_503_timecard import GetHealthResponse503Timecard
from .get_me_response_200 import GetMeResponse200
from .get_person_absence_overview_response_200 import GetPersonAbsenceOverviewResponse200
from .get_person_absence_overview_response_200_items_item import GetPersonAbsenceOverviewResponse200ItemsItem
from .get_person_absence_overview_response_200_items_item_days_item import (
    GetPersonAbsenceOverviewResponse200ItemsItemDaysItem,
)
from .get_person_absence_overview_response_200_items_item_days_item_entries_item import (
    GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem,
)
from .get_person_by_person_no_response_200 import GetPersonByPersonNoResponse200
from .get_person_by_person_no_response_200_au_period_days import GetPersonByPersonNoResponse200AuPeriodDays
from .get_person_by_person_no_response_200_external_logins import GetPersonByPersonNoResponse200ExternalLogins
from .get_person_by_person_no_response_200_free_fields_item import GetPersonByPersonNoResponse200FreeFieldsItem
from .get_person_by_person_no_response_200_free_fields_item_lookup_type_0_item import (
    GetPersonByPersonNoResponse200FreeFieldsItemLookupType0Item,
)
from .get_person_by_person_no_response_200_free_licences import GetPersonByPersonNoResponse200FreeLicences
from .get_person_by_person_no_response_200_modules import GetPersonByPersonNoResponse200Modules
from .get_person_by_person_no_response_200_time_recording import GetPersonByPersonNoResponse200TimeRecording
from .get_person_by_person_no_response_200_time_recording_calculation_templates import (
    GetPersonByPersonNoResponse200TimeRecordingCalculationTemplates,
)
from .get_person_by_person_no_response_200_time_recording_holiday import (
    GetPersonByPersonNoResponse200TimeRecordingHoliday,
)
from .get_person_by_person_no_response_200_time_recording_supervisors_item import (
    GetPersonByPersonNoResponse200TimeRecordingSupervisorsItem,
)
from .get_person_by_person_no_response_200_time_recording_working_profile import (
    GetPersonByPersonNoResponse200TimeRecordingWorkingProfile,
)
from .get_person_calendar_response_200 import GetPersonCalendarResponse200
from .get_person_calendar_response_200_absent_days_item import GetPersonCalendarResponse200AbsentDaysItem
from .get_person_calendar_response_200_public_holidays_item import GetPersonCalendarResponse200PublicHolidaysItem
from .get_person_calendar_response_200_sick_days import GetPersonCalendarResponse200SickDays
from .get_person_calendar_response_200_sick_days_certificate_available_item import (
    GetPersonCalendarResponse200SickDaysCertificateAvailableItem,
)
from .get_person_calendar_response_200_sick_days_certificate_missing_item import (
    GetPersonCalendarResponse200SickDaysCertificateMissingItem,
)
from .get_person_calendar_response_200_sick_days_certificate_not_required_item import (
    GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem,
)
from .get_person_response_200 import GetPersonResponse200
from .get_person_response_200_au_period_days import GetPersonResponse200AuPeriodDays
from .get_person_response_200_external_logins import GetPersonResponse200ExternalLogins
from .get_person_response_200_free_fields_item import GetPersonResponse200FreeFieldsItem
from .get_person_response_200_free_fields_item_lookup_type_0_item import (
    GetPersonResponse200FreeFieldsItemLookupType0Item,
)
from .get_person_response_200_free_licences import GetPersonResponse200FreeLicences
from .get_person_response_200_modules import GetPersonResponse200Modules
from .get_person_response_200_time_recording import GetPersonResponse200TimeRecording
from .get_person_response_200_time_recording_calculation_templates import (
    GetPersonResponse200TimeRecordingCalculationTemplates,
)
from .get_person_response_200_time_recording_holiday import GetPersonResponse200TimeRecordingHoliday
from .get_person_response_200_time_recording_supervisors_item import GetPersonResponse200TimeRecordingSupervisorsItem
from .get_person_response_200_time_recording_working_profile import GetPersonResponse200TimeRecordingWorkingProfile
from .get_project_response_200 import GetProjectResponse200
from .get_project_response_200_free_fields_item import GetProjectResponse200FreeFieldsItem
from .get_project_response_200_free_fields_item_lookup_type_0_item import (
    GetProjectResponse200FreeFieldsItemLookupType0Item,
)
from .get_version_response_200 import GetVersionResponse200
from .get_work_operation_response_200 import GetWorkOperationResponse200
from .get_work_operation_response_200_free_fields_item import GetWorkOperationResponse200FreeFieldsItem
from .get_work_operation_response_200_free_fields_item_lookup_type_0_item import (
    GetWorkOperationResponse200FreeFieldsItemLookupType0Item,
)
from .get_working_profile_response_200 import GetWorkingProfileResponse200
from .get_working_profile_response_200_free_fields_item import GetWorkingProfileResponse200FreeFieldsItem
from .get_working_profile_response_200_free_fields_item_lookup_type_0_item import (
    GetWorkingProfileResponse200FreeFieldsItemLookupType0Item,
)
from .get_working_profile_response_200_working_days_item import GetWorkingProfileResponse200WorkingDaysItem
from .get_working_profile_response_200_working_days_item_core_time_2_type_0 import (
    GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0,
)
from .get_working_profile_response_200_working_days_item_core_time_type_0 import (
    GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0,
)
from .get_working_profile_response_200_working_days_item_evaluated_time_type_0 import (
    GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0,
)
from .get_working_profile_response_200_working_days_item_permitted_time_type_0 import (
    GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0,
)
from .list_absence_types_response_200 import ListAbsenceTypesResponse200
from .list_absence_types_response_200_items_item import ListAbsenceTypesResponse200ItemsItem
from .list_absence_types_usage import ListAbsenceTypesUsage
from .list_allowed_projects_response_200 import ListAllowedProjectsResponse200
from .list_allowed_projects_response_200_items_item import ListAllowedProjectsResponse200ItemsItem
from .list_audit_events_action import ListAuditEventsAction
from .list_audit_events_format import ListAuditEventsFormat
from .list_audit_events_outcome import ListAuditEventsOutcome
from .list_audit_events_response_200 import ListAuditEventsResponse200
from .list_audit_events_response_200_items_item import ListAuditEventsResponse200ItemsItem
from .list_audit_events_response_200_items_item_action import ListAuditEventsResponse200ItemsItemAction
from .list_audit_events_response_200_items_item_outcome import ListAuditEventsResponse200ItemsItemOutcome
from .list_audit_events_response_200_items_item_query import ListAuditEventsResponse200ItemsItemQuery
from .list_audit_events_response_200_items_item_upstream_calls_item import (
    ListAuditEventsResponse200ItemsItemUpstreamCallsItem,
)
from .list_bookings_response_200 import ListBookingsResponse200
from .list_bookings_response_200_items_item import ListBookingsResponse200ItemsItem
from .list_break_rules_response_200 import ListBreakRulesResponse200
from .list_break_rules_response_200_items_item import ListBreakRulesResponse200ItemsItem
from .list_calculation_accounts_response_200 import ListCalculationAccountsResponse200
from .list_calculation_accounts_response_200_items_item import ListCalculationAccountsResponse200ItemsItem
from .list_calculation_accounts_response_200_items_item_unit import ListCalculationAccountsResponse200ItemsItemUnit
from .list_calculation_templates_response_200 import ListCalculationTemplatesResponse200
from .list_calculation_templates_response_200_items_item import ListCalculationTemplatesResponse200ItemsItem
from .list_carry_overs_response_200 import ListCarryOversResponse200
from .list_carry_overs_response_200_items_item import ListCarryOversResponse200ItemsItem
from .list_carry_overs_response_200_items_item_unit import ListCarryOversResponse200ItemsItemUnit
from .list_department_members_response_200 import ListDepartmentMembersResponse200
from .list_department_members_response_200_items_item import ListDepartmentMembersResponse200ItemsItem
from .list_department_members_response_200_items_item_state import ListDepartmentMembersResponse200ItemsItemState
from .list_departments_response_200 import ListDepartmentsResponse200
from .list_departments_response_200_items_item import ListDepartmentsResponse200ItemsItem
from .list_free_fields_response_200 import ListFreeFieldsResponse200
from .list_free_fields_response_200_items_item import ListFreeFieldsResponse200ItemsItem
from .list_group_members_response_200 import ListGroupMembersResponse200
from .list_group_members_response_200_items_item import ListGroupMembersResponse200ItemsItem
from .list_group_members_response_200_items_item_state import ListGroupMembersResponse200ItemsItemState
from .list_groups_response_200 import ListGroupsResponse200
from .list_groups_response_200_items_item import ListGroupsResponse200ItemsItem
from .list_person_bookings_response_200 import ListPersonBookingsResponse200
from .list_person_bookings_response_200_items_item import ListPersonBookingsResponse200ItemsItem
from .list_persons_response_200 import ListPersonsResponse200
from .list_persons_response_200_items_item import ListPersonsResponse200ItemsItem
from .list_persons_response_200_items_item_state import ListPersonsResponse200ItemsItemState
from .list_persons_state import ListPersonsState
from .list_presence_response_200 import ListPresenceResponse200
from .list_presence_response_200_items_item import ListPresenceResponse200ItemsItem
from .list_presence_response_200_items_item_status import ListPresenceResponse200ItemsItemStatus
from .list_project_work_operations_response_200 import ListProjectWorkOperationsResponse200
from .list_project_work_operations_response_200_items_item import ListProjectWorkOperationsResponse200ItemsItem
from .list_projects_response_200 import ListProjectsResponse200
from .list_projects_response_200_items_item import ListProjectsResponse200ItemsItem
from .list_work_operations_response_200 import ListWorkOperationsResponse200
from .list_work_operations_response_200_items_item import ListWorkOperationsResponse200ItemsItem
from .list_working_profiles_response_200 import ListWorkingProfilesResponse200
from .list_working_profiles_response_200_items_item import ListWorkingProfilesResponse200ItemsItem
from .replace_carry_over_body import ReplaceCarryOverBody
from .replace_carry_over_response_200 import ReplaceCarryOverResponse200
from .replace_carry_over_response_200_unit import ReplaceCarryOverResponse200Unit
from .update_booking_body import UpdateBookingBody
from .update_booking_response_200 import UpdateBookingResponse200
from .update_booking_response_200_location_type_0 import UpdateBookingResponse200LocationType0
from .update_person_body import UpdatePersonBody
from .update_person_body_free_fields_item import UpdatePersonBodyFreeFieldsItem
from .update_person_body_sex import UpdatePersonBodySex
from .update_person_body_time_recording import UpdatePersonBodyTimeRecording
from .update_person_response_200 import UpdatePersonResponse200
from .update_person_response_200_au_period_days import UpdatePersonResponse200AuPeriodDays
from .update_person_response_200_external_logins import UpdatePersonResponse200ExternalLogins
from .update_person_response_200_free_fields_item import UpdatePersonResponse200FreeFieldsItem
from .update_person_response_200_free_fields_item_lookup_type_0_item import (
    UpdatePersonResponse200FreeFieldsItemLookupType0Item,
)
from .update_person_response_200_free_licences import UpdatePersonResponse200FreeLicences
from .update_person_response_200_modules import UpdatePersonResponse200Modules
from .update_person_response_200_time_recording import UpdatePersonResponse200TimeRecording
from .update_person_response_200_time_recording_calculation_templates import (
    UpdatePersonResponse200TimeRecordingCalculationTemplates,
)
from .update_person_response_200_time_recording_holiday import UpdatePersonResponse200TimeRecordingHoliday
from .update_person_response_200_time_recording_supervisors_item import (
    UpdatePersonResponse200TimeRecordingSupervisorsItem,
)
from .update_person_response_200_time_recording_working_profile import (
    UpdatePersonResponse200TimeRecordingWorkingProfile,
)
from .update_work_operation_body import UpdateWorkOperationBody
from .update_work_operation_response_200 import UpdateWorkOperationResponse200
from .update_work_operation_response_200_free_fields_item import UpdateWorkOperationResponse200FreeFieldsItem
from .update_work_operation_response_200_free_fields_item_lookup_type_0_item import (
    UpdateWorkOperationResponse200FreeFieldsItemLookupType0Item,
)
from .upsert_person_by_person_no_body import UpsertPersonByPersonNoBody
from .upsert_person_by_person_no_body_free_fields_item import UpsertPersonByPersonNoBodyFreeFieldsItem
from .upsert_person_by_person_no_body_sex import UpsertPersonByPersonNoBodySex
from .upsert_person_by_person_no_body_time_recording import UpsertPersonByPersonNoBodyTimeRecording
from .upsert_person_by_person_no_response_200 import UpsertPersonByPersonNoResponse200
from .upsert_person_by_person_no_response_200_au_period_days import UpsertPersonByPersonNoResponse200AuPeriodDays
from .upsert_person_by_person_no_response_200_external_logins import UpsertPersonByPersonNoResponse200ExternalLogins
from .upsert_person_by_person_no_response_200_free_fields_item import UpsertPersonByPersonNoResponse200FreeFieldsItem
from .upsert_person_by_person_no_response_200_free_fields_item_lookup_type_0_item import (
    UpsertPersonByPersonNoResponse200FreeFieldsItemLookupType0Item,
)
from .upsert_person_by_person_no_response_200_free_licences import UpsertPersonByPersonNoResponse200FreeLicences
from .upsert_person_by_person_no_response_200_modules import UpsertPersonByPersonNoResponse200Modules
from .upsert_person_by_person_no_response_200_time_recording import UpsertPersonByPersonNoResponse200TimeRecording
from .upsert_person_by_person_no_response_200_time_recording_calculation_templates import (
    UpsertPersonByPersonNoResponse200TimeRecordingCalculationTemplates,
)
from .upsert_person_by_person_no_response_200_time_recording_holiday import (
    UpsertPersonByPersonNoResponse200TimeRecordingHoliday,
)
from .upsert_person_by_person_no_response_200_time_recording_supervisors_item import (
    UpsertPersonByPersonNoResponse200TimeRecordingSupervisorsItem,
)
from .upsert_person_by_person_no_response_200_time_recording_working_profile import (
    UpsertPersonByPersonNoResponse200TimeRecordingWorkingProfile,
)
from .upsert_person_by_person_no_response_201 import UpsertPersonByPersonNoResponse201
from .upsert_person_by_person_no_response_201_au_period_days import UpsertPersonByPersonNoResponse201AuPeriodDays
from .upsert_person_by_person_no_response_201_external_logins import UpsertPersonByPersonNoResponse201ExternalLogins
from .upsert_person_by_person_no_response_201_free_fields_item import UpsertPersonByPersonNoResponse201FreeFieldsItem
from .upsert_person_by_person_no_response_201_free_fields_item_lookup_type_0_item import (
    UpsertPersonByPersonNoResponse201FreeFieldsItemLookupType0Item,
)
from .upsert_person_by_person_no_response_201_free_licences import UpsertPersonByPersonNoResponse201FreeLicences
from .upsert_person_by_person_no_response_201_modules import UpsertPersonByPersonNoResponse201Modules
from .upsert_person_by_person_no_response_201_time_recording import UpsertPersonByPersonNoResponse201TimeRecording
from .upsert_person_by_person_no_response_201_time_recording_calculation_templates import (
    UpsertPersonByPersonNoResponse201TimeRecordingCalculationTemplates,
)
from .upsert_person_by_person_no_response_201_time_recording_holiday import (
    UpsertPersonByPersonNoResponse201TimeRecordingHoliday,
)
from .upsert_person_by_person_no_response_201_time_recording_supervisors_item import (
    UpsertPersonByPersonNoResponse201TimeRecordingSupervisorsItem,
)
from .upsert_person_by_person_no_response_201_time_recording_working_profile import (
    UpsertPersonByPersonNoResponse201TimeRecordingWorkingProfile,
)

__all__ = (
    "AssignWorkingProfileBody",
    "AssignWorkingProfileResponse201",
    "CreateAbsenceBookingBody",
    "CreateAbsenceBookingBodyWeekdaysItem",
    "CreateAbsenceBookingResponse201",
    "CreateBookingBody",
    "CreateBookingBodyLocation",
    "CreateBookingBodyType",
    "CreateBookingResponse201",
    "CreateBookingResponse201BookingType0",
    "CreateBookingResponse201BookingType0LocationType0",
    "CreateCarryOverBody",
    "CreateCarryOverResponse201",
    "CreateCarryOverResponse201Unit",
    "CreatePersonBody",
    "CreatePersonBodyFreeFieldsItem",
    "CreatePersonBodySex",
    "CreatePersonBodyTimeRecording",
    "CreatePersonResponse201",
    "CreatePersonResponse201AuPeriodDays",
    "CreatePersonResponse201ExternalLogins",
    "CreatePersonResponse201FreeFieldsItem",
    "CreatePersonResponse201FreeFieldsItemLookupType0Item",
    "CreatePersonResponse201FreeLicences",
    "CreatePersonResponse201Modules",
    "CreatePersonResponse201TimeRecording",
    "CreatePersonResponse201TimeRecordingCalculationTemplates",
    "CreatePersonResponse201TimeRecordingHoliday",
    "CreatePersonResponse201TimeRecordingSupervisorsItem",
    "CreatePersonResponse201TimeRecordingWorkingProfile",
    "CreateWorkOperationBody",
    "CreateWorkOperationResponse201",
    "CreateWorkOperationResponse201FreeFieldsItem",
    "CreateWorkOperationResponse201FreeFieldsItemLookupType0Item",
    "GetAbsenceOverviewResponse200",
    "GetAbsenceOverviewResponse200ItemsItem",
    "GetAbsenceOverviewResponse200ItemsItemDaysItem",
    "GetAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem",
    "GetAbsenceTypeResponse200",
    "GetAbsenceTypeResponse200FreeFieldsItem",
    "GetAbsenceTypeResponse200FreeFieldsItemLookupType0Item",
    "GetAuditEventResponse200",
    "GetAuditEventResponse200Action",
    "GetAuditEventResponse200Outcome",
    "GetAuditEventResponse200Query",
    "GetAuditEventResponse200UpstreamCallsItem",
    "GetBookingResponse200",
    "GetBookingResponse200LocationType0",
    "GetBreakRuleResponse200",
    "GetDailyBalanceResponse200",
    "GetDailyBalanceResponse200AbsencesItem",
    "GetDailyBalanceResponse200BookingTimeRange",
    "GetDailyBalanceResponse200CalculationsItem",
    "GetDailyBalanceResponse200CalculationsItemUnit",
    "GetDailyBalanceResponse200CarryOversItem",
    "GetDailyBalanceResponse200CarryOversItemKind",
    "GetDailyBalanceResponse200CarryOversItemUnit",
    "GetDailyBalanceResponse200EvaluationChanged",
    "GetDailyBalanceResponse200ProjectsItem",
    "GetDailyBalanceResponse200WorkingProfile",
    "GetDepartmentResponse200",
    "GetDepartmentResponse200FreeFieldsItem",
    "GetDepartmentResponse200FreeFieldsItemLookupType0Item",
    "GetDepartmentResponse200Kind",
    "GetDepartmentResponse200TimeRecordingType0",
    "GetFreeFieldResponse200",
    "GetFreeFieldResponse200LookupType0Item",
    "GetGroupResponse200",
    "GetGroupResponse200FreeFieldsItem",
    "GetGroupResponse200FreeFieldsItemLookupType0Item",
    "GetGroupResponse200Kind",
    "GetGroupResponse200TimeRecordingType0",
    "GetHealthResponse200",
    "GetHealthResponse200AuditDb",
    "GetHealthResponse200Status",
    "GetHealthResponse200Timecard",
    "GetHealthResponse503",
    "GetHealthResponse503AuditDb",
    "GetHealthResponse503Status",
    "GetHealthResponse503Timecard",
    "GetMeResponse200",
    "GetPersonAbsenceOverviewResponse200",
    "GetPersonAbsenceOverviewResponse200ItemsItem",
    "GetPersonAbsenceOverviewResponse200ItemsItemDaysItem",
    "GetPersonAbsenceOverviewResponse200ItemsItemDaysItemEntriesItem",
    "GetPersonByPersonNoResponse200",
    "GetPersonByPersonNoResponse200AuPeriodDays",
    "GetPersonByPersonNoResponse200ExternalLogins",
    "GetPersonByPersonNoResponse200FreeFieldsItem",
    "GetPersonByPersonNoResponse200FreeFieldsItemLookupType0Item",
    "GetPersonByPersonNoResponse200FreeLicences",
    "GetPersonByPersonNoResponse200Modules",
    "GetPersonByPersonNoResponse200TimeRecording",
    "GetPersonByPersonNoResponse200TimeRecordingCalculationTemplates",
    "GetPersonByPersonNoResponse200TimeRecordingHoliday",
    "GetPersonByPersonNoResponse200TimeRecordingSupervisorsItem",
    "GetPersonByPersonNoResponse200TimeRecordingWorkingProfile",
    "GetPersonCalendarResponse200",
    "GetPersonCalendarResponse200AbsentDaysItem",
    "GetPersonCalendarResponse200PublicHolidaysItem",
    "GetPersonCalendarResponse200SickDays",
    "GetPersonCalendarResponse200SickDaysCertificateAvailableItem",
    "GetPersonCalendarResponse200SickDaysCertificateMissingItem",
    "GetPersonCalendarResponse200SickDaysCertificateNotRequiredItem",
    "GetPersonResponse200",
    "GetPersonResponse200AuPeriodDays",
    "GetPersonResponse200ExternalLogins",
    "GetPersonResponse200FreeFieldsItem",
    "GetPersonResponse200FreeFieldsItemLookupType0Item",
    "GetPersonResponse200FreeLicences",
    "GetPersonResponse200Modules",
    "GetPersonResponse200TimeRecording",
    "GetPersonResponse200TimeRecordingCalculationTemplates",
    "GetPersonResponse200TimeRecordingHoliday",
    "GetPersonResponse200TimeRecordingSupervisorsItem",
    "GetPersonResponse200TimeRecordingWorkingProfile",
    "GetProjectResponse200",
    "GetProjectResponse200FreeFieldsItem",
    "GetProjectResponse200FreeFieldsItemLookupType0Item",
    "GetVersionResponse200",
    "GetWorkingProfileResponse200",
    "GetWorkingProfileResponse200FreeFieldsItem",
    "GetWorkingProfileResponse200FreeFieldsItemLookupType0Item",
    "GetWorkingProfileResponse200WorkingDaysItem",
    "GetWorkingProfileResponse200WorkingDaysItemCoreTime2Type0",
    "GetWorkingProfileResponse200WorkingDaysItemCoreTimeType0",
    "GetWorkingProfileResponse200WorkingDaysItemEvaluatedTimeType0",
    "GetWorkingProfileResponse200WorkingDaysItemPermittedTimeType0",
    "GetWorkOperationResponse200",
    "GetWorkOperationResponse200FreeFieldsItem",
    "GetWorkOperationResponse200FreeFieldsItemLookupType0Item",
    "ListAbsenceTypesResponse200",
    "ListAbsenceTypesResponse200ItemsItem",
    "ListAbsenceTypesUsage",
    "ListAllowedProjectsResponse200",
    "ListAllowedProjectsResponse200ItemsItem",
    "ListAuditEventsAction",
    "ListAuditEventsFormat",
    "ListAuditEventsOutcome",
    "ListAuditEventsResponse200",
    "ListAuditEventsResponse200ItemsItem",
    "ListAuditEventsResponse200ItemsItemAction",
    "ListAuditEventsResponse200ItemsItemOutcome",
    "ListAuditEventsResponse200ItemsItemQuery",
    "ListAuditEventsResponse200ItemsItemUpstreamCallsItem",
    "ListBookingsResponse200",
    "ListBookingsResponse200ItemsItem",
    "ListBreakRulesResponse200",
    "ListBreakRulesResponse200ItemsItem",
    "ListCalculationAccountsResponse200",
    "ListCalculationAccountsResponse200ItemsItem",
    "ListCalculationAccountsResponse200ItemsItemUnit",
    "ListCalculationTemplatesResponse200",
    "ListCalculationTemplatesResponse200ItemsItem",
    "ListCarryOversResponse200",
    "ListCarryOversResponse200ItemsItem",
    "ListCarryOversResponse200ItemsItemUnit",
    "ListDepartmentMembersResponse200",
    "ListDepartmentMembersResponse200ItemsItem",
    "ListDepartmentMembersResponse200ItemsItemState",
    "ListDepartmentsResponse200",
    "ListDepartmentsResponse200ItemsItem",
    "ListFreeFieldsResponse200",
    "ListFreeFieldsResponse200ItemsItem",
    "ListGroupMembersResponse200",
    "ListGroupMembersResponse200ItemsItem",
    "ListGroupMembersResponse200ItemsItemState",
    "ListGroupsResponse200",
    "ListGroupsResponse200ItemsItem",
    "ListPersonBookingsResponse200",
    "ListPersonBookingsResponse200ItemsItem",
    "ListPersonsResponse200",
    "ListPersonsResponse200ItemsItem",
    "ListPersonsResponse200ItemsItemState",
    "ListPersonsState",
    "ListPresenceResponse200",
    "ListPresenceResponse200ItemsItem",
    "ListPresenceResponse200ItemsItemStatus",
    "ListProjectsResponse200",
    "ListProjectsResponse200ItemsItem",
    "ListProjectWorkOperationsResponse200",
    "ListProjectWorkOperationsResponse200ItemsItem",
    "ListWorkingProfilesResponse200",
    "ListWorkingProfilesResponse200ItemsItem",
    "ListWorkOperationsResponse200",
    "ListWorkOperationsResponse200ItemsItem",
    "ReplaceCarryOverBody",
    "ReplaceCarryOverResponse200",
    "ReplaceCarryOverResponse200Unit",
    "UpdateBookingBody",
    "UpdateBookingResponse200",
    "UpdateBookingResponse200LocationType0",
    "UpdatePersonBody",
    "UpdatePersonBodyFreeFieldsItem",
    "UpdatePersonBodySex",
    "UpdatePersonBodyTimeRecording",
    "UpdatePersonResponse200",
    "UpdatePersonResponse200AuPeriodDays",
    "UpdatePersonResponse200ExternalLogins",
    "UpdatePersonResponse200FreeFieldsItem",
    "UpdatePersonResponse200FreeFieldsItemLookupType0Item",
    "UpdatePersonResponse200FreeLicences",
    "UpdatePersonResponse200Modules",
    "UpdatePersonResponse200TimeRecording",
    "UpdatePersonResponse200TimeRecordingCalculationTemplates",
    "UpdatePersonResponse200TimeRecordingHoliday",
    "UpdatePersonResponse200TimeRecordingSupervisorsItem",
    "UpdatePersonResponse200TimeRecordingWorkingProfile",
    "UpdateWorkOperationBody",
    "UpdateWorkOperationResponse200",
    "UpdateWorkOperationResponse200FreeFieldsItem",
    "UpdateWorkOperationResponse200FreeFieldsItemLookupType0Item",
    "UpsertPersonByPersonNoBody",
    "UpsertPersonByPersonNoBodyFreeFieldsItem",
    "UpsertPersonByPersonNoBodySex",
    "UpsertPersonByPersonNoBodyTimeRecording",
    "UpsertPersonByPersonNoResponse200",
    "UpsertPersonByPersonNoResponse200AuPeriodDays",
    "UpsertPersonByPersonNoResponse200ExternalLogins",
    "UpsertPersonByPersonNoResponse200FreeFieldsItem",
    "UpsertPersonByPersonNoResponse200FreeFieldsItemLookupType0Item",
    "UpsertPersonByPersonNoResponse200FreeLicences",
    "UpsertPersonByPersonNoResponse200Modules",
    "UpsertPersonByPersonNoResponse200TimeRecording",
    "UpsertPersonByPersonNoResponse200TimeRecordingCalculationTemplates",
    "UpsertPersonByPersonNoResponse200TimeRecordingHoliday",
    "UpsertPersonByPersonNoResponse200TimeRecordingSupervisorsItem",
    "UpsertPersonByPersonNoResponse200TimeRecordingWorkingProfile",
    "UpsertPersonByPersonNoResponse201",
    "UpsertPersonByPersonNoResponse201AuPeriodDays",
    "UpsertPersonByPersonNoResponse201ExternalLogins",
    "UpsertPersonByPersonNoResponse201FreeFieldsItem",
    "UpsertPersonByPersonNoResponse201FreeFieldsItemLookupType0Item",
    "UpsertPersonByPersonNoResponse201FreeLicences",
    "UpsertPersonByPersonNoResponse201Modules",
    "UpsertPersonByPersonNoResponse201TimeRecording",
    "UpsertPersonByPersonNoResponse201TimeRecordingCalculationTemplates",
    "UpsertPersonByPersonNoResponse201TimeRecordingHoliday",
    "UpsertPersonByPersonNoResponse201TimeRecordingSupervisorsItem",
    "UpsertPersonByPersonNoResponse201TimeRecordingWorkingProfile",
)
