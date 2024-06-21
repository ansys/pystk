IMaximumCountPathPrimitiveUpdatePolicy
======================================

.. py:class:: ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy

   object
   
   path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

.. py:currentmodule:: IMaximumCountPathPrimitiveUpdatePolicy

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy.maximum_count`
            * - :py:attr:`~ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy.remove_location`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IMaximumCountPathPrimitiveUpdatePolicy


Property detail
---------------

.. py:property:: maximum_count
    :canonical: ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy.maximum_count
    :type: int

    Gets or sets the maximum number of points in the path.

.. py:property:: remove_location
    :canonical: ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy.remove_location
    :type: PATH_PRIMITIVE_REMOVE_LOCATION

    Gets or sets where the positions on the path are removed from.


