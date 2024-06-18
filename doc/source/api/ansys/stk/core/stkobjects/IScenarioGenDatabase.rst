IScenarioGenDatabase
====================

.. py:class:: IScenarioGenDatabase

   object
   
   Represents a scenario database.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~default_database`
            * - :py:meth:`~default_direction`
            * - :py:meth:`~enable_aux_database`
            * - :py:meth:`~aux_database`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioGenDatabase


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabase.type
    :type: str

    The type of objects in the database.

.. py:property:: default_database
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabase.default_database
    :type: str

    The default database file.

.. py:property:: default_direction
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabase.default_direction
    :type: str

    The default directory of the database file.

.. py:property:: enable_aux_database
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabase.enable_aux_database
    :type: bool

    Enable the auxiliary database.

.. py:property:: aux_database
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabase.aux_database
    :type: str

    The auxiliary database file.


