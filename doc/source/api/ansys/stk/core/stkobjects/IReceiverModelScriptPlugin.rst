IReceiverModelScriptPlugin
==========================

.. py:class:: IReceiverModelScriptPlugin

   object
   
   Provide access to the properties and methods defining a script plugin receiver model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~link_margin`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverModelScriptPlugin


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IReceiverModelScriptPlugin.filename
    :type: str

    Gets or sets the script plugin filename.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelScriptPlugin.link_margin
    :type: IAgLinkMargin

    Gets the interface for configuring the link margin computation parameters.


