IComponentInfo
==============

.. py:class:: ansys.stk.core.stkobjects.IComponentInfo

   Interface for a component.

.. py:currentmodule:: IComponentInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.is_read_only`
              - Return true if the component is read-only.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.export`
              - Export the component with default component name as file name and component type as file extension to the scenario directory.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.export_with_filename_path`
              - Export the component with specified file name and location.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.name`
              - Get or set the component name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.user_comment`
              - Get or set the user comment for this component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfo.description`
              - Get the description for this component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IComponentInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.name
    :type: str

    Get or set the component name.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.user_comment
    :type: str

    Get or set the user comment for this component.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.description
    :type: str

    Get the description for this component.


Method detail
-------------






.. py:method:: is_read_only(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.is_read_only

    Return true if the component is read-only.

    :Returns:

        :obj:`~bool`

.. py:method:: export(self) -> None
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.export

    Export the component with default component name as file name and component type as file extension to the scenario directory.

    :Returns:

        :obj:`~None`

.. py:method:: export_with_filename_path(self, filename_path: str) -> None
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.export_with_filename_path

    Export the component with specified file name and location.

    :Parameters:

    **filename_path** : :obj:`~str`

    :Returns:

        :obj:`~None`

