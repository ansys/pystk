ConstantDisplayCondition
========================

.. py:class:: ansys.stk.core.graphics.ConstantDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

.. py:currentmodule:: ConstantDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ConstantDisplayCondition.display`
              - Get or set the value the display condition evaluates to.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ConstantDisplayCondition


Property detail
---------------

.. py:property:: display
    :canonical: ansys.stk.core.graphics.ConstantDisplayCondition.display
    :type: bool

    Get or set the value the display condition evaluates to.


