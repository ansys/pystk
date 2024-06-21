IKmlDocumentLoadedEventArgs
===========================

.. py:class:: ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs

   object
   
   The event is raised when a KML document has been loaded.

.. py:currentmodule:: IKmlDocumentLoadedEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.document`
            * - :py:attr:`~ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.exception`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlDocumentLoadedEventArgs


Property detail
---------------

.. py:property:: document
    :canonical: ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.document
    :type: IKmlDocument

    Gets the KML document associated with the load event.

.. py:property:: exception
    :canonical: ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs.exception
    :type: str

    Returns an error message, if an error occurred while loading the KML; otherwise an empty string.


