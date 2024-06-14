IBurnoutLaunchAzAltitude
========================

.. py:class:: IBurnoutLaunchAzAltitude

   IBurnout
   
   Properties for a launch azimuth / altitude burnout point definition.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~azimuth`
            * - :py:meth:`~down_range_dist`
            * - :py:meth:`~altitude_radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBurnoutLaunchAzAltitude


Property detail
---------------

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutLaunchAzAltitude.azimuth
    :type: typing.Any

    Gets or sets the azimuth of the launch trajectory. Uses Angle Dimension.

.. py:property:: down_range_dist
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutLaunchAzAltitude.down_range_dist
    :type: float

    Gets or sets the downrange distance of the spacecraft from launch at burnout. Uses Distance Dimension.

.. py:property:: altitude_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutLaunchAzAltitude.altitude_radius
    :type: float

    Gets or sets the altitude of the spacecraft at burnout. Uses Distance Dimension.


