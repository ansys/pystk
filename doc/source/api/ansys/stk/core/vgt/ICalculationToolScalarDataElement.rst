ICalculationToolScalarDataElement
=================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarDataElement

   object
   
   Any time-dependent data element from STK data providers available for parent STK object.

.. py:currentmodule:: ICalculationToolScalarDataElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.set`
              - Set the data provider and the element name.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.set_with_group`
              - Set the data provider name, the element name, and data provider type name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.data_provider`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.element_name`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.group`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.interpolation`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.sampling`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.use_samples`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.save_data_option`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarDataElement.invalid_data_indicator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarDataElement


Property detail
---------------

.. py:property:: data_provider
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.data_provider
    :type: str

    The name of the data provider.

.. py:property:: element_name
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.element_name
    :type: str

    The name of the data element within the data provider.

.. py:property:: group
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.group
    :type: str

    A group name the data element is a part of. If the element is not a part of a group, the property will return an empty string.

.. py:property:: interpolation
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.interpolation
    :type: IAnalysisWorkbenchInterp

    Specify whether to use Lagrange or Hermite interpolation. See STK help on interpolation.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.sampling
    :type: IAnalysisWorkbenchSampling

    Relative tolerance uses a combination of relative and absolute changes in scalar values between samples. Curvature tolerance also uses changes in slope between samples.

.. py:property:: use_samples
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.use_samples
    :type: bool

    If set to true, selected data provider is presampled over its entire availability span using sampling method specified in Advanced options...

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Determines if computed samples are saved/loaded, otherwise if using samples they are recomputed on load.

.. py:property:: invalid_data_indicator
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.invalid_data_indicator
    :type: float

    Sets the value to display in a report or graph when the actual value is not a valid real number.


Method detail
-------------












.. py:method:: set(self, dataProvider: str, elementName: str) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.set

    Set the data provider and the element name.

    :Parameters:

    **dataProvider** : :obj:`~str`
    **elementName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_group(self, dataProvider: str, typeName: str, elementName: str) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarDataElement.set_with_group

    Set the data provider name, the element name, and data provider type name.

    :Parameters:

    **dataProvider** : :obj:`~str`
    **typeName** : :obj:`~str`
    **elementName** : :obj:`~str`

    :Returns:

        :obj:`~None`



