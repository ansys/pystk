RadarCrossSectionInheritable
============================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionInheritable

   Bases: 

   Class defining a inheritable radar cross section.

.. py:currentmodule:: RadarCrossSectionInheritable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.set_model`
              - Set the current RCS model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.inherit`
              - Gets or set the option to inherit the radar cross section from the scenario object.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model`
              - Gets the current RCS model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionInheritable


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.inherit
    :type: bool

    Gets or set the option to inherit the radar cross section from the scenario object.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model
    :type: IRadarCrossSectionModel

    Gets the current RCS model.


Method detail
-------------




.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.set_model

    Set the current RCS model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


