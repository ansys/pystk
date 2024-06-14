IDisplayTime
============

.. py:class:: IDisplayTime

   object
   
   The display time interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_display_status_type`
              - Set the display status type.
            * - :py:meth:`~is_display_status_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~display_status_type`
            * - :py:meth:`~display_status_supported_types`
            * - :py:meth:`~display_times_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDisplayTime


Property detail
---------------

.. py:property:: display_status_type
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_type
    :type: "DISPLAY_TIMES_TYPE"

    Returns the Display Status type.

.. py:property:: display_status_supported_types
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_status_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: display_times_data
    :canonical: ansys.stk.core.stkobjects.IDisplayTime.display_times_data
    :type: "IAgDisplayTimesData"

    Returns the display times data.


Method detail
-------------


.. py:method:: set_display_status_type(self, displayStatus:"DISPLAY_TIMES_TYPE") -> None

    Set the display status type.

    :Parameters:

    **displayStatus** : :obj:`~"DISPLAY_TIMES_TYPE"`

    :Returns:

        :obj:`~None`

.. py:method:: is_display_status_type_supported(self, displayStatus:"DISPLAY_TIMES_TYPE") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **displayStatus** : :obj:`~"DISPLAY_TIMES_TYPE"`

    :Returns:

        :obj:`~bool`



