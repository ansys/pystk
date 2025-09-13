# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from test_util import *
from assertion_harness import *
from ansys.stk.core.stkobjects import *


class ChainAnalysisOptionsHelper(object):

    # region Run Method
    def Run(self, oChainAnalysisOptions: "ChainAnalysisOptions", isTransmitter: bool):
        # Processing Delay Time
        Assert.assertIsNotNone(oChainAnalysisOptions)
        originalProcessingDelayTime: float = oChainAnalysisOptions.processing_delay_time

        oChainAnalysisOptions.processing_delay_time = 0
        Assert.assertEqual(0, oChainAnalysisOptions.processing_delay_time)

        oChainAnalysisOptions.processing_delay_time = 5.5
        Assert.assertEqual(5.5, oChainAnalysisOptions.processing_delay_time)

        oChainAnalysisOptions.processing_delay_time = Double.PositiveInfinity
        Assert.assertEqual(Double.PositiveInfinity, oChainAnalysisOptions.processing_delay_time)

        # Cannot set negative value
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oChainAnalysisOptions.processing_delay_time = -1

        # Reset
        oChainAnalysisOptions.processing_delay_time = originalProcessingDelayTime
        if isTransmitter == False:
            originalDataRate: float = oChainAnalysisOptions.data_rate

            oChainAnalysisOptions.data_rate = 1.13
            Assert.assertEqual(1.13, oChainAnalysisOptions.data_rate)

            oChainAnalysisOptions.data_rate = 33.98
            Assert.assertEqual(33.98, oChainAnalysisOptions.data_rate)

            # Cannot set negative or too large of a value
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                oChainAnalysisOptions.data_rate = Double.PositiveInfinity
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                oChainAnalysisOptions.data_rate = -1

            # Reset
            oChainAnalysisOptions.data_rate = originalDataRate

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oChainAnalysisOptions.data_rate = 1000

    # endregion
