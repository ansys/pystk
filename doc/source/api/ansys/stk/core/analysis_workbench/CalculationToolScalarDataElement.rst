CalculationToolScalarDataElement
================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Any time-dependent data element from STK data providers available for parent STK object.

.. py:currentmodule:: CalculationToolScalarDataElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.set`
              - Set the data provider and the element name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.set_with_group`
              - Set the data provider name, the element name, and data provider type name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.data_provider`
              - The name of the data provider.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.element_name`
              - The name of the data element within the data provider.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.group`
              - A group name the data element is a part of. If the element is not a part of a group, the property will return an empty string.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.interpolation`
              - Specify whether to use Lagrange or Hermite interpolation. See STK help on interpolation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.sampling`
              - Relative tolerance uses a combination of relative and absolute changes in scalar values between samples. Curvature tolerance also uses changes in slope between samples.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.use_samples`
              - If set to true, selected data provider is presampled over its entire availability span using sampling method specified in Advanced options...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.save_data_option`
              - Determine if computed samples are saved/loaded, otherwise if using samples they are recomputed on load.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.invalid_data_indicator`
              - Set the value to display in a report or graph when the actual value is not a valid real number.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarDataElement


Property detail
---------------

.. py:property:: data_provider
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.data_provider
    :type: str

    The name of the data provider.

.. py:property:: element_name
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.element_name
    :type: str

    The name of the data element within the data provider.

.. py:property:: group
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.group
    :type: str

    A group name the data element is a part of. If the element is not a part of a group, the property will return an empty string.

.. py:property:: interpolation
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.interpolation
    :type: IAnalysisWorkbenchInterpolator

    Specify whether to use Lagrange or Hermite interpolation. See STK help on interpolation.

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.sampling
    :type: IAnalysisWorkbenchSampling

    Relative tolerance uses a combination of relative and absolute changes in scalar values between samples. Curvature tolerance also uses changes in slope between samples.

.. py:property:: use_samples
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.use_samples
    :type: bool

    If set to true, selected data provider is presampled over its entire availability span using sampling method specified in Advanced options...

.. py:property:: save_data_option
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.save_data_option
    :type: SaveDataType

    Determine if computed samples are saved/loaded, otherwise if using samples they are recomputed on load.

.. py:property:: invalid_data_indicator
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.invalid_data_indicator
    :type: float

    Set the value to display in a report or graph when the actual value is not a valid real number.


Method detail
-------------












.. py:method:: set(self, data_provider: str, element_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.set

    Set the data provider and the element name.

    :Parameters:

        **data_provider** : :obj:`~str`

        **element_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_group(self, data_provider: str, type_name: str, element_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement.set_with_group

    Set the data provider name, the element name, and data provider type name.

    :Parameters:

        **data_provider** : :obj:`~str`

        **type_name** : :obj:`~str`

        **element_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



