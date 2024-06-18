IBoundingSphere
===============

.. py:class:: IBoundingSphere

   object
   
   A sphere that encapsulates an object.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~center`
            * - :py:meth:`~radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBoundingSphere


Property detail
---------------

.. py:property:: center
    :canonical: ansys.stk.core.graphics.IBoundingSphere.center
    :type: list

    A center of the bounding sphere. The center point is specified as one-dimensional array with three elements corresponding to (X,Y,Z) cartesian coordinates.

.. py:property:: radius
    :canonical: ansys.stk.core.graphics.IBoundingSphere.radius
    :type: float

    A radius of the bounding sphere.


