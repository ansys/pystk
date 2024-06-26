IVmAdvanced
===========

.. py:class:: ansys.stk.core.stkobjects.IVmAdvanced

   object
   
   IAgVmAdvanced Interface for advanced volumetric options.

.. py:currentmodule:: IVmAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmAdvanced.automatic_recompute`
              - Automatically recompute data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmAdvanced.save_computed_data_type`
              - Get save computed data type. A member of the AgEVmSaveComputedDataType enumeration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmAdvanced


Property detail
---------------

.. py:property:: automatic_recompute
    :canonical: ansys.stk.core.stkobjects.IVmAdvanced.automatic_recompute
    :type: bool

    Automatically recompute data.

.. py:property:: save_computed_data_type
    :canonical: ansys.stk.core.stkobjects.IVmAdvanced.save_computed_data_type
    :type: VM_SAVE_COMPUTED_DATA_TYPE

    Get save computed data type. A member of the AgEVmSaveComputedDataType enumeration.


