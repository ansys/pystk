IExportToolStepSize
===================

.. py:class:: IExportToolStepSize

   object
   
   The step size.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~value`
            * - :py:meth:`~step_size_type`
            * - :py:meth:`~time_array`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IExportToolStepSize


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IExportToolStepSize.value
    :type: float

    Step size value. Uses Time Dimension.

.. py:property:: step_size_type
    :canonical: ansys.stk.core.stkobjects.IExportToolStepSize.step_size_type
    :type: EXPORT_TOOL_STEP_SIZE

    Step Size Type.

.. py:property:: time_array
    :canonical: ansys.stk.core.stkobjects.IExportToolStepSize.time_array
    :type: str

    Gets or sets the time array component for the vehicle.


