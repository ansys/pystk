IDifferentialCorrectorControlCollection
=======================================

.. py:class:: IDifferentialCorrectorControlCollection

   object
   
   Properties for the list of control parameters for a differential corrector profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`
            * - :py:meth:`~provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDifferentialCorrectorControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection.provide_runtime_type_info
    :type: IAgRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> IDifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDifferentialCorrectorControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IDifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IDifferentialCorrectorControl`


