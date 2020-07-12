# -*- coding: utf-8 -*-
# This file is part of Shuup Onboarding Sample
#
# Copyright (c) 2020 Christian Hess
#
# This source code is licensed under the OSL version 3.0 found in the
# LICENSE file in the root directory of this source tree.
from shuup_onboarding.middleware import BaseAdminOnboardingMiddleware


class ExampleAdminOnboardingMiddleware(BaseAdminOnboardingMiddleware):
    onboarding_process_id = "sample_setup"  # we are after this onboarding process id
