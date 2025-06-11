DurationPathPrimitiveUpdatePolicy
=================================

.. py:class:: ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy

   Bases: :py:class:`~ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy`

   path primitive update policy that removes points from remove location after a given duration.

.. py:currentmodule:: DurationPathPrimitiveUpdatePolicy

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy.duration`
              - Get or set the maximum duration that a point will lie on the line.
            * - :py:attr:`~ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy.remove_location`
              - Get or set where the positions on the path are removed from.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DurationPathPrimitiveUpdatePolicy


Property detail
---------------

.. py:property:: duration
    :canonical: ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy.duration
    :type: float

    Get or set the maximum duration that a point will lie on the line.

.. py:property:: remove_location
    :canonical: ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy.remove_location
    :type: PathPrimitiveRemoveLocation

    Get or set where the positions on the path are removed from.


