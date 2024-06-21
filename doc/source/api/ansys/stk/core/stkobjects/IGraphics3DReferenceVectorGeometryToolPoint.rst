IGraphics3DReferenceVectorGeometryToolPoint
===========================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint

   IGraphics3DReferenceAnalysisWorkbenchComponent
   
   Configure the visual representation of a Vector Geometry point component in 3D.

.. py:currentmodule:: IGraphics3DReferenceVectorGeometryToolPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.trajectory_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.ra_dec_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.ra_dec_unit_abrv`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.magnitude_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.magnitude_unit_abrv`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.cartesian_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.cartesian_unit_abrv`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.available_systems`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceVectorGeometryToolPoint


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.trajectory_type
    :type: TRAJECTORY_TYPE

    Specifies the arrow type used to represent the geometric element.

.. py:property:: ra_dec_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.ra_dec_visible
    :type: bool

    Displays right-ascension and declination values with the selected point.

.. py:property:: ra_dec_unit_abrv
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.ra_dec_unit_abrv
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: magnitude_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.magnitude_visible
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: magnitude_unit_abrv
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.magnitude_unit_abrv
    :type: str

    The Magnitude Unit abrv.

.. py:property:: cartesian_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.cartesian_visible
    :type: bool

    If selected, the cartesian value is displayed on the selected geometric element.

.. py:property:: cartesian_unit_abrv
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.cartesian_unit_abrv
    :type: str

    Cartesian Unit Abrv uses Distance.

.. py:property:: system
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.system
    :type: str

    The name of the system used to define the coordinate frame associated with the selected RefCrdn.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.size
    :type: float

    Gets or sets the size of the selected geometric plane or point. Dimensionless.

.. py:property:: available_systems
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPoint.available_systems
    :type: list

    Returns an array of available Systems.


