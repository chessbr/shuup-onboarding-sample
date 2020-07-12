# -*- coding: utf-8 -*-
# This file is part of Shuup Onboarding Sample
#
# Copyright (c) 2020 Christian Hess
#
# This source code is licensed under the OSL version 3.0 found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_onboarding_sample"
    label = "shuup_onboarding_sample"

    required_installed_apps = [
        "shuup_onboarding"
    ]

    provides = {
        "onboarding_process:sample_setup": [
            "shuup_onboarding_sample.steps.ShopInfo",
            "shuup_onboarding_sample.steps.OwnerPassword",
            "shuup_onboarding_sample.steps.Setup",
        ]
    }
