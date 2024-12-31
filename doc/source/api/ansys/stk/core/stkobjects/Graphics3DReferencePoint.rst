Graphics3DReferencePoint
========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferencePoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining a reference point (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferencePoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.trajectory_type`
              - Specifies the arrow type used to represent the geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_right_ascension_declination_values`
              - Displays right-ascension and declination values with the selected point.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.right_ascension_declination_units_abbreviation`
              - Right Ascension Declination Unit Abrv.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_magnitude_value`
              - If selected, the magnitude value is displayed on the selected geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.magnitude_units_abbreviation`
              - The Magnitude Unit abrv.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_cartesian_value`
              - If selected, the cartesian value is displayed on the selected geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.cartesian_units_abbreviation`
              - Cartesian Unit Abrv uses Distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.system`
              - The name of the system used to define the coordinate frame associated with the selected RefCrdn.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.size`
              - Gets or sets the size of the selected geometric plane or point. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint.available_systems`
              - Returns an array of available Systems.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferencePoint


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.trajectory_type
    :type: TrajectoryType

    Specifies the arrow type used to represent the geometric element.

.. py:property:: show_right_ascension_declination_values
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_right_ascension_declination_values
    :type: bool

    Displays right-ascension and declination values with the selected point.

.. py:property:: right_ascension_declination_units_abbreviation
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.right_ascension_declination_units_abbreviation
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: show_magnitude_value
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_magnitude_value
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: magnitude_units_abbreviation
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.magnitude_units_abbreviation
    :type: str

    The Magnitude Unit abrv.

.. py:property:: show_cartesian_value
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.show_cartesian_value
    :type: bool

    If selected, the cartesian value is displayed on the selected geometric element.

.. py:property:: cartesian_units_abbreviation
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.cartesian_units_abbreviation
    :type: str

    Cartesian Unit Abrv uses Distance.

.. py:property:: system
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.system
    :type: str

    The name of the system used to define the coordinate frame associated with the selected RefCrdn.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.size
    :type: float

    Gets or sets the size of the selected geometric plane or point. Dimensionless.

.. py:property:: available_systems
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePoint.available_systems
    :type: list

    Returns an array of available Systems.


