BurnoutLaunchAzRadius
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnout`

   The launch azimuth and radius burnout point.

.. py:currentmodule:: BurnoutLaunchAzRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.azimuth`
              - Gets or sets the azimuth of the launch trajectory. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.down_range_dist`
              - Gets or sets the downrange distance of the spacecraft from launch at burnout. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.radius`
              - Gets or sets the radius of the spacecraft at burnout. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BurnoutLaunchAzRadius


Property detail
---------------

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.azimuth
    :type: typing.Any

    Gets or sets the azimuth of the launch trajectory. Uses Angle Dimension.

.. py:property:: down_range_dist
    :canonical: ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.down_range_dist
    :type: float

    Gets or sets the downrange distance of the spacecraft from launch at burnout. Uses Distance Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius.radius
    :type: float

    Gets or sets the radius of the spacecraft at burnout. Uses Distance Dimension.


