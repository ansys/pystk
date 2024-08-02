IGreatArcGraphics3D
===================

.. py:class:: ansys.stk.core.stkobjects.IGreatArcGraphics3D

   3D Graphics common for all Great Arc Vehicles.

.. py:currentmodule:: IGreatArcGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.model`
              - Get the vehicle's 3D model properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.route`
              - Get the vehicle's 3D route properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.offsets`
              - Get the vehicle's 3D offsets properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.range_contours`
              - Get the vehicle's 3D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.covariance`
              - Get the vehicle's 3D covariance properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.vector`
              - Get the vehicle's 3D vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.data_display`
              - Get the vehicle's 3D data display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.model_pointing`
              - Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D.velocity_covariance`
              - Get the vehicle's 3D velocity covariance properties.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGreatArcGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.model
    :type: VehicleRouteGraphics3DModel

    Get the vehicle's 3D model properties.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.route
    :type: VehicleGraphics3DRoute

    Get the vehicle's 3D route properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.offsets
    :type: Graphics3DOffset

    Get the vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Get the vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.covariance
    :type: VehicleGraphics3DCovariance

    Get the vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.vector
    :type: Graphics3DVector

    Get the vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.data_display
    :type: Graphics3DDataDisplayCollection

    Get the vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.velocity_covariance
    :type: VehicleGraphics3DVelCovariance

    Get the vehicle's 3D velocity covariance properties.


