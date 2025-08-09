ScenarioBeforeSaveEventArguments
================================

.. py:class:: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments

   Contains information about the changes in the object's state.

.. py:currentmodule:: ScenarioBeforeSaveEventArguments

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.path`
              - Scenario file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.continue_save`
              - The status to allow/disallow continue saving.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_as`
              - Saving as user-specified file type and filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_as_vdf`
              - Saving as VDF.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_to_sdf`
              - Do not use this property, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Saving to SDF.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioBeforeSaveEventArguments


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.path
    :type: str

    Scenario file path.

.. py:property:: continue_save
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.continue_save
    :type: bool

    The status to allow/disallow continue saving.

.. py:property:: save_as
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_as
    :type: bool

    Saving as user-specified file type and filename.

.. py:property:: save_as_vdf
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_as_vdf
    :type: bool

    Saving as VDF.

.. py:property:: save_to_sdf
    :canonical: ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments.save_to_sdf
    :type: bool

    Do not use this property, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Saving to SDF.


