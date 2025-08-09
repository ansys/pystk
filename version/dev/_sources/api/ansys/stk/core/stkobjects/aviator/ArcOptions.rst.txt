ArcOptions
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.ArcOptions

   Class defining the arc options for a procedure.

.. py:currentmodule:: ArcOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.exit_arc`
              - Get or set the method to exit the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.join_arc`
              - Get or set the method to join the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.radius`
              - Get or set the radius of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.start_bearing`
              - Get or set the bearing from the site to the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.turn_angle`
              - Get or set the length of the arc the aircraft will fly.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.turn_direction`
              - Get or set the turn direction to the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcOptions.use_magnetic_heading`
              - Get or set the option to use a magnetic heading for the start bearing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ArcOptions


Property detail
---------------

.. py:property:: exit_arc
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.exit_arc
    :type: JoinExitArcMethod

    Get or set the method to exit the arc.

.. py:property:: join_arc
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.join_arc
    :type: JoinExitArcMethod

    Get or set the method to join the arc.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.radius
    :type: float

    Get or set the radius of the arc.

.. py:property:: start_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.start_bearing
    :type: typing.Any

    Get or set the bearing from the site to the arc.

.. py:property:: turn_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.turn_angle
    :type: typing.Any

    Get or set the length of the arc the aircraft will fly.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.turn_direction
    :type: TurnDirection

    Get or set the turn direction to the arc.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ArcOptions.use_magnetic_heading
    :type: bool

    Get or set the option to use a magnetic heading for the start bearing.


