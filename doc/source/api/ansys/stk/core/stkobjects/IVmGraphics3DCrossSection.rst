IVmGraphics3DCrossSection
=========================

.. py:class:: ansys.stk.core.stkobjects.IVmGraphics3DCrossSection

   object
   
   IAgVmVOCrossSection Interface for defining planar cross-sections through the volumetric grid.

.. py:currentmodule:: IVmGraphics3DCrossSection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.show`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.opacity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.planes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3DCrossSection


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.show
    :type: bool

    Show or hide the cross sections in 3D window.

.. py:property:: opacity
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.opacity
    :type: float

    Set the opacity multiplier which is used to incrementally increase the opacity of the cross-sections. Valid value is greater or equal to 1.

.. py:property:: planes
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DCrossSection.planes
    :type: IVmGraphics3DCrossSectionPlaneCollection

    Access and manipulate the collection of cross section planes for Volumetric object.


