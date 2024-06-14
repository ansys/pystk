ITimeToolEventIntervalCollectionFactory
=======================================

.. py:class:: ITimeToolEventIntervalCollectionFactory

   object
   
   The factory creates collections of event interval lists.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and register an event interval collection using specified name, description, and type.
            * - :py:meth:`~create_event_interval_collection_lighting`
              - Create an event interval collection defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.
            * - :py:meth:`~create_event_interval_collection_signaled`
              - Create an event interval collection recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create_event_interval_collection_satisfaction`
              - Create an event interval collection containing intervals during which condition set is satisfied.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalCollectionFactory



Method detail
-------------

.. py:method:: create(self, name:str, description:str, type:"CRDN_EVENT_INTERVAL_COLLECTION_TYPE") -> "ITimeToolEventIntervalCollection"

    Create and register an event interval collection using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~"CRDN_EVENT_INTERVAL_COLLECTION_TYPE"`

    :Returns:

        :obj:`~"ITimeToolEventIntervalCollection"`

.. py:method:: create_event_interval_collection_lighting(self, name:str, description:str) -> "ITimeToolEventIntervalCollection"

    Create an event interval collection defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~"ITimeToolEventIntervalCollection"`

.. py:method:: create_event_interval_collection_signaled(self, name:str, description:str) -> "ITimeToolEventIntervalCollection"

    Create an event interval collection recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~"ITimeToolEventIntervalCollection"`

.. py:method:: is_type_supported(self, eType:"CRDN_EVENT_INTERVAL_COLLECTION_TYPE") -> bool

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~"CRDN_EVENT_INTERVAL_COLLECTION_TYPE"`

    :Returns:

        :obj:`~bool`

.. py:method:: create_event_interval_collection_satisfaction(self, name:str, description:str) -> "ITimeToolEventIntervalCollection"

    Create an event interval collection containing intervals during which condition set is satisfied.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~"ITimeToolEventIntervalCollection"`

