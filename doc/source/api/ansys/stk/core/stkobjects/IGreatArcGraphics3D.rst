IGreatArcGraphics3D
===================

.. py:class:: ansys.stk.core.stkobjects.IGreatArcGraphics3D

   object
   
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
    :type: IVehicleRouteGraphics3DModel

    Get the vehicle's 3D model properties.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.route
    :type: IVehicleGraphics3DRoute

    Get the vehicle's 3D route properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.offsets
    :type: IGraphics3DOffset

    Get the vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.range_contours
    :type: IGraphics3DRangeContours

    Get the vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.covariance
    :type: IVehicleGraphics3DCovariance

    Get the vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.vector
    :type: IGraphics3DVector

    Get the vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.data_display
    :type: IGraphics3DDataDisplayCollection

    Get the vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.model_pointing
    :type: IGraphics3DModelPointing

    Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.velocity_covariance
    :type: IVehicleGraphics3DVelCovariance

    Get the vehicle's 3D velocity covariance properties.


