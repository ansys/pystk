IDisplayTime
============

.. py:class:: ansys.stk.core.stkobjects.IDisplayTime

   The display time interface.

.. py:currentmodule:: IDisplayTime

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.set_display_status_type`
              - Set the display status type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.is_display_status_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.display_status_type`
              - Return the Display Status type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.display_status_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.display_times_data`
              - Return the display times data.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDisplayTime


Property detail
---------------

.. py:property:: display_status_type
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_type
    :type: DisplayTimesType

    Return the Display Status type.

.. py:property:: display_status_supported_types
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: display_times_data
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_times_data
    :type: IDisplayTimesData

    Return the display times data.


Method detail
-------------


.. py:method:: set_display_status_type(self, display_status: DisplayTimesType) -> None
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.set_display_status_type

    Set the display status type.

    :Parameters:

        **display_status** : :obj:`~DisplayTimesType`


    :Returns:

        :obj:`~None`

.. py:method:: is_display_status_type_supported(self, display_status: DisplayTimesType) -> bool
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.is_display_status_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **display_status** : :obj:`~DisplayTimesType`


    :Returns:

        :obj:`~bool`



