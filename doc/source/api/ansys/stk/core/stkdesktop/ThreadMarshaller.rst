ThreadMarshaller
================

.. py:class:: ansys.stk.core.stkdesktop.ThreadMarshaller

   object

.. py:currentmodule:: ThreadMarshaller


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkdesktop.ThreadMarshaller.get_marshalled_to_current_thread`
              - Return an instance of the original stk_object that may be used on the current thread. May only be called once.
            * - :py:attr:`~ansys.stk.core.stkdesktop.ThreadMarshaller.initialize_thread`
              - Must be called on the destination thread prior to calling GetMarshalledToCurrentThread().
            * - :py:attr:`~ansys.stk.core.stkdesktop.ThreadMarshaller.release_thread`
              - Call in the destination thread after all calls to STK are finished.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkdesktop import ThreadMarshaller


Method detail
-------------

.. py:method:: get_marshalled_to_current_thread(self)
    :canonical: ansys.stk.core.stkdesktop.ThreadMarshaller.get_marshalled_to_current_thread

    Return an instance of the original stk_object that may be used on the current thread. May only be called once.

.. py:method:: initialize_thread(self) -> None
    :canonical: ansys.stk.core.stkdesktop.ThreadMarshaller.initialize_thread

    Must be called on the destination thread prior to calling GetMarshalledToCurrentThread().

    :Returns:

        :obj:`~None`

.. py:method:: release_thread(self) -> None
    :canonical: ansys.stk.core.stkdesktop.ThreadMarshaller.release_thread

    Call in the destination thread after all calls to STK are finished.

    :Returns:

        :obj:`~None`


