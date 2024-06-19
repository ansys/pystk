IAviatorPropagator
==================

.. py:class:: IAviatorPropagator

   object
   
   Interface used to access the Aviator interface for an aircraft. Use this interface to get the mission or Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Apply All Change.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~avtr_mission`
            * - :py:meth:`~auto_recalculate`
            * - :py:meth:`~avtr_catalog`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAviatorPropagator


Property detail
---------------

.. py:property:: avtr_mission
    :canonical: ansys.stk.core.stkobjects.aviator.IAviatorPropagator.avtr_mission
    :type: IAgAvtrMission

    Get the Aviator mission.

.. py:property:: auto_recalculate
    :canonical: ansys.stk.core.stkobjects.aviator.IAviatorPropagator.auto_recalculate
    :type: bool

    Opt whether to have the propagator auto recalculate.

.. py:property:: avtr_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.IAviatorPropagator.avtr_catalog
    :type: IAgAvtrCatalog

    Get the Aviator catalog.


Method detail
-------------


.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAviatorPropagator.propagate

    Apply All Change.

    :Returns:

        :obj:`~None`




