KmlGraphics
===========

.. py:class:: ansys.stk.core.graphics.KmlGraphics

   Provide loading and unloading of kml documents for a particular central body.

.. py:currentmodule:: KmlGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load_document`
              - Load a kml document from a uri.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load_document_string`
              - Load a kml document from a Uri.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load`
              - Load a kml document from a string containing the document.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load_document_async`
              - Load a kml document asynchronously from a uri. The document loaded event is raised when the document is loaded.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load_document_async_string`
              - Load a kml document asynchronously from a Uri. The document loaded event is raised when the document is loaded.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.load_async`
              - Load a kml document asynchronously from a string containing the document. The document loaded event is raised when the document is loaded.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.unload`
              - Unloads a kml document. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.unload_all`
              - Unloads all kml documents associated with this central body. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.
            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.Subscribe`
              - """Return an IKmlGraphicsEventHandler that is subscribed to handle events associated with this instance of KmlGraphics."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlGraphics.documents`
              - The collection of kml documents that are currently loaded.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlGraphics


Property detail
---------------

.. py:property:: documents
    :canonical: ansys.stk.core.graphics.KmlGraphics.documents
    :type: KmlDocumentCollection

    The collection of kml documents that are currently loaded.


Method detail
-------------


.. py:method:: load_document(self, kmlUri: str) -> KmlDocument
    :canonical: ansys.stk.core.graphics.KmlGraphics.load_document

    Load a kml document from a uri.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~KmlDocument`

.. py:method:: load_document_string(self, kmlUri: str) -> KmlDocument
    :canonical: ansys.stk.core.graphics.KmlGraphics.load_document_string

    Load a kml document from a Uri.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~KmlDocument`

.. py:method:: load(self, kmlDocument: str) -> KmlDocument
    :canonical: ansys.stk.core.graphics.KmlGraphics.load

    Load a kml document from a string containing the document.

    :Parameters:

    **kmlDocument** : :obj:`~str`

    :Returns:

        :obj:`~KmlDocument`

.. py:method:: load_document_async(self, kmlUri: str) -> None
    :canonical: ansys.stk.core.graphics.KmlGraphics.load_document_async

    Load a kml document asynchronously from a uri. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_document_async_string(self, kmlUri: str) -> None
    :canonical: ansys.stk.core.graphics.KmlGraphics.load_document_async_string

    Load a kml document asynchronously from a Uri. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlUri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_async(self, kmlDocument: str) -> None
    :canonical: ansys.stk.core.graphics.KmlGraphics.load_async

    Load a kml document asynchronously from a string containing the document. The document loaded event is raised when the document is loaded.

    :Parameters:

    **kmlDocument** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: unload(self, kmlDocument: KmlDocument) -> None
    :canonical: ansys.stk.core.graphics.KmlGraphics.unload

    Unloads a kml document. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.

    :Parameters:

    **kmlDocument** : :obj:`~KmlDocument`

    :Returns:

        :obj:`~None`

.. py:method:: unload_all(self) -> None
    :canonical: ansys.stk.core.graphics.KmlGraphics.unload_all

    Unloads all kml documents associated with this central body. All associated visual features will be removed from the Scene. Once a KmlDocument is unloaded, it is no longer valid and will throw when accessing properties or methods.

    :Returns:

        :obj:`~None`

