IVectorGeometryToolSystem
=========================

.. py:class:: IVectorGeometryToolSystem

   object
   
   The interface contains methods and properties shared by all VGT systems.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_in_system`
              - Find position, velocity, rate and orientation using the specified system.
            * - :py:meth:`~transform`
              - Translate the position vector from this system into the output system.
            * - :py:meth:`~transform_with_rate`
              - Translate the position and rate vectors from this system into the output system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystem.type
    :type: "CRDN_SYSTEM_TYPE"

    Returns a type of the system object.


Method detail
-------------


.. py:method:: find_in_system(self, epoch:typing.Any, system:"IVectorGeometryToolSystem") -> "IVectorGeometryToolSystemFindInSystemResult"

    Find position, velocity, rate and orientation using the specified system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~"IVectorGeometryToolSystemFindInSystemResult"`

.. py:method:: transform(self, epoch:typing.Any, outputSystem:"IVectorGeometryToolSystem", positionInMySystem:"ICartesian3Vector") -> "IVectorGeometryToolSystemTransformResult"

    Translate the position vector from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputSystem** : :obj:`~"IVectorGeometryToolSystem"`
    **positionInMySystem** : :obj:`~"ICartesian3Vector"`

    :Returns:

        :obj:`~"IVectorGeometryToolSystemTransformResult"`

.. py:method:: transform_with_rate(self, epoch:typing.Any, outputSystem:"IVectorGeometryToolSystem", positionInMySystem:"ICartesian3Vector", velocityInMySystem:"ICartesian3Vector") -> "IVectorGeometryToolSystemTransformWithRateResult"

    Translate the position and rate vectors from this system into the output system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputSystem** : :obj:`~"IVectorGeometryToolSystem"`
    **positionInMySystem** : :obj:`~"ICartesian3Vector"`
    **velocityInMySystem** : :obj:`~"ICartesian3Vector"`

    :Returns:

        :obj:`~"IVectorGeometryToolSystemTransformWithRateResult"`

