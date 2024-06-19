IGreatArcGraphics3D
===================

.. py:class:: IGreatArcGraphics3D

   object
   
   3D Graphics common for all Great Arc Vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model`
            * - :py:meth:`~route`
            * - :py:meth:`~offsets`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~covariance`
            * - :py:meth:`~vector`
            * - :py:meth:`~data_display`
            * - :py:meth:`~model_pointing`
            * - :py:meth:`~velocity_covariance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGreatArcGraphics3D


Property detail
---------------

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.model
    :type: IAgVeRouteVOModel

    Get the vehicle's 3D model properties.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.route
    :type: IAgVeVORoute

    Get the vehicle's 3D route properties.

.. py:property:: offsets
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.offsets
    :type: IAgVOOffset

    Get the vehicle's 3D offsets properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.range_contours
    :type: IAgVORangeContours

    Get the vehicle's 3D range contour properties.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.covariance
    :type: IAgVeVOCovariance

    Get the vehicle's 3D covariance properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.vector
    :type: IAgVOVector

    Get the vehicle's 3D vector properties.

.. py:property:: data_display
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.data_display
    :type: IAgVODataDisplayCollection

    Get the vehicle's 3D data display properties.

.. py:property:: model_pointing
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.model_pointing
    :type: IAgVOModelPointing

    Use to point parts of a facility or vehicle model toward a target, such as the Sun or Earth.

.. py:property:: velocity_covariance
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics3D.velocity_covariance
    :type: IAgVeVOVelCovariance

    Get the vehicle's 3D velocity covariance properties.


