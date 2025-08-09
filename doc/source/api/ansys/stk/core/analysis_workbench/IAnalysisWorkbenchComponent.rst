IAnalysisWorkbenchComponent
===========================

.. py:class:: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent

   A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

.. py:currentmodule:: IAnalysisWorkbenchComponent

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.anonymous_duplicate`
              - Create an anonymous copy of the instance of a VGT component. The new component is not registered and will not be persisted nor restored when a scenario is saved or loaded.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.depends_on`
              - Test if the instance depends on another component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.duplicate`
              - Create a copy of the instance of a VGT component. The new component is automatically registered and will be persisted or restored when a scenario is saved or loaded.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.export`
              - Export the component to a file.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.rename`
              - Rename the component.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.category`
              - Allow the user to access or change the component category (Folder).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.component_type`
              - Return the component kind.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.context`
              - Return the context object associated with the instance. The returned object is either an instance of AnalysisWorkbenchComponentInstance or AnalysisWorkbenchComponentTemplate interface.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.description`
              - Return the component description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.embedded_components`
              - Return a collection of embedded components.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_duplicable`
              - Return whether the VGT component can be duplicated.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_read_only`
              - Return whether the component is modifiable.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_ready`
              - Return whether the component is ready. The component is ready if it's been fully initialized.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_valid`
              - Return whether the component is valid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.name`
              - Return the component name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.path`
              - Return the component's fully qualified path (ie. ``CentralBody/Earth Body``, etc.).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.qualified_path`
              - An STK-conformant path to the VGT component that can be used to visualize the VGT components in 3D (i.e. ``CentralBody/Earth Body Vector``, etc.).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.type_information`
              - Return the component type information.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IAnalysisWorkbenchComponent


Property detail
---------------

.. py:property:: category
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.category
    :type: str

    Allow the user to access or change the component category (Folder).

.. py:property:: component_type
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.component_type
    :type: VectorGeometryToolComponentType

    Return the component kind.

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.context
    :type: IAnalysisWorkbenchComponentContext

    Return the context object associated with the instance. The returned object is either an instance of AnalysisWorkbenchComponentInstance or AnalysisWorkbenchComponentTemplate interface.

.. py:property:: description
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.description
    :type: str

    Return the component description.

.. py:property:: embedded_components
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.embedded_components
    :type: AnalysisWorkbenchComponentCollection

    Return a collection of embedded components.

.. py:property:: is_duplicable
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_duplicable
    :type: bool

    Return whether the VGT component can be duplicated.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_read_only
    :type: bool

    Return whether the component is modifiable.

.. py:property:: is_ready
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_ready
    :type: bool

    Return whether the component is ready. The component is ready if it's been fully initialized.

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.is_valid
    :type: bool

    Return whether the component is valid.

.. py:property:: name
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.name
    :type: str

    Return the component name.

.. py:property:: path
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.path
    :type: str

    Return the component's fully qualified path (ie. ``CentralBody/Earth Body``, etc.).

.. py:property:: qualified_path
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.qualified_path
    :type: str

    An STK-conformant path to the VGT component that can be used to visualize the VGT components in 3D (i.e. ``CentralBody/Earth Body Vector``, etc.).

.. py:property:: type_information
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.type_information
    :type: AnalysisWorkbenchComponentTypeInformation

    Return the component type information.


Method detail
-------------

.. py:method:: anonymous_duplicate(self) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.anonymous_duplicate

    Create an anonymous copy of the instance of a VGT component. The new component is not registered and will not be persisted nor restored when a scenario is saved or loaded.

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`




.. py:method:: depends_on(self, component: IAnalysisWorkbenchComponent) -> bool
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.depends_on

    Test if the instance depends on another component.

    :Parameters:

        **component** : :obj:`~IAnalysisWorkbenchComponent`


    :Returns:

        :obj:`~bool`


.. py:method:: duplicate(self, new_name: str, description: str) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.duplicate

    Create a copy of the instance of a VGT component. The new component is automatically registered and will be persisted or restored when a scenario is saved or loaded.

    :Parameters:

        **new_name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`


.. py:method:: export(self, filename: str, comments: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.export

    Export the component to a file.

    :Parameters:

        **filename** : :obj:`~str`

        **comments** : :obj:`~str`


    :Returns:

        :obj:`~None`









.. py:method:: rename(self, new_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent.rename

    Rename the component.

    :Parameters:

        **new_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


