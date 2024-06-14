IAntennaSystem
==============

.. py:class:: IAntennaSystem

   object
   
   Provide access to the properties for a antenna system.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_beam_selection_strategy_type`
              - Set the beam selection strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~antenna_beams`
            * - :py:meth:`~beam_selection_strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaSystem


Property detail
---------------

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.IAntennaSystem.antenna_beams
    :type: "IAgAntennaBeamCollection"

    Gets the antenna beam collection.

.. py:property:: beam_selection_strategy
    :canonical: ansys.stk.core.stkobjects.IAntennaSystem.beam_selection_strategy
    :type: "IAgAntennaBeamSelectionStrategy"

    Gets the beam selection strategy.


Method detail
-------------


.. py:method:: set_beam_selection_strategy_type(self, val:"BEAM_SELECTION_STRATEGY_TYPE") -> None

    Set the beam selection strategy type.

    :Parameters:

    **val** : :obj:`~"BEAM_SELECTION_STRATEGY_TYPE"`

    :Returns:

        :obj:`~None`


