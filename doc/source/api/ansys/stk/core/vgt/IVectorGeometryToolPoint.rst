IVectorGeometryToolPoint
========================

.. py:class:: IVectorGeometryToolPoint

   object
   
   The interface defines methods and properties common to all points.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~locate_in_system_with_rate`
              - Locates the point's position and velocity in a specified coordinate system.
            * - :py:meth:`~locate_in_system`
              - Locates the point's position in a specified coordinate system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPoint


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPoint.type
    :type: "VECTOR_GEOMETRY_TOOL_POINT_TYPE"

    Returns a type of the point object.


Method detail
-------------


.. py:method:: locate_in_system_with_rate(self, epoch:typing.Any, system:"IVectorGeometryToolSystem") -> "IVectorGeometryToolPointLocateInSystemWithRateResult"

    Locates the point's position and velocity in a specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~"IVectorGeometryToolPointLocateInSystemWithRateResult"`

.. py:method:: locate_in_system(self, epoch:typing.Any, system:"IVectorGeometryToolSystem") -> "IVectorGeometryToolPointLocateInSystemResult"

    Locates the point's position in a specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~"IVectorGeometryToolPointLocateInSystemResult"`

