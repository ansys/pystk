ISensorGraphics3DProjectionElement
==================================

.. py:class:: ansys.stk.core.stkobjects.ISensorGraphics3DProjectionElement

   object
   
   Represents elements of the space and target projection collections.

.. py:currentmodule:: ISensorGraphics3DProjectionElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics3DProjectionElement.time`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorGraphics3DProjectionElement.distance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorGraphics3DProjectionElement


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DProjectionElement.time
    :type: typing.Any

    Time used together with distance to compute the space projection. Uses DateFormat Dimension.

.. py:property:: distance
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3DProjectionElement.distance
    :type: float

    Distance used together with time to compute the space projection. Uses Distance Dimension.


