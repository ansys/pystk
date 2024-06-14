IFigureOfMeritDefinitionCompute
===============================

.. py:class:: IFigureOfMeritDefinitionCompute

   IFigureOfMeritDefinition
   
   Compute options for navigation accuracy.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_compute_type`
              - Set the type of compute option.
            * - :py:meth:`~is_compute_type_supported`
              - Is the type of compute option supported?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_type`
            * - :py:meth:`~compute_supported_types`
            * - :py:meth:`~compute`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionCompute


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type
    :type: "FIGURE_OF_MERIT_COMPUTE"

    Type of compute option to be used for navigation accuracy.

.. py:property:: compute_supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types
    :type: list

    Compute supported types.

.. py:property:: compute
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute.compute
    :type: "IAgFmDefinitionData"

    Compute.


Method detail
-------------


.. py:method:: set_compute_type(self, computeType:"FIGURE_OF_MERIT_COMPUTE") -> None

    Set the type of compute option.

    :Parameters:

    **computeType** : :obj:`~"FIGURE_OF_MERIT_COMPUTE"`

    :Returns:

        :obj:`~None`

.. py:method:: is_compute_type_supported(self, computeType:"FIGURE_OF_MERIT_COMPUTE") -> bool

    Is the type of compute option supported?

    :Parameters:

    **computeType** : :obj:`~"FIGURE_OF_MERIT_COMPUTE"`

    :Returns:

        :obj:`~bool`



