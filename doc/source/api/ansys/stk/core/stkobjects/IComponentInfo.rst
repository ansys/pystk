IComponentInfo
==============

.. py:class:: IComponentInfo

   object
   
   Interface for a component.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_read_only`
              - Return true if the component is read-only.
            * - :py:meth:`~export`
              - Export the component with default component name as file name and component type as file extension to the scenario directory.
            * - :py:meth:`~export_with_filename_path`
              - Export the component with specified file name and location.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~user_comment`
            * - :py:meth:`~description`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IComponentInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.name
    :type: str

    Gets or sets the component name.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.user_comment
    :type: str

    Gets or sets the user comment for this component.

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

.. py:method:: export_with_filename_path(self, filenamePath: str) -> None
    :canonical: ansys.stk.core.stkobjects.IComponentInfo.export_with_filename_path

    Export the component with specified file name and location.

    :Parameters:

    **filenamePath** : :obj:`~str`

    :Returns:

        :obj:`~None`

