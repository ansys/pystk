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

"""Provides graphs for Transmitter objects."""
import collections.abc

import matplotlib

from ansys.stk.core.stkobjects import Transmitter
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import line_chart


def transmitter_spectrum_and_filter_line_chart(stk_object : Transmitter, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Show the spectrum of a modulated RF signal as a function of the frequency across the RF bandwidth of a transmitter.

    It also lists the profile of the transmitter filter magnitude and the profile of the filtered spectrum as modified by the filter.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Transmitter\\Transmitter Spectrum and Filter.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Transmitter
        The STK Transmitter object.
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.root
    df = stk_object.data_providers.item('Transmitter Spectrum and Filter').execute_elements(['SpectrumMagnitude', 'FilterMagnitude', 'BandFrequency', 'FilteredSpectrum']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'spectrummagnitude', 'label':'SpectrumMagnitude', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'},
            {'y_name':'filtermagnitude', 'label':'FilterMagnitude', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'},
            {'y_name':'filteredspectrum', 'label':'FilteredSpectrum', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart([df], root, ['bandfrequency','spectrummagnitude','filtermagnitude','filteredspectrum'], [], axes, 'bandfrequency','Band Frequency', 'Transmitter Spectrum and Filter', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

