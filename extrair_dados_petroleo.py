import pandas as pd
from datetime import datetime, timedelta

try:
    import yfinance as yf
except Exception:
    raise ImportError("[ERRO] A biblioteca 'yfinance' não está instalada. Instale usando: pip install yfinance")

SERIES_MAP = {
    "wti": "CL=F",   # WTI
    "brent": "BZ=F", # Brent
}

def _extract_close(df: pd.DataFrame) -> pd.Series:
    if df is None or df.empty:
        raise ValueError("[ERRO] Sem dados retornados pelo Yahoo Finance.")
    if "Close" in df.columns:
        close = df["Close"]
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]
        return close
    if isinstance(df.columns, pd.MultiIndex):
        try:
            close = df.xs("Close", level=0, axis=1)
            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]
            return close
        except (KeyError, ValueError):
            pass
    candidates = [c for c in df.columns if str(c).lower() == "close" or "close" in str(c).lower()]
    if candidates:
        close = df[candidates[0]]
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]
        return close
    raise ValueError("[ERRO] Não foi possível identificar a coluna de fechamento ('Close').")

def fetch_yahoo_series(ticker: str, start: str, end: str) -> pd.DataFrame:
    try:
        end_inclusive = (datetime.fromisoformat(end) + timedelta(days=1)).date().isoformat()
    except Exception:
        end_inclusive = end

    df = yf.download(
        tickers=ticker,
        start=start,
        end=end_inclusive,
        interval="1d",
        progress=False,
        auto_adjust=False,
        threads=True,
        group_by="column",
    )

    close = _extract_close(df)

    out = close.reset_index()
    if "Date" in out.columns:
        out = out.rename(columns={"Date": "ds", close.name: "price"})
    else:
        out = out.rename(columns={out.columns[0]: "ds", close.name: "price"})
    out["ds"] = pd.to_datetime(out["ds"])
    out["price"] = pd.to_numeric(out["price"], errors="coerce")
    out = out.dropna(subset=["price"]).sort_values("ds").reset_index(drop=True)

    mask = (out["ds"] >= pd.to_datetime(start)) & (out["ds"] <= pd.to_datetime(end))
    out = out.loc[mask].reset_index(drop=True)
    return out

def extrair_dados_petroleo(series: str, inicio: str, fim: str) -> pd.DataFrame:
    """
    Função para extrair dados de preços diários do petróleo (WTI/Brent).

    Args:
        series (str): Série desejada, "wti" ou "brent".
        inicio (str): Data inicial no formato "YYYY-MM-DD".
        fim (str): Data final no formato "YYYY-MM-DD".

    Returns:
        pd.DataFrame: DataFrame contendo as colunas "ds" (datas) e "price" (preços).
    """
    if series not in SERIES_MAP:
        raise ValueError("Série inválida. Escolha entre 'wti' ou 'brent'.")

    ticker = SERIES_MAP[series]
    return fetch_yahoo_series(ticker, inicio, fim)