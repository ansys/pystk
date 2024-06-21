ICoverageBoundsCustomBoundary
=============================

.. py:class:: ansys.stk.core.stkobjects.ICoverageBoundsCustomBoundary

   ICoverageBounds
   
   Custom Boundary.

.. py:currentmodule:: ICoverageBoundsCustomBoundary

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsCustomBoundary.region_files`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageBoundsCustomBoundary.boundary_objects`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageBoundsCustomBoundary


Property detail
---------------

.. py:property:: region_files
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomBoundary.region_files
    :type: ICoverageRegionFilesCollection

    File containing user-defined points defining a specific grid region.

.. py:property:: boundary_objects
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomBoundary.boundary_objects
    :type: IObjectLinkCollection

    A list of STK Objects to be used as part of the coverage area.


