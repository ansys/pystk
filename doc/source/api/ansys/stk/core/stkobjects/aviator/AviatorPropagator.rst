AviatorPropagator
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.AviatorPropagator

   Bases: 

   Class defining the Aviator propagator.

.. py:currentmodule:: AviatorPropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.propagate`
              - Apply All Change.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_mission`
              - Get the Aviator mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.auto_recalculate`
              - Opt whether to have the propagator auto recalculate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_catalog`
              - Get the Aviator catalog.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AviatorPropagator


Property detail
---------------

.. py:property:: aviator_mission
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_mission
    :type: IMission

    Get the Aviator mission.

.. py:property:: auto_recalculate
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.auto_recalculate
    :type: bool

    Opt whether to have the propagator auto recalculate.

.. py:property:: aviator_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_catalog
    :type: ICatalog

    Get the Aviator catalog.


Method detail
-------------


.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.propagate

    Apply All Change.

    :Returns:

        :obj:`~None`




