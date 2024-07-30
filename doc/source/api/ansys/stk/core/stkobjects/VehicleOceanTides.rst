VehicleOceanTides
=================

.. py:class:: ansys.stk.core.stkobjects.VehicleOceanTides

   Bases: 

   Class defining the contribution of ocean tides.

.. py:currentmodule:: VehicleOceanTides

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOceanTides.max_degree`
              - Maximum degree: limit the ocean tide model to contributions of a specified maximum degree. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOceanTides.max_order`
              - Maximum order: limit the ocean tide model to contributions of a specified maximum order. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOceanTides.min_amplitude`
              - Minimum amplitude: include only those constituents whose tidal amplitude is sufficiently large by specifying the minimum amplitude to include in the computation. Uses SmallDistanceUnit Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleOceanTides


Property detail
---------------

.. py:property:: max_degree
    :canonical: ansys.stk.core.stkobjects.VehicleOceanTides.max_degree
    :type: int

    Maximum degree: limit the ocean tide model to contributions of a specified maximum degree. Dimensionless.

.. py:property:: max_order
    :canonical: ansys.stk.core.stkobjects.VehicleOceanTides.max_order
    :type: int

    Maximum order: limit the ocean tide model to contributions of a specified maximum order. Dimensionless.

.. py:property:: min_amplitude
    :canonical: ansys.stk.core.stkobjects.VehicleOceanTides.min_amplitude
    :type: float

    Minimum amplitude: include only those constituents whose tidal amplitude is sufficiently large by specifying the minimum amplitude to include in the computation. Uses SmallDistanceUnit Dimension.


