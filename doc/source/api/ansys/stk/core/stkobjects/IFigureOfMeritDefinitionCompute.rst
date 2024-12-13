IFigureOfMeritDefinitionCompute
===============================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute

   Bases: IFigureOfMeritDefinition

   Compute options for navigation accuracy.

.. py:currentmodule:: IFigureOfMeritDefinitionCompute

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type`
              - Set the type of compute option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported`
              - Is the type of compute option supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type`
              - Type of compute option to be used for navigation accuracy.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types`
              - Compute supported types.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute`
              - Compute.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionCompute


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type
    :type: FigureOfMeritCompute

    Type of compute option to be used for navigation accuracy.

.. py:property:: compute_supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types
    :type: list

    Compute supported types.

.. py:property:: compute
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute
    :type: IFigureOfMeritDefinitionData

    Compute.


Method detail
-------------


.. py:method:: set_compute_type(self, compute_type: FigureOfMeritCompute) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type

    Set the type of compute option.

    :Parameters:

    **compute_type** : :obj:`~FigureOfMeritCompute`

    :Returns:

        :obj:`~None`

.. py:method:: is_compute_type_supported(self, compute_type: FigureOfMeritCompute) -> bool
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported

    Is the type of compute option supported?

    :Parameters:

    **compute_type** : :obj:`~FigureOfMeritCompute`

    :Returns:

        :obj:`~bool`



