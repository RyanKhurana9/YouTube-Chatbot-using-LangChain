from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript(video_id: str, languages: list[str] = ["en"]) -> str:
    """
    Fetch and concatenate the transcript for a given YouTube video ID.

    Args:
        video_id:  The YouTube video ID (e.g. 'Gfr50f6ZBvo').
        languages: Preferred caption languages, in priority order.

    Returns:
        The full transcript as a single string.

    Raises:
        TranscriptsDisabled: If no captions are available for the video.
    """
    try:
        api      = YouTubeTranscriptApi()
        fetched  = api.fetch(video_id, languages=languages)
        return " ".join(chunk.text for chunk in fetched)

    except TranscriptsDisabled:
        raise TranscriptsDisabled(
            f"No captions available for video '{video_id}'."
        )
