IConstantDisplayCondition
=========================

.. py:class:: IConstantDisplayCondition

   object
   
   A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~display`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IConstantDisplayCondition


Property detail
---------------

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IConstantDisplayCondition.display
    :type: bool

    Gets or sets the value the display condition evaluates to.


