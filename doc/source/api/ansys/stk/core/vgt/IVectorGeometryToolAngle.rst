IVectorGeometryToolAngle
========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngle

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
    :type: ANGLE_TYPE

    Returns a type of the angle object.


Method detail
-------------


.. py:method:: find_angle(self, epoch: typing.Any) -> IAngleFindAngleResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle

    Find an angle at the specified epoch.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAngleFindAngleResult`

.. py:method:: find_angle_with_rate(self, epoch: typing.Any) -> IAngleFindAngleWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_angle_with_rate

    Find an angle and angle rate.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAngleFindAngleWithRateResult`

.. py:method:: find_coordinates(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IAngleFindResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates

    Find the angle value and three vectors that define the angle in a specified input axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IAngleFindResult`

.. py:method:: find_coordinates_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IAngleFindWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngle.find_coordinates_with_rate

    Find the angle value, the angle rate and three vectors that define the angle in a specified input axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IAngleFindWithRateResult`

