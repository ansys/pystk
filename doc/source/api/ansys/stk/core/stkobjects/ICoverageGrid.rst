ICoverageGrid
=============

.. py:class:: ansys.stk.core.stkobjects.ICoverageGrid

   object
   
   Grid Definition and resolution.

.. py:currentmodule:: ICoverageGrid

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGrid.bounds_type`
              - Type of bounds used to define the coverage region.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGrid.bounds`
              - Get the coverage region.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGrid.resolution_type`
              - Type of criterion used to define grid resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGrid.resolution`
              - Grid resolution.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGrid


Property detail
---------------

.. py:property:: bounds_type
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.bounds_type
    :type: COVERAGE_BOUNDS

    Type of bounds used to define the coverage region.

.. py:property:: bounds
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.bounds
    :type: ICoverageBounds

    Get the coverage region.

.. py:property:: resolution_type
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.resolution_type
    :type: COVERAGE_RESOLUTION

    Type of criterion used to define grid resolution.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.resolution
    :type: ICoverageResolution

    Grid resolution.


