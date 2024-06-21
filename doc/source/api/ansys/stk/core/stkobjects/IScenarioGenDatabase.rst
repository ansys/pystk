IScenarioGenDatabase
====================

.. py:class:: ansys.stk.core.stkobjects.IScenarioGenDatabase

   object
   
   Represents a scenario database.

.. py:currentmodule:: IScenarioGenDatabase

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabase.type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabase.default_database`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabase.default_direction`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabase.enable_aux_database`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabase.aux_database`


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


