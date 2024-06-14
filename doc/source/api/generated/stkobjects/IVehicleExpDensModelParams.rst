IVehicleExpDensModelParams
==========================

.. py:class:: IVehicleExpDensModelParams

   object
   
   Interface for exponential density model (for LOP propagator).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_density`
            * - :py:meth:`~reference_height`
            * - :py:meth:`~scale_height`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleExpDensModelParams


Property detail
---------------

.. py:property:: reference_density
    :canonical: ansys.stk.core.stkobjects.IVehicleExpDensModelParams.reference_density
    :type: float

    Gets or sets the reference density. Uses Density Dimension.

.. py:property:: reference_height
    :canonical: ansys.stk.core.stkobjects.IVehicleExpDensModelParams.reference_height
    :type: float

    Gets or sets the reference height. Uses Distance Dimension.

.. py:property:: scale_height
    :canonical: ansys.stk.core.stkobjects.IVehicleExpDensModelParams.scale_height
    :type: float

    Gets or sets the scale height. Uses Distance Dimension.


