IElement
========

.. py:class:: IElement

   object
   
   Provide access to the properties and methods defining a phased array element.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~x`
            * - :py:meth:`~y`
            * - :py:meth:`~id`
            * - :py:meth:`~enabled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElement


Property detail
---------------

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.IElement.x
    :type: float

    Gets the x position, in wavelengths.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.IElement.y
    :type: float

    Gets the y position, in wavelengths.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IElement.id
    :type: int

    Gets the element Id.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IElement.enabled
    :type: bool

    Gets or set whether or not the element is enabled.


