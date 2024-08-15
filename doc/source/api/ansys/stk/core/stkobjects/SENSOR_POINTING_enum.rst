SENSOR_POINTING
===============

.. py:class:: ansys.stk.core.stkobjects.SENSOR_POINTING

   IntEnum


.. py:currentmodule:: SENSOR_POINTING

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~POINT_3D_MODEL`
              - 3D model: point a sensor along one of the available elements of the selected 3D Model.

            * - :py:attr:`~POINT_EXTERNAL`
              - External: import a custom sensor pointing file.

            * - :py:attr:`~POINT_FIXED`
              - Fixed: model sensors that are fixed in the parent object's body coordinate frame, so that they always point in the same direction relative to the parent.

            * - :py:attr:`~POINT_FIXED_AXES`
              - Fixed in axes: point a sensor with reference to a set of axes, using the selected orientation system.

            * - :py:attr:`~POINT_SPINNING`
              - Spinning: model radars, push broom sensors and other instruments that spin, scan or sweep over time.

            * - :py:attr:`~POINT_TARGETED`
              - Targeted: model sensors that track other objects.

            * - :py:attr:`~POINT_GRAZING_ALTITUDE`
              - Grazing altitude: model a sensor so that the boresight vector will graze the central body at a specified altitude.

            * - :py:attr:`~POINT_ALONG_VECTOR`
              - Along Vector: model a sensor so that sensor pointing alignment is controlled by using a pair of vectors defined using the Vector Geometry tool.

            * - :py:attr:`~POINT_SCHEDULE`
              - Schedule: controls scheduled sensor pointing.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_POINTING


