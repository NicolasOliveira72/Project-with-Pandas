import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

dataset = Path(__file__).parent / "datasets"
dataset.mkdir(parents=True, exist_ok=True)
