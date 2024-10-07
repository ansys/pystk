IAutomationStrategyFactory
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAutomationStrategyFactory

   Interface used to send connect commands to Aviator objects.

.. py:currentmodule:: IAutomationStrategyFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAutomationStrategyFactory.construct_strategy`
              - Construct the strategy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAutomationStrategyFactory



Method detail
-------------

.. py:method:: construct_strategy(self, pUnk: IUnknown) -> IBasicManeuverStrategy
    :canonical: ansys.stk.core.stkobjects.aviator.IAutomationStrategyFactory.construct_strategy

    Construct the strategy.

    :Parameters:

    **pUnk** : :obj:`~IUnknown`

    :Returns:

        :obj:`~IBasicManeuverStrategy`

