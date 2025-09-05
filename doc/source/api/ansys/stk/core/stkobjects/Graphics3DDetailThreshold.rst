Graphics3DDetailThreshold
=========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DDetailThreshold

   Class defining detail thresholds as an aid for improving performance when viewing in 3D.

.. py:currentmodule:: Graphics3DDetailThreshold

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.all`
              - The maximum viewing distance at which the finest detail in the model, label and vectors, attitude sphere, and geostationary box is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.enable_detail_threshold`
              - Detail thresholds as an aid for improving performance when viewing in 3D. Using these thresholds, the viewer sees varying degrees of detail on the models and graphics in the 3D Graphics window, depending on the distance of the object from the viewer.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.marker`
              - The maximum viewing distance at which a marker representing the object is visible. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.marker_label`
              - The maximum viewing distance at which a label and marker representing the object is visible. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.model_label`
              - The maximum viewing distance at which the coarsest detail in the model, label and vectors, attitude sphere, and geostationary box is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold.point`
              - The maximum viewing distance at which a point representing the object is visible. Uses Distance Dimension.



Examples
--------

Modify the Detail Thresholds Levels

.. code-block:: python

    # Satellite satellite: Satellite object
    details = satellite.graphics_3d.model.detail_threshold
    details.enable_detail_threshold = True
    details.all = 1  # km
    details.model_label = 2  # km
    details.marker_label = 40000  # km
    details.marker = 500000  # km
    details.point = 500000  # km


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DDetailThreshold


Property detail
---------------

.. py:property:: all
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.all
    :type: float

    The maximum viewing distance at which the finest detail in the model, label and vectors, attitude sphere, and geostationary box is displayed. Uses Distance Dimension.

.. py:property:: enable_detail_threshold
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.enable_detail_threshold
    :type: bool

    Detail thresholds as an aid for improving performance when viewing in 3D. Using these thresholds, the viewer sees varying degrees of detail on the models and graphics in the 3D Graphics window, depending on the distance of the object from the viewer.

.. py:property:: marker
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.marker
    :type: float

    The maximum viewing distance at which a marker representing the object is visible. Uses Distance Dimension.

.. py:property:: marker_label
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.marker_label
    :type: float

    The maximum viewing distance at which a label and marker representing the object is visible. Uses Distance Dimension.

.. py:property:: model_label
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.model_label
    :type: float

    The maximum viewing distance at which the coarsest detail in the model, label and vectors, attitude sphere, and geostationary box is displayed. Uses Distance Dimension.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.Graphics3DDetailThreshold.point
    :type: float

    The maximum viewing distance at which a point representing the object is visible. Uses Distance Dimension.


