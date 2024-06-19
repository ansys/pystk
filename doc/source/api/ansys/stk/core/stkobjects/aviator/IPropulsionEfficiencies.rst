IPropulsionEfficiencies
=======================

.. py:class:: IPropulsionEfficiencies

   object
   
   Interface used to access the options for the Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~technology_level`
            * - :py:meth:`~intake_type`
            * - :py:meth:`~turbine_type`
            * - :py:meth:`~exhaust_nozzle_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPropulsionEfficiencies


Property detail
---------------

.. py:property:: technology_level
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionEfficiencies.technology_level
    :type: JET_ENGINE_TECHNOLOGY_LEVEL

    Gets or sets the technology level of the jet engine.

.. py:property:: intake_type
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionEfficiencies.intake_type
    :type: JET_ENGINE_INTAKE_TYPE

    Gets or sets the jet engine intake type.

.. py:property:: turbine_type
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionEfficiencies.turbine_type
    :type: JET_ENGINE_TURBINE_TYPE

    Gets or sets the jet engine turbine type.

.. py:property:: exhaust_nozzle_type
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionEfficiencies.exhaust_nozzle_type
    :type: JET_ENGINE_EXHAUST_NOZZLE_TYPE

    Gets or sets the jet engine exhaust nozzle type.


