CoverageBoundsCustomBoundary
============================

.. py:class:: ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`

   Custom Boundary.

.. py:currentmodule:: CoverageBoundsCustomBoundary

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary.region_files`
              - File containing user-defined points defining a specific grid region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary.boundary_objects`
              - A list of STK Objects to be used as part of the coverage area.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBoundsCustomBoundary


Property detail
---------------

.. py:property:: region_files
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary.region_files
    :type: CoverageRegionFilesCollection

    File containing user-defined points defining a specific grid region.

.. py:property:: boundary_objects
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary.boundary_objects
    :type: ObjectLinkCollection

    A list of STK Objects to be used as part of the coverage area.


