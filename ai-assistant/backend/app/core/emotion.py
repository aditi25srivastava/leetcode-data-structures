from typing import Literal

Emotion = Literal["thinking", "happy", "sad", "excited", "confused", "listening", "neutral"]

KEYWORDS = {
    "happy": ["great", "awesome", "fantastic", "love", "congratulations", "happy", "excellent"],
    "sad": ["sorry", "unfortunately", "regret", "sad", "apologize", "mistake"],
    "excited": ["excited", "amazing", "thrilled", "super", "awesome", "wow", "celebrate"],
    "confused": ["confused", "unclear", "do not understand", "not sure", "why", "what do you mean"],
    "thinking": ["analyzing", "thinking", "considering", "let me", "review", "processing"],
}


def detect_emotion(text: str) -> Emotion:
    normalized = text.lower()
    for emotion, tokens in KEYWORDS.items():
        if any(token in normalized for token in tokens):
            return emotion  # type: ignore[return-value]
    if len(normalized) < 40 and "!" in normalized:
        return "excited"
    if "sorry" in normalized or "cannot" in normalized or "unable" in normalized:
        return "sad"
    return "neutral"
