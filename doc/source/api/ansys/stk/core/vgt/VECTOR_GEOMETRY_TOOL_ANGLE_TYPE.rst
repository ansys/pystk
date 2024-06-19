VECTOR_GEOMETRY_TOOL_ANGLE_TYPE
===============================

.. py:class:: VECTOR_GEOMETRY_TOOL_ANGLE_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported type.

            * - :py:attr:`~BETWEEN_VECTORS`
              - An angle between two vectors.

            * - :py:attr:`~BETWEEN_PLANES`
              - An angle between two planes.

            * - :py:attr:`~DIHEDRAL_ANGLE`
              - An angle between two vectors about an axis.

            * - :py:attr:`~ROTATION`
              - Angle of the shortest rotation between the two specified axes.

            * - :py:attr:`~TO_PLANE`
              - An angle between a vector and a plane.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT angle created from a template. This type of angle is not creatable.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VECTOR_GEOMETRY_TOOL_ANGLE_TYPE


