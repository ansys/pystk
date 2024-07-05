IVectorGeometryToolAngle
========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngle

   object
   
   The interface defines methods and properties common to all angles.

.. py:currentmodule:: IVectorGeometryToolAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle`
              - Find an angle at the specified epoch.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle_with_rate`
              - Find an angle and angle rate.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates`
              - Find the angle value and three vectors that define the angle in a specified input axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates_with_rate`
              - Find the angle value, the angle rate and three vectors that define the angle in a specified input axes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngle.type`
              - Returns a type of the angle object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngle


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.type
    :type: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE

    Returns a type of the angle object.


Method detail
-------------


.. py:method:: find_angle(self, epoch: typing.Any) -> IVectorGeometryToolAngleFindAngleResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle

    Find an angle at the specified epoch.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAngleFindAngleResult`

.. py:method:: find_angle_with_rate(self, epoch: typing.Any) -> IVectorGeometryToolAngleFindAngleWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle_with_rate

    Find an angle and angle rate.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAngleFindAngleWithRateResult`

.. py:method:: find_coordinates(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolAngleFindResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates

    Find the angle value and three vectors that define the angle in a specified input axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolAngleFindResult`

.. py:method:: find_coordinates_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolAngleFindWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates_with_rate

    Find the angle value, the angle rate and three vectors that define the angle in a specified input axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolAngleFindWithRateResult`

