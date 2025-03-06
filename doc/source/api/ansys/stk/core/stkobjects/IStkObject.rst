IStkObject
==========

.. py:class:: ansys.stk.core.stkobjects.IStkObject

   Represents the instance of STK object.

.. py:currentmodule:: IStkObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.export`
              - Export the object to a file.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.is_object_coverage_supported`
              - Determine whether or not the object supports ObjectCoverage.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.is_access_supported`
              - Determine whether or not the object supports Access.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.get_access`
              - Return an IAgStkAccess object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.get_access_to_object`
              - Return an IAgStkAccess object associated with this STK object and another STK object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.create_one_point_access`
              - Create one point access to the supplied object name. The Remove method in IAgOnePtAccess should be called when you are done with the data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.unload`
              - Remove the object from the scenario.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.supports_analysis_workbench`
              - Return whether the object supports Vector Geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.copy_object`
              - Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.parent`
              - Return the parent object or null if the object has become orphaned. The exception is AgStkObjectRoot object which is a topmost element and does not have a parent.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.path`
              - Return the object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.instance_name`
              - A name of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.class_type`
              - Return a class type of the object (i.e. eAircraft, eFacility etc.).
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.class_name`
              - Return a class name of the object (i.e. Aircraft, Facility.).
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.children`
              - Return a collection of direct descendants of the current object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.root`
              - Return the Root object or null.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.data_providers`
              - Return the object representing a list of available data providers for the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.short_description`
              - The short description of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.long_description`
              - A long description of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.has_children`
              - Return true if the object has direct descendants.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.object_coverage`
              - Return an IAgStkObjectCoverage object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.access_constraints`
              - Get the constraints imposed on the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.object_files`
              - Return the list of files that constitute an object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.analysis_workbench_components`
              - Return an instance of Vector Geometry Tool provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.central_body_name`
              - The object's central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObject.metadata`
              - Get the object's metadata. Metadata is a collection of keys and their associated values.


Examples
--------

Create a New AdvCAT Object

.. code-block:: python

    # Scenario scenario: Scenario object
    advCAT = scenario.children.new(STKObjectType.ADVCAT, "MyAdvCAT")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObject


Property detail
---------------

.. py:property:: parent
    :canonical: ansys.stk.core.stkobjects.IStkObject.parent
    :type: IStkObject

    Return the parent object or null if the object has become orphaned. The exception is AgStkObjectRoot object which is a topmost element and does not have a parent.

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.IStkObject.path
    :type: str

    Return the object path.

.. py:property:: instance_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.instance_name
    :type: str

    A name of the object.

.. py:property:: class_type
    :canonical: ansys.stk.core.stkobjects.IStkObject.class_type
    :type: STKObjectType

    Return a class type of the object (i.e. eAircraft, eFacility etc.).

.. py:property:: class_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.class_name
    :type: str

    Return a class name of the object (i.e. Aircraft, Facility.).

.. py:property:: children
    :canonical: ansys.stk.core.stkobjects.IStkObject.children
    :type: IStkObjectCollection

    Return a collection of direct descendants of the current object.

.. py:property:: root
    :canonical: ansys.stk.core.stkobjects.IStkObject.root
    :type: StkObjectRoot

    Return the Root object or null.

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.IStkObject.data_providers
    :type: DataProviderCollection

    Return the object representing a list of available data providers for the object.

.. py:property:: short_description
    :canonical: ansys.stk.core.stkobjects.IStkObject.short_description
    :type: str

    The short description of the object.

.. py:property:: long_description
    :canonical: ansys.stk.core.stkobjects.IStkObject.long_description
    :type: str

    A long description of the object.

.. py:property:: has_children
    :canonical: ansys.stk.core.stkobjects.IStkObject.has_children
    :type: bool

    Return true if the object has direct descendants.

.. py:property:: object_coverage
    :canonical: ansys.stk.core.stkobjects.IStkObject.object_coverage
    :type: ObjectCoverage

    Return an IAgStkObjectCoverage object.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IStkObject.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the object.

.. py:property:: object_files
    :canonical: ansys.stk.core.stkobjects.IStkObject.object_files
    :type: list

    Return the list of files that constitute an object.

.. py:property:: analysis_workbench_components
    :canonical: ansys.stk.core.stkobjects.IStkObject.analysis_workbench_components
    :type: IAnalysisWorkbenchComponentProvider

    Return an instance of Vector Geometry Tool provider.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.central_body_name
    :type: str

    The object's central body.

.. py:property:: metadata
    :canonical: ansys.stk.core.stkobjects.IStkObject.metadata
    :type: KeyValueCollection

    Get the object's metadata. Metadata is a collection of keys and their associated values.


Method detail
-------------








.. py:method:: export(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.IStkObject.export

    Export the object to a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`








.. py:method:: is_object_coverage_supported(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObject.is_object_coverage_supported

    Determine whether or not the object supports ObjectCoverage.

    :Returns:

        :obj:`~bool`


.. py:method:: is_access_supported(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObject.is_access_supported

    Determine whether or not the object supports Access.

    :Returns:

        :obj:`~bool`

.. py:method:: get_access(self, object_path: str) -> Access
    :canonical: ansys.stk.core.stkobjects.IStkObject.get_access

    Return an IAgStkAccess object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.

    :Parameters:

    **object_path** : :obj:`~str`

    :Returns:

        :obj:`~Access`

.. py:method:: get_access_to_object(self, object: IStkObject) -> Access
    :canonical: ansys.stk.core.stkobjects.IStkObject.get_access_to_object

    Return an IAgStkAccess object associated with this STK object and another STK object.

    :Parameters:

    **object** : :obj:`~IStkObject`

    :Returns:

        :obj:`~Access`


.. py:method:: create_one_point_access(self, path_to_object: str) -> OnePointAccess
    :canonical: ansys.stk.core.stkobjects.IStkObject.create_one_point_access

    Create one point access to the supplied object name. The Remove method in IAgOnePtAccess should be called when you are done with the data.

    :Parameters:

    **path_to_object** : :obj:`~str`

    :Returns:

        :obj:`~OnePointAccess`


.. py:method:: unload(self) -> None
    :canonical: ansys.stk.core.stkobjects.IStkObject.unload

    Remove the object from the scenario.

    :Returns:

        :obj:`~None`

.. py:method:: supports_analysis_workbench(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObject.supports_analysis_workbench

    Return whether the object supports Vector Geometry.

    :Returns:

        :obj:`~bool`


.. py:method:: copy_object(self, new_object_name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObject.copy_object

    Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.

    :Parameters:

    **new_object_name** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`



