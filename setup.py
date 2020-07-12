# -*- coding: utf-8 -*-
# This file is part of Shuup Onboarding Sample
#
# Copyright (c) 2020 Christian Hess
#
# This source code is licensed under the OSL version 3.0 found in the
# LICENSE file in the root directory of this source tree.
import setuptools

try:
    import shuup_setup_utils
except ImportError:
    shuup_setup_utils = None


if __name__ == '__main__':
    setuptools.setup(
        cmdclass=(shuup_setup_utils.COMMANDS if shuup_setup_utils else {}),
        setup_requires=['setuptools>=34.0', 'setuptools-gitver'],
        gitver=True
    )
