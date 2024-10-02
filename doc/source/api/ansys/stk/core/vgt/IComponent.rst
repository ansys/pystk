IComponent
==========

.. py:class:: ansys.stk.core.vgt.IComponent

   A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

.. py:currentmodule:: IComponent

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IComponent.duplicate`
              - Create a copy of the instance of a VGT component. The new component is automatically registered and will be persisted or restored when a scenario is saved or loaded.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.anonymous_duplicate`
              - Create an anonymous copy of the instance of a VGT component. The new component is not registered and will not be persisted nor restored when a scenario is saved or loaded.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.depends_on`
              - Test if the instance depends on another component.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.export`
              - Export the component to a file.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.rename`
              - Rename the component.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IComponent.component_type`
              - Returns the component kind.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.category`
              - Allows the user to access or change the component category (Folder).
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.name`
              - Returns the component name.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.description`
              - Returns the component description.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.path`
              - Returns the component's fully qualified path (ie. \"CentralBody/Earth Body\", etc.).
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.is_duplicable`
              - Returns whether the VGT component can be duplicated.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.context`
              - Returns the context object associated with the instance. The returned object is either an instance of IAgCrdnInstance or IAgCrdnTemplate interface.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.type_information`
              - Returns the component type information.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.qualified_path`
              - An STK-conformant path to the VGT component that can be used to visualize the VGT components in 3D (i.e. \"CentralBody/Earth Body Vector\", etc.).
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.is_valid`
              - Returns whether the component is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.is_ready`
              - Returns whether the component is ready. The component is ready if it's been fully initialized.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.is_read_only`
              - Returns whether the component is modifiable.
            * - :py:attr:`~ansys.stk.core.vgt.IComponent.embedded_components`
              - Returns a collection of embedded components.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IComponent


Property detail
---------------

.. py:property:: component_type
    :canonical: ansys.stk.core.vgt.IComponent.component_type
    :type: VECTOR_GEOMETRY_TOOL_COMPONENT_TYPE

    Returns the component kind.

.. py:property:: category
    :canonical: ansys.stk.core.vgt.IComponent.category
    :type: str

    Allows the user to access or change the component category (Folder).

.. py:property:: name
    :canonical: ansys.stk.core.vgt.IComponent.name
    :type: str

    Returns the component name.

.. py:property:: description
    :canonical: ansys.stk.core.vgt.IComponent.description
    :type: str

    Returns the component description.

.. py:property:: path
    :canonical: ansys.stk.core.vgt.IComponent.path
    :type: str

    Returns the component's fully qualified path (ie. \"CentralBody/Earth Body\", etc.).

.. py:property:: is_duplicable
    :canonical: ansys.stk.core.vgt.IComponent.is_duplicable
    :type: bool

    Returns whether the VGT component can be duplicated.

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IComponent.context
    :type: IComponentContext

    Returns the context object associated with the instance. The returned object is either an instance of IAgCrdnInstance or IAgCrdnTemplate interface.

.. py:property:: type_information
    :canonical: ansys.stk.core.vgt.IComponent.type_information
    :type: AnalysisWorkbenchComponentTypeInformation

    Returns the component type information.

.. py:property:: qualified_path
    :canonical: ansys.stk.core.vgt.IComponent.qualified_path
    :type: str

    An STK-conformant path to the VGT component that can be used to visualize the VGT components in 3D (i.e. \"CentralBody/Earth Body Vector\", etc.).

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IComponent.is_valid
    :type: bool

    Returns whether the component is valid.

.. py:property:: is_ready
    :canonical: ansys.stk.core.vgt.IComponent.is_ready
    :type: bool

    Returns whether the component is ready. The component is ready if it's been fully initialized.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.vgt.IComponent.is_read_only
    :type: bool

    Returns whether the component is modifiable.

.. py:property:: embedded_components
    :canonical: ansys.stk.core.vgt.IComponent.embedded_components
    :type: AnalysisWorkbenchComponentCollection

    Returns a collection of embedded components.


Method detail
-------------














.. py:method:: duplicate(self, newName: str, description: str) -> IComponent
    :canonical: ansys.stk.core.vgt.IComponent.duplicate

    Create a copy of the instance of a VGT component. The new component is automatically registered and will be persisted or restored when a scenario is saved or loaded.

    :Parameters:

    **newName** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~IComponent`

.. py:method:: anonymous_duplicate(self) -> IComponent
    :canonical: ansys.stk.core.vgt.IComponent.anonymous_duplicate

    Create an anonymous copy of the instance of a VGT component. The new component is not registered and will not be persisted nor restored when a scenario is saved or loaded.

    :Returns:

        :obj:`~IComponent`

.. py:method:: depends_on(self, component: IComponent) -> bool
    :canonical: ansys.stk.core.vgt.IComponent.depends_on

    Test if the instance depends on another component.

    :Parameters:

    **component** : :obj:`~IComponent`

    :Returns:

        :obj:`~bool`


.. py:method:: export(self, filename: str, comments: str) -> None
    :canonical: ansys.stk.core.vgt.IComponent.export

    Export the component to a file.

    :Parameters:

    **filename** : :obj:`~str`
    **comments** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: rename(self, newName: str) -> None
    :canonical: ansys.stk.core.vgt.IComponent.rename

    Rename the component.

    :Parameters:

    **newName** : :obj:`~str`

    :Returns:

        :obj:`~None`

