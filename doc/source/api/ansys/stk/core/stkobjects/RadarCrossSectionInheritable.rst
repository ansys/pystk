RadarCrossSectionInheritable
============================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionInheritable

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
              - Do not use this method, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Sets the current RCS model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.inherit`
              - Get or set the option to inherit the radar cross section from the scenario object.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.supported_models`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model`
              - Do not use this property, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Gets the current RCS model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model_component_linking`
              - Get the link/embed controller for managing the radar cross section model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionInheritable


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.inherit
    :type: bool

    Get or set the option to inherit the radar cross section from the scenario object.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.supported_models
    :type: list

    Do not use this property, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model
    :type: RadarCrossSectionModel

    Do not use this property, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Gets the current RCS model.

.. py:property:: model_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar cross section model component.


Method detail
-------------




.. py:method:: set_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionInheritable.set_model

    Do not use this method, as it is deprecated. Use ModelComponentLinking on RadarCrossSectionInheritable instead. Sets the current RCS model by name.

    :Parameters:

        **model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



