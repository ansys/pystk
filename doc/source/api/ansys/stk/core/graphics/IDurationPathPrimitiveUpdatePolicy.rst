IDurationPathPrimitiveUpdatePolicy
==================================

.. py:class:: IDurationPathPrimitiveUpdatePolicy

   object
   
   path primitive update policy that removes points from remove location after a given duration.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~duration`
            * - :py:meth:`~remove_location`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDurationPathPrimitiveUpdatePolicy


Property detail
---------------

.. py:property:: duration
    :canonical: ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicy.duration
    :type: float

    Gets or sets the maximum duration that a point will lie on the line.

.. py:property:: remove_location
    :canonical: ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicy.remove_location
    :type: PATH_PRIMITIVE_REMOVE_LOCATION

    Gets or sets where the positions on the path are removed from.


