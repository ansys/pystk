IGoldenSectionControlCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection

   object
   
   Properties for the list of Golden Section control parameters.

.. py:currentmodule:: IGoldenSectionControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGoldenSectionControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IGoldenSectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGoldenSectionControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IGoldenSectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IGoldenSectionControl`

