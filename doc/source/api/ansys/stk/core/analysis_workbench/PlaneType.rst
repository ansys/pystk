PlaneType
=========

.. py:class:: ansys.stk.core.analysis_workbench.PlaneType

   IntEnum


.. py:currentmodule:: PlaneType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported type.

            * - :py:attr:`~NORMAL`
              - A plane normal to a vector at a given point.

            * - :py:attr:`~QUADRANT`
              - A plane is defined by the quadrant from a Reference System (e.g., XY, XZ, YZ, YX, ZX, ZY). The reference point in all cases is the origin of the coordinate system.

            * - :py:attr:`~TRAJECTORY`
              - A plane is defined on the basis of a trajectory of a selected point with respect to a reference point.

            * - :py:attr:`~TRIAD`
              - A plane is defined by the three points.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT plane created from a template. This type of plane is not creatable.

            * - :py:attr:`~TWO_VECTOR`
              - A plane passing through point and containing two given vectors.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import PlaneType


