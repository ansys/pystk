IAntennaSystem
==============

.. py:class:: ansys.stk.core.stkobjects.IAntennaSystem

   object
   
   Provide access to the properties for a antenna system.

.. py:currentmodule:: IAntennaSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaSystem.set_beam_selection_strategy_type`
              - Set the beam selection strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaSystem.antenna_beams`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaSystem.beam_selection_strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaSystem


Property detail
---------------

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.IAntennaSystem.antenna_beams
    :type: IAntennaBeamCollection

    Gets the antenna beam collection.

.. py:property:: beam_selection_strategy
    :canonical: ansys.stk.core.stkobjects.IAntennaSystem.beam_selection_strategy
    :type: IAntennaBeamSelectionStrategy

    Gets the beam selection strategy.


Method detail
-------------


.. py:method:: set_beam_selection_strategy_type(self, val: BEAM_SELECTION_STRATEGY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaSystem.set_beam_selection_strategy_type

    Set the beam selection strategy type.

    :Parameters:

    **val** : :obj:`~BEAM_SELECTION_STRATEGY_TYPE`

    :Returns:

        :obj:`~None`


