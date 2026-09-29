"""
Public demo version of Iran Store Map Extractor.

This file shows the project structure and main workflow without publishing the
full private extraction logic. It is suitable for a public GitHub portfolio.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd


SHOP_TYPES = {
    "supermarket": "سوپرمارکت",
    "convenience": "فروشگاه محلی/خواربار",
    "bakery": "نانوایی",
    "dairy": "لبنیاتی",
    "wholesale": "عمده فروشی",
    "mall": "مرکز خرید",
}


def get_area_query(city: str | None, province: str | None) -> str:
    """Build a simple search area label."""
    if city:
        return f"{city}, Iran"
    if province:
        return f"{province} Province, Iran"
    return "Tehran, Iran"


def fetch_store_records(area_query: str) -> list[dict[str, object]]:
    """
    Placeholder for the private extraction logic.

    The private version resolves map areas, queries public map records, handles
    retries, cleans tags, and exports structured store data.
    """
    return [
        {
            "نام فروشگاه": "Sample Store",
            "نوع فروشگاه": SHOP_TYPES["supermarket"],
            "shop_tag": "supermarket",
            "استان/شهر جستجو": area_query,
            "آدرس": "Sample address",
            "lat": 35.7000,
            "lon": 51.4000,
            "source": "OpenStreetMap/Overpass",
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    ]


def clean_records(records: list[dict[str, object]]) -> pd.DataFrame:
    """Convert records to a clean DataFrame and remove duplicate rows."""
    df = pd.DataFrame(records)
    if df.empty:
        return df

    df = df.drop_duplicates()
    return df.sort_values(["استان/شهر جستجو", "نوع فروشگاه", "نام فروشگاه"])


def save_output(df: pd.DataFrame, output_path: str) -> None:
    """Save extracted records as Excel or CSV."""
    path = Path(output_path)

    if path.suffix.lower() == ".xlsx":
        df.to_excel(path, index=False)
        return

    if path.suffix.lower() == ".csv":
        df.to_csv(path, index=False, encoding="utf-8-sig")
        return

    raise ValueError("Output file must end with .xlsx or .csv")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Public demo store extractor.")
    parser.add_argument("--city", help='Example: "Tehran"')
    parser.add_argument("--province", help='Example: "East Azerbaijan"')
    parser.add_argument("--output", default="sample_stores.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    area_query = get_area_query(args.city, args.province)
    records = fetch_store_records(area_query)
    df = clean_records(records)
    save_output(df, args.output)
    print(f"Saved {len(df)} sample rows to {args.output}")


if __name__ == "__main__":
    main()

