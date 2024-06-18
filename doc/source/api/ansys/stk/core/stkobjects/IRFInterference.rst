IRFInterference
===============

.. py:class:: IRFInterference

   object
   
   Provide access to the properties and methods defining a radio frequency interference.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enabled`
            * - :py:meth:`~include_active_comm_system_interference_emitters`
            * - :py:meth:`~emitters`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRFInterference


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IRFInterference.enabled
    :type: bool

    Gets or sets whether the interference is enabled or disabled.

.. py:property:: include_active_comm_system_interference_emitters
    :canonical: ansys.stk.core.stkobjects.IRFInterference.include_active_comm_system_interference_emitters
    :type: bool

    Gets or sets whether the emitters from the active CommSystem object are included in their interference computation.

.. py:property:: emitters
    :canonical: ansys.stk.core.stkobjects.IRFInterference.emitters
    :type: "IAgObjectLinkCollection"

    Gets the interference emitters collection.


