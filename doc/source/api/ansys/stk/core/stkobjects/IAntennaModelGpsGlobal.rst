IAntennaModelGpsGlobal
======================

.. py:class:: IAntennaModelGpsGlobal

   object
   
   Provide access to the properties and methods defining a GPS global antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_block_types`
            * - :py:meth:`~block_type`
            * - :py:meth:`~efficiency`
            * - :py:meth:`~max_gain`
            * - :py:meth:`~beamwidth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelGpsGlobal


Property detail
---------------

.. py:property:: supported_block_types
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGpsGlobal.supported_block_types
    :type: list

    Gets an array of supported block types.

.. py:property:: block_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGpsGlobal.block_type
    :type: str

    Gets or sets the block type.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGpsGlobal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: max_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGpsGlobal.max_gain
    :type: float

    Gets the maximum gain.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelGpsGlobal.beamwidth
    :type: typing.Any

    Gets the beamwidth.


