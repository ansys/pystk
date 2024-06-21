IComponentLinkEmbedControl
==========================

.. py:class:: ansys.stk.core.stkobjects.IComponentLinkEmbedControl

   object
   
   Interface for a control which manages the linking or embedding of a component from the component browser.

.. py:currentmodule:: IComponentLinkEmbedControl

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl.set_component`
              - Set the component by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl.reference_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl.component`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl.supported_components`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IComponentLinkEmbedControl


Property detail
---------------

.. py:property:: reference_type
    :canonical: ansys.stk.core.stkobjects.IComponentLinkEmbedControl.reference_type
    :type: COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE

    Gets or sets the component reference type.

.. py:property:: component
    :canonical: ansys.stk.core.stkobjects.IComponentLinkEmbedControl.component
    :type: IComponentInfo

    Get the component interface.

.. py:property:: supported_components
    :canonical: ansys.stk.core.stkobjects.IComponentLinkEmbedControl.supported_components
    :type: list

    Gets the list of supported component names.


Method detail
-------------





.. py:method:: set_component(self, componentName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IComponentLinkEmbedControl.set_component

    Set the component by name.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~None`

