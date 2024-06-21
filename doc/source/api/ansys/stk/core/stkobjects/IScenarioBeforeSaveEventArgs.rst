IScenarioBeforeSaveEventArgs
============================

.. py:class:: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs

   object
   
   Contains information about the changes in the object's state.

.. py:currentmodule:: IScenarioBeforeSaveEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.path`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.continue_save`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.save_as`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.vdf_save`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.sdf_save`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioBeforeSaveEventArgs


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.path
    :type: str

    Scenario file path.

.. py:property:: continue_save
    :canonical: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.continue_save
    :type: bool

    The status to allow/disallow continue saving.

.. py:property:: save_as
    :canonical: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.save_as
    :type: bool

    Saving as user-specified file type and filename.

.. py:property:: vdf_save
    :canonical: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.vdf_save
    :type: bool

    Saving as VDF.

.. py:property:: sdf_save
    :canonical: ansys.stk.core.stkobjects.IScenarioBeforeSaveEventArgs.sdf_save
    :type: bool

    Saving to SDF.


