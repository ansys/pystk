MilitaryStandard2525bSymbols
============================

.. py:class:: ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols

   AgStdMil2525bSymbols class provides methods to create 2525b symbols.

.. py:currentmodule:: MilitaryStandard2525bSymbols

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.create_symbol`
              - Generate a 2525b symbol. Image will be saved to the file specified by SaveImageFilePath.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.fill_enabled`
              - Turn on or off the fill for symbol id.
            * - :py:attr:`~ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.symbol_image_size`
              - Gets or sets the size for the symbol id. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MilitaryStandard2525bSymbols


Property detail
---------------

.. py:property:: fill_enabled
    :canonical: ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.fill_enabled
    :type: bool

    Turn on or off the fill for symbol id.

.. py:property:: symbol_image_size
    :canonical: ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.symbol_image_size
    :type: int

    Gets or sets the size for the symbol id. Dimensionless.


Method detail
-------------





.. py:method:: create_symbol(self, symbolID: str, saveImageFilePath: str) -> None
    :canonical: ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols.create_symbol

    Generate a 2525b symbol. Image will be saved to the file specified by SaveImageFilePath.

    :Parameters:

    **symbolID** : :obj:`~str`
    **saveImageFilePath** : :obj:`~str`

    :Returns:

        :obj:`~None`

