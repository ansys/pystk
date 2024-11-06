LaserTroposphericScintillationLossModelITURP1814
================================================

.. py:class:: ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILaserTroposphericScintillationLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

.. py:currentmodule:: LaserTroposphericScintillationLossModelITURP1814

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.set_atmospheric_turbulence_model_type`
              - Set the atmospheric turbulence model type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.atmospheric_turbulence_model`
              - Gets the atmospheric turbulence model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaserTroposphericScintillationLossModelITURP1814


Property detail
---------------

.. py:property:: atmospheric_turbulence_model
    :canonical: ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.atmospheric_turbulence_model
    :type: IAtmosphericTurbulenceModel

    Gets the atmospheric turbulence model.


Method detail
-------------

.. py:method:: set_atmospheric_turbulence_model_type(self, value: ATMOSPHERIC_TURBULENCE_MODEL_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.set_atmospheric_turbulence_model_type

    Set the atmospheric turbulence model type.

    :Parameters:

    **value** : :obj:`~ATMOSPHERIC_TURBULENCE_MODEL_TYPE`

    :Returns:

        :obj:`~None`


