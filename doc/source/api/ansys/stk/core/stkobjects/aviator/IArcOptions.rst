IArcOptions
===========

.. py:class:: ansys.stk.core.stkobjects.aviator.IArcOptions

   object
   
   Interface used to access the arc options for a procedure.

.. py:currentmodule:: IArcOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.turn_direction`
              - Gets or sets the turn direction to the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.start_bearing`
              - Gets or sets the bearing from the site to the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.use_magnetic_heading`
              - Gets or sets the option to use a magnetic heading for the start bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.radius`
              - Gets or sets the radius of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.turn_angle`
              - Gets or sets the length of the arc the aircraft will fly.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.join_arc`
              - Gets or sets the method to join the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IArcOptions.exit_arc`
              - Gets or sets the method to exit the arc.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IArcOptions


Property detail
---------------

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.turn_direction
    :type: TURN_DIRECTION

    Gets or sets the turn direction to the arc.

.. py:property:: start_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.start_bearing
    :type: typing.Any

    Gets or sets the bearing from the site to the arc.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magnetic heading for the start bearing.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.radius
    :type: float

    Gets or sets the radius of the arc.

.. py:property:: turn_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.turn_angle
    :type: typing.Any

    Gets or sets the length of the arc the aircraft will fly.

.. py:property:: join_arc
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.join_arc
    :type: JOIN_EXIT_ARC_METHOD

    Gets or sets the method to join the arc.

.. py:property:: exit_arc
    :canonical: ansys.stk.core.stkobjects.aviator.IArcOptions.exit_arc
    :type: JOIN_EXIT_ARC_METHOD

    Gets or sets the method to exit the arc.


