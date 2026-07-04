def analyze_text(transcript, speakers):

    # ==========================================
    # EXTRACT DATA
    # ==========================================
    text = transcript.get("text", "")

    # ==========================================
    # BASIC TEXT ANALYSIS
    # ==========================================
    words = text.split()
    word_count = len(words)

    sentences = [
        s.strip()
        for s in text.split(".")
        if s.strip()
    ]

    sentence_count = len(sentences)

    avg_words_per_sentence = round(
        word_count / max(sentence_count, 1),
        2
    )

    # ==========================================
    # SENTIMENT ANALYSIS
    # ==========================================
    lower = text.lower()

    positive_words = {
        "good",
        "great",
        "happy",
        "excellent",
        "awesome",
        "love",
        "amazing",
        "perfect",
        "best",
        "excited",
        "motivated",
        "engaging",
        "energy",
        "passionate",
        "success",
        "positive"
    }

    negative_words = {
        "bad",
        "sad",
        "angry",
        "hate",
        "problem",
        "worst",
        "issue",
        "error",
        "fail",
        "wrong",
        "negative"
    }

    pos_score = sum(
        1 for word in positive_words
        if word in lower
    )

    neg_score = sum(
        1 for word in negative_words
        if word in lower
    )

    if pos_score > neg_score:
        sentiment = "Positive"
        emoji = "😊"

    elif neg_score > pos_score:
        sentiment = "Negative"
        emoji = "😟"

    else:
        sentiment = "Neutral"
        emoji = "😐"

    # ==========================================
    # SUMMARY
    # ==========================================
    if len(sentences) > 0:
        summary = sentences[0][:250]
    else:
        summary = "No meaningful conversation detected."

    # ==========================================
    # MAIN TOPICS DETECTION
    # ==========================================
    keywords = []

    topic_words = [
        "ai",
        "technology",
        "meeting",
        "project",
        "audio",
        "speech",
        "engagement",
        "learning",
        "motivation",
        "conversation",
        "business",
        "research",
        "presentation",
        "listener",
        "speaker"
    ]

    for word in topic_words:
        if word in lower:
            keywords.append(word.capitalize())

    if not keywords:
        keywords.append("General Discussion")

    # ==========================================
    # IMPORTANT EVENTS
    # ==========================================
    important_events = []

    if "launch" in lower:
        important_events.append(
            "A launch or release was mentioned."
        )

    if "meeting" in lower:
        important_events.append(
            "A meeting discussion was detected."
        )

    if "project" in lower:
        important_events.append(
            "Project-related discussion identified."
        )

    if not important_events:
        important_events.append(
            "No major events detected in the transcript."
        )

    # ==========================================
    # EMOTION ANALYSIS
    # ==========================================
    emotions = []

    if "excited" in lower or "amazing" in lower:
        emotions.append(
            "Enthusiastic: The speaker sounds energetic and positive."
        )

    if "motivate" in lower or "encourage" in lower:
        emotions.append(
            "Motivational: The conversation encourages action."
        )

    if "important" in lower:
        emotions.append(
            "Serious: Important ideas are being emphasized."
        )

    if "passionate" in lower:
        emotions.append(
            "Passionate: Strong interest and emotion detected."
        )

    if not emotions:
        emotions.append(
            "Neutral: No strong emotional tone detected."
        )

    # ==========================================
    # INTENT DETECTION
    # ==========================================
    intents = []

    if "learn" in lower or "understand" in lower:
        intents.append(
            "To share knowledge or explain concepts."
        )

    if "project" in lower:
        intents.append(
            "To discuss project-related ideas."
        )

    if "engage" in lower or "listener" in lower:
        intents.append(
            "To keep the audience engaged and interested."
        )

    if "presentation" in lower:
        intents.append(
            "To deliver an informative presentation."
        )

    if not intents:
        intents.append(
            "General communication and discussion."
        )

    # ==========================================
    # FORMAT OUTPUT SECTIONS
    # ==========================================
    topics_text = "\n".join(
        [f"- {topic}" for topic in keywords]
    )

    events_text = "\n".join(
        [f"- {event}" for event in important_events]
    )

    emotions_text = "\n".join(
        [f"- {emotion}" for emotion in emotions]
    )

    intents_text = "\n".join(
        [f"- {intent}" for intent in intents]
    )

    # ==========================================
    # FINAL AI REPORT
    # ==========================================
    result = f"""
# 🧠 AI REASONING REPORT

## 📝 TRANSCRIPTION

{text}

---

# 🧠 AI REASONING

Here's the analysis of the conversation:

---

## 1. SUMMARY

The conversation mainly discusses:

"{summary}"

---

## 2. MAIN TOPICS

{topics_text}

---

## 3. IMPORTANT EVENTS

{events_text}

---

## 4. TRANSCRIPT ANALYTICS

- Total Words: {word_count}
- Total Sentences: {sentence_count}
- Average Words Per Sentence: {avg_words_per_sentence}

---

## 5. EMOTION ANALYSIS

{emotions_text}

---

## 6. SENTIMENT ANALYSIS

{emoji} Overall Sentiment: {sentiment}

---

## 7. INTENT DETECTION

{intents_text}

---

## 8. AI INTERPRETATION

This transcript contains {word_count} words.

The overall tone appears to be **{sentiment}**.

The AI system detected conversational patterns,
emotional tone, topic relevance,
and communication intent.

---

## 🧾 FULL TRANSCRIPT

{text}

"""

    return result