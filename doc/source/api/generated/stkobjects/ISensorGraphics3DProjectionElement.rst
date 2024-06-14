ISensorGraphics3DProjectionElement
==================================

.. py:class:: ISensorGraphics3DProjectionElement

   object
   
   Represents elements of the space and target projection collections.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time`
            * - :py:meth:`~distance`


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


