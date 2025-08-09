SceneCollection
===============

.. py:class:: ansys.stk.core.graphics.SceneCollection

   A collection of scenes.

.. py:currentmodule:: SceneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneCollection.item`
              - Return a scene in the collection at a specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneCollection.count`
              - Total number of scenes in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.SceneCollection._new_enum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.SceneCollection.count
    :type: int

    Total number of scenes in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.SceneCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Scene
    :canonical: ansys.stk.core.graphics.SceneCollection.item

    Return a scene in the collection at a specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Scene`


