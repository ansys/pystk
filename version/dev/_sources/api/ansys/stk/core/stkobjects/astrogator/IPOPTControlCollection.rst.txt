IPOPTControlCollection
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection

   Properties for the list of IPOPT control parameters.

.. py:currentmodule:: IPOPTControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> IPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~IPOPTControl`

.. py:method:: item(self, index: int) -> IPOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IPOPTControl`


