# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, Final, List

from . import Tag

_NAMESPACE = "AWS::Macie"

class CustomDataIdentifier:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html"""

    Id: Final[str]

    Arn: Final[str]

    CreatedAt: Final[str]

    Deleted: Final[bool]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Regex: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        IgnoreWords: List[str] = ...,
        Keywords: List[str] = ...,
        MaximumMatchDistance: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class FindingsFilter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html"""

    Id: Final[str]

    Arn: Final[str]

    FindingsFilterListItems: Final[List]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FindingCriteria: "FindingsFilter.FindingCriteria",
        Name: str,
        Action: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Position: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Criterion:
        def __init__(self) -> None: ...
    class FindingCriteria:
        def __init__(self, *, Criterion: "FindingsFilter.Criterion" = ...): ...
    class FindingsFilterListItem:
        def __init__(self, *, Id: str = ..., Name: str = ...): ...

class Session:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html"""

    AwsAccountId: Final[str]

    ServiceRole: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FindingPublishingFrequency: str = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
