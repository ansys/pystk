Graphics3DReferenceVectorGeometryToolPoint
==========================================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining a reference point (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferenceVectorGeometryToolPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.trajectory_type`
              - Specifies the arrow type used to represent the geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.ra_dec_visible`
              - Displays right-ascension and declination values with the selected point.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.ra_dec_unit_abrv`
              - Right Ascension Declination Unit Abrv.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.magnitude_visible`
              - If selected, the magnitude value is displayed on the selected geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.magnitude_unit_abrv`
              - The Magnitude Unit abrv.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.cartesian_visible`
              - If selected, the cartesian value is displayed on the selected geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.cartesian_unit_abrv`
              - Cartesian Unit Abrv uses Distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.system`
              - The name of the system used to define the coordinate frame associated with the selected RefCrdn.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.size`
              - Gets or sets the size of the selected geometric plane or point. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.available_systems`
              - Returns an array of available Systems.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferenceVectorGeometryToolPoint


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.trajectory_type
    :type: TRAJECTORY_TYPE

    Specifies the arrow type used to represent the geometric element.

.. py:property:: ra_dec_visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.ra_dec_visible
    :type: bool

    Displays right-ascension and declination values with the selected point.

.. py:property:: ra_dec_unit_abrv
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.ra_dec_unit_abrv
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: magnitude_visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.magnitude_visible
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: magnitude_unit_abrv
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.magnitude_unit_abrv
    :type: str

    The Magnitude Unit abrv.

.. py:property:: cartesian_visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.cartesian_visible
    :type: bool

    If selected, the cartesian value is displayed on the selected geometric element.

.. py:property:: cartesian_unit_abrv
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.cartesian_unit_abrv
    :type: str

    Cartesian Unit Abrv uses Distance.

.. py:property:: system
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.system
    :type: str

    The name of the system used to define the coordinate frame associated with the selected RefCrdn.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.size
    :type: float

    Gets or sets the size of the selected geometric plane or point. Dimensionless.

.. py:property:: available_systems
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint.available_systems
    :type: list

    Returns an array of available Systems.


