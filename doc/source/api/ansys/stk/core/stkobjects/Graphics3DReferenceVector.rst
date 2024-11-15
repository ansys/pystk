Graphics3DReferenceVector
=========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferenceVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining a reference vector (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferenceVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.draw_at_central_body`
              - Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_right_ascension_declination_values`
              - Displays right-ascension and declination values with the selected vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.right_ascension_declination_units_abbreviation`
              - Right Ascension Declination Unit Abrv.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_magnitude_value`
              - If selected, the magnitude value is displayed on the selected geometric element.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.magnitude_dimension`
              - The Magnitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.magnitude_units_abbreviation`
              - Magnitude's current unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_persistence`
              - Successively displays geometric elements over the specified duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.duration`
              - The length of time during which the geometric element is visible. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.connect`
              - Specifies the method used for connecting geometric elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.transparent`
              - If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.axes`
              - The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.draw_at_point`
              - If selected, the geometric element is drawn at the selected point.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.point`
              - Displays a point at the current animation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.true_scale`
              - If the Scale Relative to Model is selected, the scale of the model is multiplied by the scale of the vector. If the Scale Relative to Model is not selected, you can set the size of the geometric elements independent of the model scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.available_axes`
              - Returns a safearray of available axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector.available_points`
              - Returns a safearray of available points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferenceVector


Property detail
---------------

.. py:property:: draw_at_central_body
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.draw_at_central_body
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: show_right_ascension_declination_values
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_right_ascension_declination_values
    :type: bool

    Displays right-ascension and declination values with the selected vector.

.. py:property:: right_ascension_declination_units_abbreviation
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.right_ascension_declination_units_abbreviation
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: show_magnitude_value
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_magnitude_value
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: magnitude_dimension
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.magnitude_dimension
    :type: str

    The Magnitude Dimension.

.. py:property:: magnitude_units_abbreviation
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.magnitude_units_abbreviation
    :type: str

    Magnitude's current unit.

.. py:property:: show_persistence
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.show_persistence
    :type: bool

    Successively displays geometric elements over the specified duration.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.duration
    :type: float

    The length of time during which the geometric element is visible. Uses Time Dimension.

.. py:property:: connect
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.connect
    :type: VECTOR_AXES_CONNECT_TYPE

    Specifies the method used for connecting geometric elements.

.. py:property:: transparent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.transparent
    :type: bool

    If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.

.. py:property:: axes
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.axes
    :type: str

    The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.

.. py:property:: draw_at_point
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.draw_at_point
    :type: bool

    If selected, the geometric element is drawn at the selected point.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.point
    :type: str

    Displays a point at the current animation time.

.. py:property:: true_scale
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.true_scale
    :type: bool

    If the Scale Relative to Model is selected, the scale of the model is multiplied by the scale of the vector. If the Scale Relative to Model is not selected, you can set the size of the geometric elements independent of the model scale.

.. py:property:: available_axes
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.available_axes
    :type: list

    Returns a safearray of available axes.

.. py:property:: available_points
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVector.available_points
    :type: list

    Returns a safearray of available points.


