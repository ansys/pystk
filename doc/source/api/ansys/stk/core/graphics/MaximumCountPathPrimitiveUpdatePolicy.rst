MaximumCountPathPrimitiveUpdatePolicy
=====================================

.. py:class:: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy

   Bases: :py:class:`~ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy`

   path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

.. py:currentmodule:: MaximumCountPathPrimitiveUpdatePolicy

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy.maximum_count`
              - Gets or sets the maximum number of points in the path.
            * - :py:attr:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy.remove_location`
              - Gets or sets where the positions on the path are removed from.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MaximumCountPathPrimitiveUpdatePolicy


Property detail
---------------

.. py:property:: maximum_count
    :canonical: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy.maximum_count
    :type: int

    Gets or sets the maximum number of points in the path.

.. py:property:: remove_location
    :canonical: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy.remove_location
    :type: PathPrimitiveRemoveLocation

    Gets or sets where the positions on the path are removed from.


