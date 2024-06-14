ISceneCollection
================

.. py:class:: ISceneCollection

   object
   
   A collection of scenes.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return a scene in the collection at a specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISceneCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ISceneCollection.count
    :type: int

    Total number of scenes in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.ISceneCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index:int) -> "IScene"

    Return a scene in the collection at a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IScene"`


