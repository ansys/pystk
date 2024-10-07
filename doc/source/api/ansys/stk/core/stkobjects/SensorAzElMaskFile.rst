SensorAzElMaskFile
==================

.. py:class:: ansys.stk.core.stkobjects.SensorAzElMaskFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAzElMaskData`

   Class to define a Sensor's Azimuth-Elevation mask.

.. py:currentmodule:: SensorAzElMaskFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorAzElMaskFile.filename`
              - Path and filename of Az-El mask file (.aem) or body mask file (.bmsk).
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorAzElMaskFile.boresight_axis`
              - Boresight Axis, calculated using the body-fixed coordinates of the sensor's parent object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorAzElMaskFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.SensorAzElMaskFile.filename
    :type: str

    Path and filename of Az-El mask file (.aem) or body mask file (.bmsk).

.. py:property:: boresight_axis
    :canonical: ansys.stk.core.stkobjects.SensorAzElMaskFile.boresight_axis
    :type: SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE

    Boresight Axis, calculated using the body-fixed coordinates of the sensor's parent object.


