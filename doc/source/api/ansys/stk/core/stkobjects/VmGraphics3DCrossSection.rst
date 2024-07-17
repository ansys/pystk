VmGraphics3DCrossSection
========================

.. py:class:: ansys.stk.core.stkobjects.VmGraphics3DCrossSection

   Bases: 

   Class defining planar cross-sections through the volumetric grid.

.. py:currentmodule:: VmGraphics3DCrossSection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSection.show`
              - Show or hide the cross sections in 3D window.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSection.opacity`
              - Set the opacity multiplier which is used to incrementally increase the opacity of the cross-sections. Valid value is greater or equal to 1.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSection.planes`
              - Access and manipulate the collection of cross section planes for Volumetric object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VmGraphics3DCrossSection


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSection.show
    :type: bool

    Show or hide the cross sections in 3D window.

.. py:property:: opacity
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSection.opacity
    :type: float

    Set the opacity multiplier which is used to incrementally increase the opacity of the cross-sections. Valid value is greater or equal to 1.

.. py:property:: planes
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSection.planes
    :type: IVmGraphics3DCrossSectionPlaneCollection

    Access and manipulate the collection of cross section planes for Volumetric object.


