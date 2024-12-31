SensorPointing
==============

.. py:class:: ansys.stk.core.stkobjects.SensorPointing

   IntEnum


.. py:currentmodule:: SensorPointing

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ELEMENT_OF_3D_MODEL`
              - 3D model: point a sensor along one of the available elements of the selected 3D Model.

            * - :py:attr:`~FILE`
              - External: import a custom sensor pointing file.

            * - :py:attr:`~FIXED_IN_PARENT_BODY_AXES`
              - Fixed: model sensors that are fixed in the parent object's body coordinate frame, so that they always point in the same direction relative to the parent.

            * - :py:attr:`~FIXED_IN_AXES`
              - Fixed in axes: point a sensor with reference to a set of axes, using the selected orientation system.

            * - :py:attr:`~SPINNING`
              - Spinning: model radars, push broom sensors and other instruments that spin, scan or sweep over time.

            * - :py:attr:`~TARGETED`
              - Targeted: model sensors that track other objects.

            * - :py:attr:`~BORESIGHT_GRAZING_ALTITUDE`
              - Grazing altitude: model a sensor so that the boresight vector will graze the central body at a specified altitude.

            * - :py:attr:`~ALONG_VECTOR`
              - Along Vector: model a sensor so that sensor pointing alignment is controlled by using a pair of vectors defined using the Vector Geometry tool.

            * - :py:attr:`~SCHEDULED`
              - Schedule: controls scheduled sensor pointing.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointing


