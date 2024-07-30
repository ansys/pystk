NavigationOptions
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.NavigationOptions

   Bases: 

   Class defining the navigation options in a procedure.

.. py:currentmodule:: NavigationOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.navigation_mode`
              - Gets or sets the navigation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.arrive_on_course`
              - Gets or sets the aircraft will start or arrive at the procedure site with the specified course. The nav mode must be set to Arrive on Course to set this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.use_magnetic_heading`
              - Opt whether to use a magnetic heading to arrive on course. The nav mode must be set to Arrive on Course to set this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_first_turn`
              - Option for the first turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_second_turn`
              - Option for the second turn.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import NavigationOptions


Property detail
---------------

.. py:property:: navigation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.navigation_mode
    :type: POINT_TO_POINT_MODE

    Gets or sets the navigation mode.

.. py:property:: arrive_on_course
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.arrive_on_course
    :type: typing.Any

    Gets or sets the aircraft will start or arrive at the procedure site with the specified course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.use_magnetic_heading
    :type: bool

    Opt whether to use a magnetic heading to arrive on course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: enroute_first_turn
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_first_turn
    :type: NAVIGATOR_TURN_DIRECTION

    Option for the first turn.

.. py:property:: enroute_second_turn
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_second_turn
    :type: NAVIGATOR_TURN_DIRECTION

    Option for the second turn.


