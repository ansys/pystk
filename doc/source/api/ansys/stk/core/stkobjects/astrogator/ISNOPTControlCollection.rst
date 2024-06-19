ISNOPTControlCollection
=======================

.. py:class:: ISNOPTControlCollection

   object
   
   Properties for the list of SNOPT control parameters.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISNOPTControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> ISNOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISNOPTControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> ISNOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~ISNOPTControl`

