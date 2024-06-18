INavigationOptions
==================

.. py:class:: INavigationOptions

   object
   
   Interface used to access the navigation options for an Aviator procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~nav_mode`
            * - :py:meth:`~arrive_on_course`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~enroute_first_turn`
            * - :py:meth:`~enroute_second_turn`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import INavigationOptions


Property detail
---------------

.. py:property:: nav_mode
    :canonical: ansys.stk.core.stkobjects.aviator.INavigationOptions.nav_mode
    :type: "POINT_TO_POINT_MODE"

    Gets or sets the navigation mode.

.. py:property:: arrive_on_course
    :canonical: ansys.stk.core.stkobjects.aviator.INavigationOptions.arrive_on_course
    :type: typing.Any

    Gets or sets the aircraft will start or arrive at the procedure site with the specified course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.INavigationOptions.use_magnetic_heading
    :type: bool

    Opt whether to use a magnetic heading to arrive on course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: enroute_first_turn
    :canonical: ansys.stk.core.stkobjects.aviator.INavigationOptions.enroute_first_turn
    :type: "NAVIGATOR_TURN_DIRECTION"

    Option for the first turn.

.. py:property:: enroute_second_turn
    :canonical: ansys.stk.core.stkobjects.aviator.INavigationOptions.enroute_second_turn
    :type: "NAVIGATOR_TURN_DIRECTION"

    Option for the second turn.


