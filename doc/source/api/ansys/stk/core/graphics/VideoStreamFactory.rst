VideoStreamFactory
==================

.. py:class:: ansys.stk.core.graphics.VideoStreamFactory

   A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

.. py:currentmodule:: VideoStreamFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.VideoStreamFactory.initialize_with_string_uri`
              - Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStreamFactory.initialize_with_string_uri_and_audio`
              - Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStreamFactory.initialize_audio_video_with_string_uri`
              - Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import VideoStreamFactory



Method detail
-------------

.. py:method:: initialize_with_string_uri(self, uri: str) -> VideoStream
    :canonical: ansys.stk.core.graphics.VideoStreamFactory.initialize_with_string_uri

    Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~VideoStream`

.. py:method:: initialize_with_string_uri_and_audio(self, uri: str, loadAudio: bool) -> VideoStream
    :canonical: ansys.stk.core.graphics.VideoStreamFactory.initialize_with_string_uri_and_audio

    Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

    :Parameters:

    **uri** : :obj:`~str`
    **loadAudio** : :obj:`~bool`

    :Returns:

        :obj:`~VideoStream`

.. py:method:: initialize_audio_video_with_string_uri(self, uri: str, audioUri: str) -> VideoStream
    :canonical: ansys.stk.core.graphics.VideoStreamFactory.initialize_audio_video_with_string_uri

    Initialize the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

    :Parameters:

    **uri** : :obj:`~str`
    **audioUri** : :obj:`~str`

    :Returns:

        :obj:`~VideoStream`

