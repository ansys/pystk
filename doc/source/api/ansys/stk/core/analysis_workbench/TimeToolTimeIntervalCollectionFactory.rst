TimeToolTimeIntervalCollectionFactory
=====================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory

   The factory creates collections of event interval lists.

.. py:currentmodule:: TimeToolTimeIntervalCollectionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create`
              - Create and register an event interval collection using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_lighting`
              - Create an event interval collection defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_satisfaction`
              - Create an event interval collection containing intervals during which condition set is satisfied.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_signaled`
              - Create an event interval collection recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalCollectionFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: EventIntervalCollectionType) -> ITimeToolTimeIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create

    Create and register an event interval collection using specified name, description, and type.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~EventIntervalCollectionType`


    :Returns:

        :obj:`~ITimeToolTimeIntervalCollection`

.. py:method:: create_lighting(self, name: str, description: str) -> ITimeToolTimeIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_lighting

    Create an event interval collection defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolTimeIntervalCollection`

.. py:method:: create_satisfaction(self, name: str, description: str) -> ITimeToolTimeIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_satisfaction

    Create an event interval collection containing intervals during which condition set is satisfied.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolTimeIntervalCollection`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolTimeIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.create_signaled

    Create an event interval collection recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolTimeIntervalCollection`

.. py:method:: is_type_supported(self, type: EventIntervalCollectionType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~EventIntervalCollectionType`


    :Returns:

        :obj:`~bool`

