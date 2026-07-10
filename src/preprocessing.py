import re
import html
from pathlib import Path
from data_loader import load_data

def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"#(\w+)", r"\1", text)
    text = html.unescape(text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text

def preprocess_data(df):
    processed_df = df[
        ["target", "text"]
    ].copy()

    processed_df["target"] = (
        processed_df["target"]
        .map({
            0: 0,
            4: 1,
        })
    )

    processed_df["cleaned_text"] = (
        processed_df["text"]
        .apply(clean_text)
    )

    return processed_df


