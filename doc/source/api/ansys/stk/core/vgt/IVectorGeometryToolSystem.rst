IVectorGeometryToolSystem
=========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolSystem

   object
   
   The interface contains methods and properties shared by all VGT systems.

.. py:currentmodule:: IVectorGeometryToolSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystem.find_in_system`
              - Find position, velocity, rate and orientation using the specified system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystem.transform`
              - Translate the position vector from this system into the output system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystem.transform_with_rate`
              - Translate the position and rate vectors from this system into the output system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystem.type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.type
    :type: CRDN_SYSTEM_TYPE

    Returns a type of the system object.


Method detail
-------------


.. py:method:: find_in_system(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> IVectorGeometryToolSystemFindInSystemResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.find_in_system

    Find position, velocity, rate and orientation using the specified system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~IVectorGeometryToolSystemFindInSystemResult`

.. py:method:: transform(self, epoch: typing.Any, outputSystem: IVectorGeometryToolSystem, positionInMySystem: ICartesian3Vector) -> IVectorGeometryToolSystemTransformResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.transform

    Translate the position vector from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputSystem** : :obj:`~IVectorGeometryToolSystem`
    **positionInMySystem** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~IVectorGeometryToolSystemTransformResult`

.. py:method:: transform_with_rate(self, epoch: typing.Any, outputSystem: IVectorGeometryToolSystem, positionInMySystem: ICartesian3Vector, velocityInMySystem: ICartesian3Vector) -> IVectorGeometryToolSystemTransformWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.transform_with_rate

    Translate the position and rate vectors from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputSystem** : :obj:`~IVectorGeometryToolSystem`
    **positionInMySystem** : :obj:`~ICartesian3Vector`
    **velocityInMySystem** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~IVectorGeometryToolSystemTransformWithRateResult`

