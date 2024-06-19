IStkObject
==========

.. py:class:: IStkObject

   object
   
   Represents the instance of STK object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~export`
              - Export the object to a file.
            * - :py:meth:`~is_object_coverage_supported`
              - Determine whether or not the object supports ObjectCoverage.
            * - :py:meth:`~is_access_supported`
              - Determine whether or not the object supports Access.
            * - :py:meth:`~get_access`
              - Return an IAgStkAccess object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.
            * - :py:meth:`~get_access_to_object`
              - Return an IAgStkAccess object associated with this STK object and another STK object.
            * - :py:meth:`~create_one_point_access`
              - Create one point access to the supplied object name. The Remove method in IAgOnePtAccess should be called when you are done with the data.
            * - :py:meth:`~unload`
              - Remove the object from the scenario.
            * - :py:meth:`~is_vgt_supported`
              - Return whether the object supports Vector Geometry.
            * - :py:meth:`~copy_object`
              - Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~parent`
            * - :py:meth:`~path`
            * - :py:meth:`~instance_name`
            * - :py:meth:`~class_type`
            * - :py:meth:`~class_name`
            * - :py:meth:`~children`
            * - :py:meth:`~root`
            * - :py:meth:`~data_providers`
            * - :py:meth:`~short_description`
            * - :py:meth:`~long_description`
            * - :py:meth:`~has_children`
            * - :py:meth:`~object_coverage`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~object_files`
            * - :py:meth:`~vgt`
            * - :py:meth:`~central_body_name`
            * - :py:meth:`~metadata`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObject


Property detail
---------------

.. py:property:: parent
    :canonical: ansys.stk.core.stkobjects.IStkObject.parent
    :type: IAgStkObject

    Returns the parent object or null if the object has become orphaned. The exception is AgStkObjectRoot object which is a topmost element and does not have a parent.

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.IStkObject.path
    :type: str

    Returns the object path.

.. py:property:: instance_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.instance_name
    :type: str

    A name of the object.

.. py:property:: class_type
    :canonical: ansys.stk.core.stkobjects.IStkObject.class_type
    :type: STK_OBJECT_TYPE

    Returns a class type of the object (i.e. eAircraft, eFacility etc.).

.. py:property:: class_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.class_name
    :type: str

    Returns a class name of the object (i.e. Aircraft, Facility.).

.. py:property:: children
    :canonical: ansys.stk.core.stkobjects.IStkObject.children
    :type: IAgStkObjectCollection

    Returns a collection of direct descendants of the current object.

.. py:property:: root
    :canonical: ansys.stk.core.stkobjects.IStkObject.root
    :type: IAgStkObjectRoot

    Returns the Root object or null.

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.IStkObject.data_providers
    :type: IAgDataProviderCollection

    Returns the object representing a list of available data providers for the object.

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

    Returns true if the object has direct descendants.

.. py:property:: object_coverage
    :canonical: ansys.stk.core.stkobjects.IStkObject.object_coverage
    :type: IAgStkObjectCoverage

    Returns an IAgStkObjectCoverage object.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IStkObject.access_constraints
    :type: IAgAccessConstraintCollection

    Get the constraints imposed on the object.

.. py:property:: object_files
    :canonical: ansys.stk.core.stkobjects.IStkObject.object_files
    :type: list

    Returns the list of files that constitute an object.

.. py:property:: vgt
    :canonical: ansys.stk.core.stkobjects.IStkObject.vgt
    :type: IAgCrdnProvider

    Returns an instance of Vector Geometry Tool provider.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IStkObject.central_body_name
    :type: str

    The object's central body.

.. py:property:: metadata
    :canonical: ansys.stk.core.stkobjects.IStkObject.metadata
    :type: IAgKeyValueCollection

    Gets the object's metadata. Metadata is a collection of keys and their associated values.


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

.. py:method:: get_access(self, objectPath: str) -> IStkAccess
    :canonical: ansys.stk.core.stkobjects.IStkObject.get_access

    Return an IAgStkAccess object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~IStkAccess`

.. py:method:: get_access_to_object(self, pObject: IStkObject) -> IStkAccess
    :canonical: ansys.stk.core.stkobjects.IStkObject.get_access_to_object

    Return an IAgStkAccess object associated with this STK object and another STK object.

    :Parameters:

    **pObject** : :obj:`~IStkObject`

    :Returns:

        :obj:`~IStkAccess`


.. py:method:: create_one_point_access(self, pathToObject: str) -> IOnePointAccess
    :canonical: ansys.stk.core.stkobjects.IStkObject.create_one_point_access

    Create one point access to the supplied object name. The Remove method in IAgOnePtAccess should be called when you are done with the data.

    :Parameters:

    **pathToObject** : :obj:`~str`

    :Returns:

        :obj:`~IOnePointAccess`


.. py:method:: unload(self) -> None
    :canonical: ansys.stk.core.stkobjects.IStkObject.unload

    Remove the object from the scenario.

    :Returns:

        :obj:`~None`

.. py:method:: is_vgt_supported(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObject.is_vgt_supported

    Return whether the object supports Vector Geometry.

    :Returns:

        :obj:`~bool`


.. py:method:: copy_object(self, newObjectName: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObject.copy_object

    Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.

    :Parameters:

    **newObjectName** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`



