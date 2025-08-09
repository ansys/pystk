CoverageGrid
============

.. py:class:: ansys.stk.core.stkobjects.CoverageGrid

   Grid Definition and resolution.

.. py:currentmodule:: CoverageGrid

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGrid.bounds_type`
              - Type of bounds used to define the coverage region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGrid.bounds`
              - Get the coverage region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGrid.resolution_type`
              - Type of criterion used to define grid resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGrid.resolution`
              - Grid resolution.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGrid


Property detail
---------------

.. py:property:: bounds_type
    :canonical: ansys.stk.core.stkobjects.CoverageGrid.bounds_type
    :type: CoverageBounds

    Type of bounds used to define the coverage region.

.. py:property:: bounds
    :canonical: ansys.stk.core.stkobjects.CoverageGrid.bounds
    :type: ICoverageBounds

    Get the coverage region.

.. py:property:: resolution_type
    :canonical: ansys.stk.core.stkobjects.CoverageGrid.resolution_type
    :type: CoverageResolution

    Type of criterion used to define grid resolution.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.CoverageGrid.resolution
    :type: ICoverageResolution

    Grid resolution.


