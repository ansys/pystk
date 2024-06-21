IDisplayTime
============

.. py:class:: ansys.stk.core.stkobjects.IDisplayTime

   object
   
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
            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.display_status_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDisplayTime.display_times_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDisplayTime


Property detail
---------------

.. py:property:: display_status_type
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_type
    :type: DISPLAY_TIMES_TYPE

    Returns the Display Status type.

.. py:property:: display_status_supported_types
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: display_times_data
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_times_data
    :type: IDisplayTimesData

    Returns the display times data.


Method detail
-------------


.. py:method:: set_display_status_type(self, displayStatus: DISPLAY_TIMES_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.set_display_status_type

    Set the display status type.

    :Parameters:

    **displayStatus** : :obj:`~DISPLAY_TIMES_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_display_status_type_supported(self, displayStatus: DISPLAY_TIMES_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.is_display_status_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **displayStatus** : :obj:`~DISPLAY_TIMES_TYPE`

    :Returns:

        :obj:`~bool`



