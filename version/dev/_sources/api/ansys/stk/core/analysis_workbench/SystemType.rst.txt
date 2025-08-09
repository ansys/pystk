SystemType
==========

.. py:class:: ansys.stk.core.analysis_workbench.SystemType

   IntEnum


.. py:currentmodule:: SystemType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported system type.

            * - :py:attr:`~ASSEMBLED`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:attr:`~ON_SURFACE`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT system created from a template. This type of system is not creatable.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SystemType


