IAccessEventDetection
=====================

.. py:class:: ansys.stk.core.stkobjects.IAccessEventDetection

   object
   
   Define properties and methods to configure the event detection strategy used in access computations.

.. py:currentmodule:: IAccessEventDetection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessEventDetection.set_type`
              - Set the event detection type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessEventDetection.is_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessEventDetection.type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessEventDetection.supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessEventDetection.strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessEventDetection


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IAccessEventDetection.type
    :type: EVENT_DETECTION

    Get the type of event detection (e.g., with or without subsampling).

.. py:property:: supported_types
    :canonical: ansys.stk.core.stkobjects.IAccessEventDetection.supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: strategy
    :canonical: ansys.stk.core.stkobjects.IAccessEventDetection.strategy
    :type: IEventDetectionStrategy

    Get the selected event detection strategy.


Method detail
-------------


.. py:method:: set_type(self, eventDetection: EVENT_DETECTION) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessEventDetection.set_type

    Set the event detection type.

    :Parameters:

    **eventDetection** : :obj:`~EVENT_DETECTION`

    :Returns:

        :obj:`~None`

.. py:method:: is_type_supported(self, eventDetection: EVENT_DETECTION) -> bool
    :canonical: ansys.stk.core.stkobjects.IAccessEventDetection.is_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **eventDetection** : :obj:`~EVENT_DETECTION`

    :Returns:

        :obj:`~bool`



