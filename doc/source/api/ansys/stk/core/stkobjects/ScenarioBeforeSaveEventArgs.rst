ScenarioBeforeSaveEventArgs
===========================

.. py:class:: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs

   Contains information about the changes in the object's state.

.. py:currentmodule:: ScenarioBeforeSaveEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.path`
              - Scenario file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.continue_save`
              - The status to allow/disallow continue saving.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.save_as`
              - Saving as user-specified file type and filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.vdf_save`
              - Saving as VDF.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.sdf_save`
              - Saving to SDF.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioBeforeSaveEventArgs


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.path
    :type: str

    Scenario file path.

.. py:property:: continue_save
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.continue_save
    :type: bool

    The status to allow/disallow continue saving.

.. py:property:: save_as
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.save_as
    :type: bool

    Saving as user-specified file type and filename.

.. py:property:: vdf_save
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.vdf_save
    :type: bool

    Saving as VDF.

.. py:property:: sdf_save
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs.sdf_save
    :type: bool

    Saving to SDF.


