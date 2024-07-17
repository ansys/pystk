RadarCrossSection
=================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSection

   Bases: 

   Class defining a radar cross section.

.. py:currentmodule:: RadarCrossSection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSection.set_model`
              - Set the current RCS model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSection.supported_models`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSection.model`
              - Gets the current RCS model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSection


Property detail
---------------

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.RadarCrossSection.supported_models
    :type: list

    Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.RadarCrossSection.model
    :type: IRadarCrossSectionModel

    Gets the current RCS model.


Method detail
-------------


.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSection.set_model

    Set the current RCS model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


