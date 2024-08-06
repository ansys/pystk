IReceiverModelScriptPlugin
==========================

.. py:class:: ansys.stk.core.stkobjects.IReceiverModelScriptPlugin

   Provide access to the properties and methods defining a script plugin receiver model.

.. py:currentmodule:: IReceiverModelScriptPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelScriptPlugin.filename`
              - Gets or sets the script plugin filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelScriptPlugin.link_margin`
              - Gets the interface for configuring the link margin computation parameters.


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
    :type: LinkMargin

    Gets the interface for configuring the link margin computation parameters.


