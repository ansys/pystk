ICoverageGrid
=============

.. py:class:: ICoverageGrid

   object
   
   Grid Definition and resolution.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bounds_type`
            * - :py:meth:`~bounds`
            * - :py:meth:`~resolution_type`
            * - :py:meth:`~resolution`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGrid


Property detail
---------------

.. py:property:: bounds_type
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.bounds_type
    :type: "COVERAGE_BOUNDS"

    Type of bounds used to define the coverage region.

.. py:property:: bounds
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.bounds
    :type: "IAgCvBounds"

    Get the coverage region.

.. py:property:: resolution_type
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.resolution_type
    :type: "COVERAGE_RESOLUTION"

    Type of criterion used to define grid resolution.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.ICoverageGrid.resolution
    :type: "IAgCvResolution"

    Grid resolution.


