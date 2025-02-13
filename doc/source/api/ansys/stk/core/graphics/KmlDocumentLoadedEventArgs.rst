KmlDocumentLoadedEventArgs
==========================

.. py:class:: ansys.stk.core.graphics.KmlDocumentLoadedEventArgs

   The event is raised when a KML document has been loaded.

.. py:currentmodule:: KmlDocumentLoadedEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlDocumentLoadedEventArgs.document`
              - Get the KML document associated with the load event.
            * - :py:attr:`~ansys.stk.core.graphics.KmlDocumentLoadedEventArgs.exception`
              - Return an error message, if an error occurred while loading the KML; otherwise an empty string.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlDocumentLoadedEventArgs


Property detail
---------------

.. py:property:: document
    :canonical: ansys.stk.core.graphics.KmlDocumentLoadedEventArgs.document
    :type: KmlDocument

    Get the KML document associated with the load event.

.. py:property:: exception
    :canonical: ansys.stk.core.graphics.KmlDocumentLoadedEventArgs.exception
    :type: str

    Return an error message, if an error occurred while loading the KML; otherwise an empty string.


