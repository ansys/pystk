AntennaSystem
=============

.. py:class:: ansys.stk.core.stkobjects.AntennaSystem

   Class defining an antenna system.

.. py:currentmodule:: AntennaSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaSystem.set_beam_selection_strategy_type`
              - Set the beam selection strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaSystem.antenna_beams`
              - Gets the antenna beam collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaSystem.beam_selection_strategy`
              - Gets the beam selection strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaSystem


Property detail
---------------

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.AntennaSystem.antenna_beams
    :type: AntennaBeamCollection

    Gets the antenna beam collection.

.. py:property:: beam_selection_strategy
    :canonical: ansys.stk.core.stkobjects.AntennaSystem.beam_selection_strategy
    :type: IAntennaBeamSelectionStrategy

    Gets the beam selection strategy.


Method detail
-------------


.. py:method:: set_beam_selection_strategy_type(self, value: BeamSelectionStrategyType) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaSystem.set_beam_selection_strategy_type

    Set the beam selection strategy type.

    :Parameters:

    **value** : :obj:`~BeamSelectionStrategyType`

    :Returns:

        :obj:`~None`


