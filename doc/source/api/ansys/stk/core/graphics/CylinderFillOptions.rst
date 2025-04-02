CylinderFillOptions
===================

.. py:class:: ansys.stk.core.graphics.CylinderFillOptions

   IntFlag


.. py:currentmodule:: CylinderFillOptions

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~WALL`
              - Fill the cylinder's wall.

            * - :py:attr:`~BOTTOM_CAP`
              - Fill the cylinder's bottom cap.

            * - :py:attr:`~TOP_CAP`
              - Fill the cylinder's top cap.

            * - :py:attr:`~ALL`
              - Completely fill the cylinder, including its wall, bottom, and top cap.


Examples
--------

Combine enumerations with the logical OR operator

.. code-block:: python

    from ansys.stk.core.graphics import CylinderFillOptions

    # CylinderFillOptions inherits from enum.IntFlag and may be combined
    # using the `|` operator
    cyl_fill = CylinderFillOptions.BOTTOM_CAP | CylinderFillOptions.TOP_CAP


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CylinderFillOptions


