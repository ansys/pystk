VectorGeometryToolAngleFactory
==============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory

   A Factory object to create angles.

.. py:currentmodule:: VectorGeometryToolAngleFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory.create`
              - Create a VGT angle using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory.is_type_supported`
              - Return true if the type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAngleFactory



Method detail
-------------

.. py:method:: create(self, angle_name: str, description: str, angle_type: AngleType) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory.create

    Create a VGT angle using specified name, description and type.

    :Parameters:

        **angle_name** : :obj:`~str`

        **description** : :obj:`~str`

        **angle_type** : :obj:`~AngleType`


    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: is_type_supported(self, type: AngleType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory.is_type_supported

    Return true if the type is supported.

    :Parameters:

        **type** : :obj:`~AngleType`


    :Returns:

        :obj:`~bool`

