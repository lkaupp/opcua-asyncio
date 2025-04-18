#AUTOGENERATED!!! Date: 2025-03-31 11:51:57.540484+00:00

from asyncua.ua.uaerrors import UaStatusCodeError


class Bad(UaStatusCodeError):
    code = 0x80000000


class BadUnexpectedError(UaStatusCodeError):
    code = 0x80010000


class BadInternalError(UaStatusCodeError):
    code = 0x80020000


class BadOutOfMemory(UaStatusCodeError):
    code = 0x80030000


class BadResourceUnavailable(UaStatusCodeError):
    code = 0x80040000


class BadCommunicationError(UaStatusCodeError):
    code = 0x80050000


class BadEncodingError(UaStatusCodeError):
    code = 0x80060000


class BadDecodingError(UaStatusCodeError):
    code = 0x80070000


class BadEncodingLimitsExceeded(UaStatusCodeError):
    code = 0x80080000


class BadRequestTooLarge(UaStatusCodeError):
    code = 0x80B80000


class BadResponseTooLarge(UaStatusCodeError):
    code = 0x80B90000


class BadUnknownResponse(UaStatusCodeError):
    code = 0x80090000


class BadTimeout(UaStatusCodeError):
    code = 0x800A0000


class BadServiceUnsupported(UaStatusCodeError):
    code = 0x800B0000


class BadShutdown(UaStatusCodeError):
    code = 0x800C0000


class BadServerNotConnected(UaStatusCodeError):
    code = 0x800D0000


class BadServerHalted(UaStatusCodeError):
    code = 0x800E0000


class BadNothingToDo(UaStatusCodeError):
    code = 0x800F0000


class BadTooManyOperations(UaStatusCodeError):
    code = 0x80100000


class BadTooManyMonitoredItems(UaStatusCodeError):
    code = 0x80DB0000


class BadDataTypeIdUnknown(UaStatusCodeError):
    code = 0x80110000


class BadCertificateInvalid(UaStatusCodeError):
    code = 0x80120000


class BadSecurityChecksFailed(UaStatusCodeError):
    code = 0x80130000


class BadCertificatePolicyCheckFailed(UaStatusCodeError):
    code = 0x81140000


class BadCertificateTimeInvalid(UaStatusCodeError):
    code = 0x80140000


class BadCertificateIssuerTimeInvalid(UaStatusCodeError):
    code = 0x80150000


class BadCertificateHostNameInvalid(UaStatusCodeError):
    code = 0x80160000


class BadCertificateUriInvalid(UaStatusCodeError):
    code = 0x80170000


class BadCertificateUseNotAllowed(UaStatusCodeError):
    code = 0x80180000


class BadCertificateIssuerUseNotAllowed(UaStatusCodeError):
    code = 0x80190000


class BadCertificateUntrusted(UaStatusCodeError):
    code = 0x801A0000


class BadCertificateRevocationUnknown(UaStatusCodeError):
    code = 0x801B0000


class BadCertificateIssuerRevocationUnknown(UaStatusCodeError):
    code = 0x801C0000


class BadCertificateRevoked(UaStatusCodeError):
    code = 0x801D0000


class BadCertificateIssuerRevoked(UaStatusCodeError):
    code = 0x801E0000


class BadCertificateChainIncomplete(UaStatusCodeError):
    code = 0x810D0000


class BadUserAccessDenied(UaStatusCodeError):
    code = 0x801F0000


class BadIdentityTokenInvalid(UaStatusCodeError):
    code = 0x80200000


class BadIdentityTokenRejected(UaStatusCodeError):
    code = 0x80210000


class BadSecureChannelIdInvalid(UaStatusCodeError):
    code = 0x80220000


class BadInvalidTimestamp(UaStatusCodeError):
    code = 0x80230000


class BadNonceInvalid(UaStatusCodeError):
    code = 0x80240000


class BadSessionIdInvalid(UaStatusCodeError):
    code = 0x80250000


class BadSessionClosed(UaStatusCodeError):
    code = 0x80260000


class BadSessionNotActivated(UaStatusCodeError):
    code = 0x80270000


class BadSubscriptionIdInvalid(UaStatusCodeError):
    code = 0x80280000


class BadRequestHeaderInvalid(UaStatusCodeError):
    code = 0x802A0000


class BadTimestampsToReturnInvalid(UaStatusCodeError):
    code = 0x802B0000


class BadRequestCancelledByClient(UaStatusCodeError):
    code = 0x802C0000


class BadTooManyArguments(UaStatusCodeError):
    code = 0x80E50000


class BadLicenseExpired(UaStatusCodeError):
    code = 0x810E0000


class BadLicenseLimitsExceeded(UaStatusCodeError):
    code = 0x810F0000


class BadLicenseNotAvailable(UaStatusCodeError):
    code = 0x81100000


class BadServerTooBusy(UaStatusCodeError):
    code = 0x80EE0000


class BadNoCommunication(UaStatusCodeError):
    code = 0x80310000


class BadWaitingForInitialData(UaStatusCodeError):
    code = 0x80320000


class BadNodeIdInvalid(UaStatusCodeError):
    code = 0x80330000


class BadNodeIdUnknown(UaStatusCodeError):
    code = 0x80340000


class BadAttributeIdInvalid(UaStatusCodeError):
    code = 0x80350000


class BadIndexRangeInvalid(UaStatusCodeError):
    code = 0x80360000


class BadIndexRangeNoData(UaStatusCodeError):
    code = 0x80370000


class BadIndexRangeDataMismatch(UaStatusCodeError):
    code = 0x80EA0000


class BadDataEncodingInvalid(UaStatusCodeError):
    code = 0x80380000


class BadDataEncodingUnsupported(UaStatusCodeError):
    code = 0x80390000


class BadNotReadable(UaStatusCodeError):
    code = 0x803A0000


class BadNotWritable(UaStatusCodeError):
    code = 0x803B0000


class BadOutOfRange(UaStatusCodeError):
    code = 0x803C0000


class BadNotSupported(UaStatusCodeError):
    code = 0x803D0000


class BadNotFound(UaStatusCodeError):
    code = 0x803E0000


class BadObjectDeleted(UaStatusCodeError):
    code = 0x803F0000


class BadNotImplemented(UaStatusCodeError):
    code = 0x80400000


class BadMonitoringModeInvalid(UaStatusCodeError):
    code = 0x80410000


class BadMonitoredItemIdInvalid(UaStatusCodeError):
    code = 0x80420000


class BadMonitoredItemFilterInvalid(UaStatusCodeError):
    code = 0x80430000


class BadMonitoredItemFilterUnsupported(UaStatusCodeError):
    code = 0x80440000


class BadFilterNotAllowed(UaStatusCodeError):
    code = 0x80450000


class BadStructureMissing(UaStatusCodeError):
    code = 0x80460000


class BadEventFilterInvalid(UaStatusCodeError):
    code = 0x80470000


class BadContentFilterInvalid(UaStatusCodeError):
    code = 0x80480000


class BadFilterOperatorInvalid(UaStatusCodeError):
    code = 0x80C10000


class BadFilterOperatorUnsupported(UaStatusCodeError):
    code = 0x80C20000


class BadFilterOperandCountMismatch(UaStatusCodeError):
    code = 0x80C30000


class BadFilterOperandInvalid(UaStatusCodeError):
    code = 0x80490000


class BadFilterElementInvalid(UaStatusCodeError):
    code = 0x80C40000


class BadFilterLiteralInvalid(UaStatusCodeError):
    code = 0x80C50000


class BadContinuationPointInvalid(UaStatusCodeError):
    code = 0x804A0000


class BadNoContinuationPoints(UaStatusCodeError):
    code = 0x804B0000


class BadReferenceTypeIdInvalid(UaStatusCodeError):
    code = 0x804C0000


class BadBrowseDirectionInvalid(UaStatusCodeError):
    code = 0x804D0000


class BadNodeNotInView(UaStatusCodeError):
    code = 0x804E0000


class BadNumericOverflow(UaStatusCodeError):
    code = 0x81120000


class BadLocaleNotSupported(UaStatusCodeError):
    code = 0x80ED0000


class BadNoValue(UaStatusCodeError):
    code = 0x80F00000


class BadServerUriInvalid(UaStatusCodeError):
    code = 0x804F0000


class BadServerNameMissing(UaStatusCodeError):
    code = 0x80500000


class BadDiscoveryUrlMissing(UaStatusCodeError):
    code = 0x80510000


class BadSemaphoreFileMissing(UaStatusCodeError):
    code = 0x80520000


class BadRequestTypeInvalid(UaStatusCodeError):
    code = 0x80530000


class BadSecurityModeRejected(UaStatusCodeError):
    code = 0x80540000


class BadSecurityPolicyRejected(UaStatusCodeError):
    code = 0x80550000


class BadTooManySessions(UaStatusCodeError):
    code = 0x80560000


class BadUserSignatureInvalid(UaStatusCodeError):
    code = 0x80570000


class BadApplicationSignatureInvalid(UaStatusCodeError):
    code = 0x80580000


class BadNoValidCertificates(UaStatusCodeError):
    code = 0x80590000


class BadIdentityChangeNotSupported(UaStatusCodeError):
    code = 0x80C60000


class BadRequestCancelledByRequest(UaStatusCodeError):
    code = 0x805A0000


class BadParentNodeIdInvalid(UaStatusCodeError):
    code = 0x805B0000


class BadReferenceNotAllowed(UaStatusCodeError):
    code = 0x805C0000


class BadNodeIdRejected(UaStatusCodeError):
    code = 0x805D0000


class BadNodeIdExists(UaStatusCodeError):
    code = 0x805E0000


class BadNodeClassInvalid(UaStatusCodeError):
    code = 0x805F0000


class BadBrowseNameInvalid(UaStatusCodeError):
    code = 0x80600000


class BadBrowseNameDuplicated(UaStatusCodeError):
    code = 0x80610000


class BadNodeAttributesInvalid(UaStatusCodeError):
    code = 0x80620000


class BadTypeDefinitionInvalid(UaStatusCodeError):
    code = 0x80630000


class BadSourceNodeIdInvalid(UaStatusCodeError):
    code = 0x80640000


class BadTargetNodeIdInvalid(UaStatusCodeError):
    code = 0x80650000


class BadDuplicateReferenceNotAllowed(UaStatusCodeError):
    code = 0x80660000


class BadInvalidSelfReference(UaStatusCodeError):
    code = 0x80670000


class BadReferenceLocalOnly(UaStatusCodeError):
    code = 0x80680000


class BadNoDeleteRights(UaStatusCodeError):
    code = 0x80690000


class BadServerIndexInvalid(UaStatusCodeError):
    code = 0x806A0000


class BadViewIdUnknown(UaStatusCodeError):
    code = 0x806B0000


class BadViewTimestampInvalid(UaStatusCodeError):
    code = 0x80C90000


class BadViewParameterMismatch(UaStatusCodeError):
    code = 0x80CA0000


class BadViewVersionInvalid(UaStatusCodeError):
    code = 0x80CB0000


class BadNotTypeDefinition(UaStatusCodeError):
    code = 0x80C80000


class BadTooManyMatches(UaStatusCodeError):
    code = 0x806D0000


class BadQueryTooComplex(UaStatusCodeError):
    code = 0x806E0000


class BadNoMatch(UaStatusCodeError):
    code = 0x806F0000


class BadMaxAgeInvalid(UaStatusCodeError):
    code = 0x80700000


class BadSecurityModeInsufficient(UaStatusCodeError):
    code = 0x80E60000


class BadHistoryOperationInvalid(UaStatusCodeError):
    code = 0x80710000


class BadHistoryOperationUnsupported(UaStatusCodeError):
    code = 0x80720000


class BadInvalidTimestampArgument(UaStatusCodeError):
    code = 0x80BD0000


class BadWriteNotSupported(UaStatusCodeError):
    code = 0x80730000


class BadTypeMismatch(UaStatusCodeError):
    code = 0x80740000


class BadMethodInvalid(UaStatusCodeError):
    code = 0x80750000


class BadArgumentsMissing(UaStatusCodeError):
    code = 0x80760000


class BadNotExecutable(UaStatusCodeError):
    code = 0x81110000


class BadTooManySubscriptions(UaStatusCodeError):
    code = 0x80770000


class BadTooManyPublishRequests(UaStatusCodeError):
    code = 0x80780000


class BadNoSubscription(UaStatusCodeError):
    code = 0x80790000


class BadSequenceNumberUnknown(UaStatusCodeError):
    code = 0x807A0000


class BadMessageNotAvailable(UaStatusCodeError):
    code = 0x807B0000


class BadInsufficientClientProfile(UaStatusCodeError):
    code = 0x807C0000


class BadStateNotActive(UaStatusCodeError):
    code = 0x80BF0000


class BadAlreadyExists(UaStatusCodeError):
    code = 0x81150000


class BadTcpServerTooBusy(UaStatusCodeError):
    code = 0x807D0000


class BadTcpMessageTypeInvalid(UaStatusCodeError):
    code = 0x807E0000


class BadTcpSecureChannelUnknown(UaStatusCodeError):
    code = 0x807F0000


class BadTcpMessageTooLarge(UaStatusCodeError):
    code = 0x80800000


class BadTcpNotEnoughResources(UaStatusCodeError):
    code = 0x80810000


class BadTcpInternalError(UaStatusCodeError):
    code = 0x80820000


class BadTcpEndpointUrlInvalid(UaStatusCodeError):
    code = 0x80830000


class BadRequestInterrupted(UaStatusCodeError):
    code = 0x80840000


class BadRequestTimeout(UaStatusCodeError):
    code = 0x80850000


class BadSecureChannelClosed(UaStatusCodeError):
    code = 0x80860000


class BadSecureChannelTokenUnknown(UaStatusCodeError):
    code = 0x80870000


class BadSequenceNumberInvalid(UaStatusCodeError):
    code = 0x80880000


class BadProtocolVersionUnsupported(UaStatusCodeError):
    code = 0x80BE0000


class BadConfigurationError(UaStatusCodeError):
    code = 0x80890000


class BadNotConnected(UaStatusCodeError):
    code = 0x808A0000


class BadDeviceFailure(UaStatusCodeError):
    code = 0x808B0000


class BadSensorFailure(UaStatusCodeError):
    code = 0x808C0000


class BadOutOfService(UaStatusCodeError):
    code = 0x808D0000


class BadDeadbandFilterInvalid(UaStatusCodeError):
    code = 0x808E0000


class BadRefreshInProgress(UaStatusCodeError):
    code = 0x80970000


class BadConditionAlreadyDisabled(UaStatusCodeError):
    code = 0x80980000


class BadConditionAlreadyEnabled(UaStatusCodeError):
    code = 0x80CC0000


class BadConditionDisabled(UaStatusCodeError):
    code = 0x80990000


class BadEventIdUnknown(UaStatusCodeError):
    code = 0x809A0000


class BadEventNotAcknowledgeable(UaStatusCodeError):
    code = 0x80BB0000


class BadDialogNotActive(UaStatusCodeError):
    code = 0x80CD0000


class BadDialogResponseInvalid(UaStatusCodeError):
    code = 0x80CE0000


class BadConditionBranchAlreadyAcked(UaStatusCodeError):
    code = 0x80CF0000


class BadConditionBranchAlreadyConfirmed(UaStatusCodeError):
    code = 0x80D00000


class BadConditionAlreadyShelved(UaStatusCodeError):
    code = 0x80D10000


class BadConditionNotShelved(UaStatusCodeError):
    code = 0x80D20000


class BadShelvingTimeOutOfRange(UaStatusCodeError):
    code = 0x80D30000


class BadNoData(UaStatusCodeError):
    code = 0x809B0000


class BadBoundNotFound(UaStatusCodeError):
    code = 0x80D70000


class BadBoundNotSupported(UaStatusCodeError):
    code = 0x80D80000


class BadDataLost(UaStatusCodeError):
    code = 0x809D0000


class BadDataUnavailable(UaStatusCodeError):
    code = 0x809E0000


class BadEntryExists(UaStatusCodeError):
    code = 0x809F0000


class BadNoEntryExists(UaStatusCodeError):
    code = 0x80A00000


class BadTimestampNotSupported(UaStatusCodeError):
    code = 0x80A10000


class BadAggregateListMismatch(UaStatusCodeError):
    code = 0x80D40000


class BadAggregateNotSupported(UaStatusCodeError):
    code = 0x80D50000


class BadAggregateInvalidInputs(UaStatusCodeError):
    code = 0x80D60000


class BadAggregateConfigurationRejected(UaStatusCodeError):
    code = 0x80DA0000


class BadRequestNotAllowed(UaStatusCodeError):
    code = 0x80E40000


class BadRequestNotComplete(UaStatusCodeError):
    code = 0x81130000


class BadTransactionPending(UaStatusCodeError):
    code = 0x80E80000


class BadTicketRequired(UaStatusCodeError):
    code = 0x811F0000


class BadTicketInvalid(UaStatusCodeError):
    code = 0x81200000


class BadLocked(UaStatusCodeError):
    code = 0x80E90000


class BadRequiresLock(UaStatusCodeError):
    code = 0x80EC0000


class BadDominantValueChanged(UaStatusCodeError):
    code = 0x80E10000


class BadDependentValueChanged(UaStatusCodeError):
    code = 0x80E30000


class BadEdited_OutOfRange(UaStatusCodeError):
    code = 0x81190000


class BadInitialValue_OutOfRange(UaStatusCodeError):
    code = 0x811A0000


class BadOutOfRange_DominantValueChanged(UaStatusCodeError):
    code = 0x811B0000


class BadEdited_OutOfRange_DominantValueChanged(UaStatusCodeError):
    code = 0x811C0000


class BadOutOfRange_DominantValueChanged_DependentValueChanged(UaStatusCodeError):
    code = 0x811D0000


class BadEdited_OutOfRange_DominantValueChanged_DependentValueChanged(UaStatusCodeError):
    code = 0x811E0000


class BadInvalidArgument(UaStatusCodeError):
    code = 0x80AB0000


class BadConnectionRejected(UaStatusCodeError):
    code = 0x80AC0000


class BadDisconnect(UaStatusCodeError):
    code = 0x80AD0000


class BadConnectionClosed(UaStatusCodeError):
    code = 0x80AE0000


class BadInvalidState(UaStatusCodeError):
    code = 0x80AF0000


class BadEndOfStream(UaStatusCodeError):
    code = 0x80B00000


class BadNoDataAvailable(UaStatusCodeError):
    code = 0x80B10000


class BadWaitingForResponse(UaStatusCodeError):
    code = 0x80B20000


class BadOperationAbandoned(UaStatusCodeError):
    code = 0x80B30000


class BadExpectedStreamToBlock(UaStatusCodeError):
    code = 0x80B40000


class BadWouldBlock(UaStatusCodeError):
    code = 0x80B50000


class BadSyntaxError(UaStatusCodeError):
    code = 0x80B60000


class BadMaxConnectionsReached(UaStatusCodeError):
    code = 0x80B70000


class BadDataSetIdInvalid(UaStatusCodeError):
    code = 0x80E70000
