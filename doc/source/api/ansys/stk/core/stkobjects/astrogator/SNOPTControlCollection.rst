SNOPTControlCollection
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection

   SNOPT control collection.

.. py:currentmodule:: SNOPTControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SNOPTControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> SNOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~SNOPTControl`

.. py:method:: item(self, index: int) -> SNOPTControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SNOPTControl`


