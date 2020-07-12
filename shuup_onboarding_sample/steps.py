# -*- coding: utf-8 -*-
# This file is part of Shuup Onboarding Sample
#
# Copyright (c) 2020 Christian Hess
#
# This source code is licensed under the OSL version 3.0 found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from shuup import configuration

from shuup_onboarding.base import OnboardingStep


class ShopInfoForm(forms.Form):
    name = forms.CharField(label="Shop name")


class OwnerPassForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class ShopInfo(OnboardingStep):
    identifier = "shop_info"
    title = "Shop Information"
    description = "Enter the information of your shop"
    template_name = "sample/shop_info.jinja"

    def can_skip(self) -> bool:
        return False

    def is_done(self) -> bool:
        return bool(configuration.get(self.context.shop, "step_shop_info"))

    def is_visible(self) -> bool:
        return True

    def get_form(self, **kwargs) -> forms.Form:
        initial = kwargs.get("initial", {})
        if not initial.get("name"):
            initial["name"] = self.context.storage.get("shop_name")
        kwargs["initial"] = initial

        return ShopInfoForm(**kwargs)

    def save(self, form):
        self.context.storage["shop_name"] = form.cleaned_data["name"]

        # mark as done
        configuration.set(self.context.shop, "step_shop_info", True)

    def undo(self):
        configuration.set(self.context.shop, "step_shop_info", False)


class OwnerPassword(OnboardingStep):
    identifier = "owner_password"
    title = "Owner Password"
    description = "Enter the password of the admin user"
    template_name = "sample/owner_pass.jinja"

    def skip(self):
        configuration.set(self.context.shop, "step_owner_pass_skipped", True)

    def can_skip(self) -> bool:
        return True

    def was_skipped(self) -> bool:
        return bool(configuration.get(self.context.shop, "step_owner_pass_skipped"))

    def is_visible(self) -> bool:
        return True

    def get_form(self, **kwargs) -> forms.Form:
        return OwnerPassForm(**kwargs)

    def is_done(self) -> bool:
        return bool(configuration.get(self.context.shop, "step_owner_pass"))

    def save(self, form):
        self.context.storage["owner_pass"] = form.cleaned_data["password"]

        # mark as done
        configuration.set(self.context.shop, "step_owner_pass", True)

    def undo(self):
        configuration.set(self.context.shop, "step_owner_pass_skipped", False)
        configuration.set(self.context.shop, "step_owner_pass", False)


class Setup(OnboardingStep):
    identifier = "setup"
    title = "Setup instance"
    description = "Click on finish to finish yout setup"
    template_name = "sample/setup.jinja"

    def can_skip(self) -> bool:
        return False

    def is_visible(self) -> bool:
        return True

    def get_form(self, **kwargs) -> forms.Form:
        return forms.Form(**kwargs)

    def is_done(self) -> bool:
        return bool(configuration.get(self.context.shop, "step_setup"))

    def save(self, form):
        if self.context.storage.get("owner_pass"):
            self.context.user.set_password(self.context.storage["owner_pass"])
            self.context.user.save()

        # mark as done
        configuration.set(self.context.shop, "step_setup", True)

    def undo(self):
        configuration.set(self.context.shop, "step_setup", False)
