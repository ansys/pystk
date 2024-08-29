IFigureOfMeritDefinitionDilutionOfPrecision
===========================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision

   Bases: IFigureOfMeritDefinitionCompute

   Dilution Of Precision Figure of Merit.

.. py:currentmodule:: IFigureOfMeritDefinitionDilutionOfPrecision

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.set_method`
              - Set a static DOP value over the entire coverage interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.is_method_supported`
              - Is the DOP method supported?
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.set_type`
              - Set the compute option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.is_type_supported`
              - Is the compute option supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.method`
              - Calculate dilution of precision.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.supported_methods`
              - Supported DOP methods.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.type`
              - Compute options for the DOP Figure of Merit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.supported_types`
              - Supported compute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.time_step`
              - Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.type_data`
              - DOP type data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.invalid_value_action`
              - Controls consideration of time samples usage for computing navigation solution.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionDilutionOfPrecision


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.method
    :type: FIGURE_OF_MERIT_METHOD

    Calculate dilution of precision.

.. py:property:: supported_methods
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.supported_methods
    :type: list

    Supported DOP methods.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.type
    :type: FIGURE_OF_MERIT_COMPUTE_TYPE

    Compute options for the DOP Figure of Merit.

.. py:property:: supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.supported_types
    :type: list

    Supported compute options.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.time_step
    :type: float

    Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.

.. py:property:: type_data
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.type_data
    :type: IFigureOfMeritDefinitionData

    DOP type data.

.. py:property:: invalid_value_action
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.invalid_value_action
    :type: FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE

    Controls consideration of time samples usage for computing navigation solution.


Method detail
-------------


.. py:method:: set_method(self, method: FIGURE_OF_MERIT_METHOD) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.set_method

    Set a static DOP value over the entire coverage interval.

    :Parameters:

    **method** : :obj:`~FIGURE_OF_MERIT_METHOD`

    :Returns:

        :obj:`~None`

.. py:method:: is_method_supported(self, method: FIGURE_OF_MERIT_METHOD) -> bool
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.is_method_supported

    Is the DOP method supported?

    :Parameters:

    **method** : :obj:`~FIGURE_OF_MERIT_METHOD`

    :Returns:

        :obj:`~bool`



.. py:method:: set_type(self, computeType: FIGURE_OF_MERIT_COMPUTE_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.set_type

    Set the compute option.

    :Parameters:

    **computeType** : :obj:`~FIGURE_OF_MERIT_COMPUTE_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_type_supported(self, computeType: FIGURE_OF_MERIT_COMPUTE_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision.is_type_supported

    Is the compute option supported?

    :Parameters:

    **computeType** : :obj:`~FIGURE_OF_MERIT_COMPUTE_TYPE`

    :Returns:

        :obj:`~bool`







