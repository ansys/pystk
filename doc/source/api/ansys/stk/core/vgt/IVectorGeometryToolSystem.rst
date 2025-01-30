IVectorGeometryToolSystem
=========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolSystem

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
              - Returns a type of the system object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.type
    :type: SystemType

    Returns a type of the system object.


Method detail
-------------


.. py:method:: find_in_system(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> AnalysisWorkbenchSystemFindInSystemResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.find_in_system

    Find position, velocity, rate and orientation using the specified system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~AnalysisWorkbenchSystemFindInSystemResult`

.. py:method:: transform(self, epoch: typing.Any, output_system: IVectorGeometryToolSystem, position_in_my_system: ICartesian3Vector) -> AnalysisWorkbenchSystemTransformResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.transform

    Translate the position vector from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **output_system** : :obj:`~IVectorGeometryToolSystem`
    **position_in_my_system** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~AnalysisWorkbenchSystemTransformResult`

.. py:method:: transform_with_rate(self, epoch: typing.Any, output_system: IVectorGeometryToolSystem, position_in_my_system: ICartesian3Vector, velocity_in_my_system: ICartesian3Vector) -> AnalysisWorkbenchSystemTransformWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.transform_with_rate

    Translate the position and rate vectors from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **output_system** : :obj:`~IVectorGeometryToolSystem`
    **position_in_my_system** : :obj:`~ICartesian3Vector`
    **velocity_in_my_system** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~AnalysisWorkbenchSystemTransformWithRateResult`

