# -*- encoding: utf-8 -*-

# Copyright (c) 2023-2024 Huawei Cloud Computing Technology Co., Ltd. All rights reserved.
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

from __future__ import absolute_import
from typing import List

from iot_device_sdk_python.gateway.requests.del_sub_device_failed_reason import DelSubDeviceFailedReason


class GtwDelSubDeviceRsp:
    def __init__(self):
        self._successful_devices: List[str] = []
        self._failed_devices: List[DelSubDeviceFailedReason] = []

    @property
    def successful_devices(self):
        return self._successful_devices

    @successful_devices.setter
    def successful_devices(self, value):
        self._successful_devices = value

    @property
    def failed_devices(self):
        return self._failed_devices

    @failed_devices.setter
    def failed_devices(self, value):
        self._failed_devices = value

    def to_dict(self):
        return {"successful_devices": self._successful_devices,
                "failed_devices": self._failed_devices}















