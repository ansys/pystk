BoresightType
=============

.. py:class:: ansys.stk.core.stkobjects.BoresightType

   IntEnum


.. py:currentmodule:: BoresightType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~HOLD`
              - Hold: rotation about the Y axis followed by rotation about the new X-axis.

            * - :py:attr:`~LEVEL`
              - Level: boresight is aligned with the line of sight to the target, while the sensor's x-axis is constrained to be in the plane parallel to the meridian plane passing through the target.

            * - :py:attr:`~ROTATE`
              - Rotate: rotation about the sensor's or antenna's Z axis by the azimuth angle, followed by rotation about the new Y axis by 90 degrees minus the elevation angle.

            * - :py:attr:`~UP_VECTOR`
              - UpVector: boresight is aligned with the line of sight to the target, while the specified constraint direction lies at a specified clock angle about the boresight from the sensor's x-axis.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import BoresightType


