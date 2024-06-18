ICompositeDisplayConditionFactory
=================================

.. py:class:: ICompositeDisplayConditionFactory

   object
   
   A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize an empty composite display condition.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICompositeDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> "ICompositeDisplayCondition"

    Initialize an empty composite display condition.

    :Returns:

        :obj:`~"ICompositeDisplayCondition"`

