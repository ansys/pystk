ISensorAzElMaskFile
===================

.. py:class:: ISensorAzElMaskFile

   object
   
   IAgSnAzElMaskFile Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~boresight_axis`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorAzElMaskFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.ISensorAzElMaskFile.filename
    :type: str

    Path and filename of Az-El mask file (.aem) or body mask file (.bmsk).

.. py:property:: boresight_axis
    :canonical: ansys.stk.core.stkobjects.ISensorAzElMaskFile.boresight_axis
    :type: "SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE"

    Boresight Axis, calculated using the body-fixed coordinates of the sensor's parent object.


